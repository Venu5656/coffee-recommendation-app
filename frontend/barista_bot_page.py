import streamlit as st
from html import escape
from urllib.parse import quote

from barista_bot import BaristaBot
from backend_client import CoffeeBackendClient
from history import HistoryTracker
from recommendation_engine import _composition_cup_html, _cup_html
from visualization import load_coffee_profiles, render_hot_cup, render_cold_glass


CUSTOM_DRINKS = [
    {
        "name": "Espresso Tonic",
        "description": "A bright iced espresso drink with tonic water, citrus lift, and a crisp cafe finish.",
        "tags": ("tonic", "sparkling", "citrus", "refreshing", "iced", "adventurous"),
        "equipment": ("espresso machine or moka pot", "glass", "ice"),
        "ingredients": ("1 double shot espresso", "120-150 ml chilled tonic water", "ice", "optional orange peel"),
        "steps": ("Fill a glass with ice and tonic first.", "Pour espresso slowly over the back of a spoon.", "Add orange peel if you want a brighter aroma.", "Stir gently just before drinking."),
        "tips": ("Use very cold tonic so the drink stays lively.", "A concentrated moka pot brew works if you do not have espresso."),
    },
    {
        "name": "Vietnamese Iced Coffee",
        "description": "A bold sweet iced coffee built from dark coffee and condensed milk.",
        "tags": ("vietnamese", "condensed", "sweet", "strong", "iced", "rich"),
        "equipment": ("phin filter or strong brew method", "glass", "ice"),
        "ingredients": ("2-3 tablespoons sweetened condensed milk", "90-120 ml strong dark coffee", "ice"),
        "steps": ("Add condensed milk to a glass.", "Brew or pour strong coffee over it.", "Stir until fully combined.", "Pour over ice and serve."),
        "tips": ("Use darker roast coffee for the right intensity.", "Make the coffee stronger rather than adding more sweetness if it tastes flat."),
    },
    {
        "name": "Dirty Chai Latte",
        "description": "A chai latte sharpened with espresso for a spiced, comforting cup.",
        "tags": ("chai", "spiced", "comforting", "milky", "hot"),
        "equipment": ("espresso machine or moka pot", "saucepan or milk steamer"),
        "ingredients": ("1 shot espresso", "180 ml chai concentrate or strong chai", "120 ml milk"),
        "steps": ("Prepare a strong chai base.", "Heat or steam the milk until silky.", "Pour chai into the cup, then add espresso.", "Finish with milk and optional cinnamon."),
        "tips": ("Use less chai if you want more coffee definition.", "Oat milk works especially well here."),
    },
    {
        "name": "Shakerato",
        "description": "An Italian-style shaken espresso that feels colder, lighter, and more elegant than standard iced coffee.",
        "tags": ("shakerato", "refreshing", "smooth", "iced", "light"),
        "equipment": ("cocktail shaker or sealed jar", "ice"),
        "ingredients": ("2 shots espresso", "ice", "optional sugar syrup"),
        "steps": ("Pull the espresso shots fresh.", "Add them to a shaker with ice and optional syrup.", "Shake hard for 10-15 seconds.", "Strain into a chilled glass."),
        "tips": ("Shake hard enough to build a light foam on top.", "Drink quickly while the texture is still lively."),
    },
]


KNOWLEDGE_TOPICS = [
    {
        "title": "Latte vs Cappuccino",
        "keywords": ("latte", "cappuccino", "difference", "compare", "versus", "vs"),
        "summary": "A latte is milkier and smoother, while a cappuccino is foamier and feels lighter on the palate.",
        "bullets": ("Lattes carry more steamed milk, so they taste softer.", "Cappuccinos use a more pronounced foam layer.", "Choose latte for creaminess and cappuccino for stronger coffee definition."),
    },
    {
        "title": "Cold Brew vs Iced Coffee",
        "keywords": ("cold brew", "iced coffee", "iced americano"),
        "summary": "Cold brew is extracted cold over time; iced coffee styles are brewed hot first and chilled or served over ice.",
        "bullets": ("Cold brew usually tastes smoother and rounder.", "Iced coffee styles feel brighter and more immediate.", "Choose iced Americano for a clean crisp cup."),
    },
    {
        "title": "Coffee Ratios and Extraction",
        "keywords": ("ratio", "extraction", "grind", "dose", "brew time", "water temperature"),
        "summary": "Good brewing usually comes down to ratio, grind size, contact time, and water temperature.",
        "bullets": ("Ratio controls strength and balance.", "Finer grind usually extracts faster.", "Taste should guide adjustment more than fixed recipes."),
    },
    {
        "title": "Coffee Terms",
        "keywords": ("what is", "term", "body", "mouthfeel", "arabica", "robusta", "roast"),
        "summary": "Coffee terms usually describe extraction balance, mouthfeel, roast behavior, or preparation style.",
        "bullets": ("Body means how heavy or light coffee feels.", "Under-extracted coffee often tastes sour or thin.", "Over-extracted coffee often tastes bitter or dry."),
    },
]


def render_barista_bot_page(client: CoffeeBackendClient | None = None):
    """Render the Barista Bot conversational interface."""
    if st.query_params.get("barista_action", "") == "reset":
        for key in (
            "barista_bot",
            "barista_bot_started",
            "barista_bot_messages",
            "barista_latest",
        ):
            st.session_state.pop(key, None)
        st.query_params.clear()
        st.rerun()

    prompt_examples = [
        "I'm tired but want something smooth",
        "How do I make cold brew at home?",
        "What is the difference between latte and cappuccino?",
        "Surprise me with something off menu",
    ]
    prompt_links = "".join(
        f'<a href="?barista_prompt={quote(prompt)}"><span>Try</span>{escape(prompt)}</a>'
        for prompt in prompt_examples
    )

    st.markdown(
        f"""
        <section class="barista-local-hero">
          <div>
            <span>Local Barista Assistant</span>
            <h1>Ask for a drink, a brew guide, or coffee knowledge.</h1>
          </div>
          <a href="?barista_action=reset">Clear chat</a>
        </section>
        <section class="barista-mode-strip">
          <div>
            <span>Quick starts</span>
            <strong>Recommendation, recipe, knowledge, or off-menu idea.</strong>
          </div>
          <nav>{prompt_links}</nav>
        </section>
        """,
        unsafe_allow_html=True,
    )

    if "barista_bot" not in st.session_state:
        st.session_state.barista_bot = BaristaBot()
        st.session_state.barista_bot_started = False
        st.session_state.barista_bot_messages = [
            {
                "role": "barista",
                "content": "Ask for a coffee recommendation, an off-menu drink, brewing help, or coffee knowledge. I can act like an experienced barista, not just a menu picker.",
            }
        ]

    barista = st.session_state.barista_bot

    if not st.session_state.barista_bot_started:
        st.session_state.barista_bot_started = True

    quick_prompt = st.query_params.get("barista_prompt", "")
    if quick_prompt:
        _send_barista_message(quick_prompt, barista, client or CoffeeBackendClient(use_mock=True))
        st.query_params.clear()
        st.rerun()

    context = barista.get_context()
    concerns = ", ".join(context.concerns) if context.concerns else "None yet"

    st.markdown(
        f"""
        <section class="barista-signal-row">
          <div><span>Mood</span><strong>{escape(context.mood.title())}</strong></div>
          <div><span>Temperature</span><strong>{escape(context.temperature_pref.title())}</strong></div>
          <div><span>Setting</span><strong>{escape(context.location.title())}</strong></div>
          <div><span>Effort</span><strong>{escape(context.effort_pref.title())}</strong></div>
          <div><span>Watchouts</span><strong>{escape(concerns.title())}</strong></div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    chat_col, latest_col = st.columns([1.04, 0.96], gap="large")

    with chat_col:
        st.markdown(
            """
            <section class="barista-ai-chat-panel">
              <header>
                <div>
                  <span>Conversation</span>
                  <strong>Tell the assistant what kind of answer you want.</strong>
                </div>
              </header>
              <div class="barista-ai-scroll">
            """,
            unsafe_allow_html=True,
        )

        total = len(st.session_state.barista_bot_messages)
        for i, message in enumerate(st.session_state.barista_bot_messages):
            role = "user" if message["role"] == "user" else "barista"
            label = "Customer" if role == "user" else "Barista"
            delay = max(0.0, (total - 1 - i) * 0.055)
            st.markdown(
                f"""
                <div class="barista-ai-row {role}" style="animation-delay:{delay:.2f}s">
                  <div>
                    <span>{label}</span>
                    <p>{escape(message["content"])}</p>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div></section>", unsafe_allow_html=True)

        with st.form("barista_ai_form", clear_on_submit=True):
            st.markdown('<div id="barista-ai-input-marker"></div>', unsafe_allow_html=True)
            input_col, send_col = st.columns([0.72, 0.28], gap="small")
            with input_col:
                user_input = st.text_area(
                    "Message",
                    placeholder="I'm tired but want something comforting and not too strong.",
                    label_visibility="collapsed",
                    key="barista_input_area",
                    height=96,
                )
            with send_col:
                send_button = st.form_submit_button("Ask Barista", use_container_width=True)

        if send_button and user_input.strip():
            _send_barista_message(
                user_input,
                barista,
                client or CoffeeBackendClient(use_mock=True),
            )
            st.rerun()

    with latest_col:
        _render_barista_latest(st.session_state.get("barista_latest"), barista)


def _send_barista_message(message: str, barista: BaristaBot, backend_client: CoffeeBackendClient) -> None:
    st.session_state.barista_bot_messages.append({"role": "user", "content": message})
    conversation = _backend_conversation(st.session_state.barista_bot_messages)
    latest = _build_barista_response(message, barista, backend_client, conversation)
    st.session_state.barista_latest = latest
    st.session_state.barista_bot_messages.append({"role": "barista", "content": str(latest.get("reply", ""))})


def _backend_conversation(messages: list[dict]) -> list[dict[str, str]]:
    conversation: list[dict[str, str]] = []
    for message in messages:
        role = "assistant" if message.get("role") == "barista" else str(message.get("role", "user"))
        content = str(message.get("content", "")).strip()
        if content:
            conversation.append({"role": role, "content": content})
    return conversation


def _history_events_for_backend() -> list[dict]:
    events = []
    for item in HistoryTracker().get_recent(50):
        events.append(
            {
                "type": "chat",
                "recommendation": item.drink_name,
                "timestamp": item.timestamp,
                "matchScore": item.match_score,
                "preferences": {
                    "mood": item.mood,
                    "time": item.time_of_day,
                    "temperature": item.temperature,
                    "location": item.location,
                },
                "metadata": {"composition": item.composition or {}},
            }
        )
    return events


def _display_preferences(preferences: dict | None, barista: BaristaBot) -> dict:
    preferences = preferences or {}
    return {
        "Mood": str(preferences.get("mood") or barista.context.mood).title(),
        "Taste": str(preferences.get("taste") or "smooth").title(),
        "Temperature": str(preferences.get("temperature") or barista.context.temperature_pref).title(),
        "Effort": str(preferences.get("effort") or barista.context.effort_pref).title(),
    }


def _backend_drink_temperature(drink: dict, barista: BaristaBot, preferences: dict | None = None) -> str:
    preferred = str((preferences or {}).get("temperature") or "").lower()
    if preferred in {"hot", "iced", "cold"}:
        return "iced" if preferred == "cold" else preferred
    raw_temperature = drink.get("temperature")
    if isinstance(raw_temperature, list) and raw_temperature:
        return str(raw_temperature[0]).lower()
    if isinstance(raw_temperature, str) and raw_temperature:
        return raw_temperature.lower()
    return barista.context.temperature_pref


def _normalize_backend_chat_result(data: dict, barista: BaristaBot) -> dict:
    preferences = data.get("extractedPreferences") or {}
    normalized = dict(data)
    normalized["preferences"] = _display_preferences(preferences, barista)

    if data.get("mode") == "profile_recommendation" and isinstance(data.get("recommendation"), dict):
        recommendation = data["recommendation"]
        drink = recommendation.get("drink") or {}
        drink_name = str(drink.get("name") or "Unknown")
        composition = drink.get("composition") or {}
        if not composition:
            composition = _composition_for_drink(drink_name, {})
        raw_score = recommendation.get("matchScore")
        if raw_score is None:
            raw_score = float(recommendation.get("score", 0) or 0) / 21 * 100
        normalized["recommendation_card"] = {
            "drink_name": drink_name,
            "match_score": _score_percent(raw_score),
            "explanation": str(recommendation.get("reasoning") or data.get("reply") or "Based on our chat."),
            "composition": composition,
            "temperature": _backend_drink_temperature(drink, barista, preferences),
        }

    return normalized


def _persist_guest_backend_recommendation(latest: dict, barista: BaristaBot, backend_client: CoffeeBackendClient) -> None:
    if getattr(backend_client, "_token", ""):
        return
    if latest.get("mode") != "profile_recommendation" or not latest.get("recommendation_card"):
        return

    card = latest["recommendation_card"]
    context = barista.get_context()
    HistoryTracker().add_recommendation(
        drink_name=str(card.get("drink_name", "Unknown")),
        mood=context.mood,
        time_of_day=context.time_of_day,
        temperature=str(card.get("temperature") or context.temperature_pref),
        location=context.location,
        match_score=int(card.get("match_score", 0)),
        composition=card.get("composition") or {},
    )


def _build_barista_response(
    message: str,
    barista: BaristaBot,
    backend_client: CoffeeBackendClient,
    conversation: list[dict[str, str]],
) -> dict:
    barista.process_user_input(message)

    backend_result = backend_client.chat(message, _history_events_for_backend(), conversation)
    if backend_result:
        latest = _normalize_backend_chat_result(backend_result, barista)
        _persist_guest_backend_recommendation(latest, barista, backend_client)
        return latest

    return _build_local_barista_response(message, barista, backend_client)


def _build_local_barista_response(message: str, barista: BaristaBot, backend_client: CoffeeBackendClient) -> dict:
    mode = _classify_barista_intent(message)
    preferences = _barista_extracted_preferences(message, barista)

    if mode == "knowledge":
        topic = _match_knowledge_topic(message)
        return {"mode": "knowledge", "reply": f"{topic['title']}: {topic['summary']}", "knowledge": topic, "preferences": preferences, "assistantEngine": "local-fallback"}

    if mode == "custom":
        drink = _match_custom_drink(message, preferences)
        return {"mode": "custom", "reply": f"I would suggest {drink['name']}. {drink['description']}", "custom": drink, "guide": _guide_from_custom(drink), "preferences": preferences, "assistantEngine": "local-fallback"}

    if mode == "guide":
        guide = _build_brew_guide(message, barista)
        return {"mode": "guide", "reply": f"Here is a practical home guide for {guide['title']}.", "guide": guide, "preferences": preferences, "assistantEngine": "local-fallback"}

    recommendation = _get_barista_recommendation(barista, backend_client)
    if not recommendation:
        warning = backend_client.last_error or "The backend chat service is unavailable."
        return {"mode": "empty", "reply": f"I could not reach the backend barista yet. {warning}", "preferences": preferences, "assistantEngine": "local-fallback"}
    return {"mode": "recommendation", "reply": f"Based on what you said, I would recommend {recommendation['drink_name']}. {recommendation.get('explanation', '')}", "recommendation": recommendation, "preferences": preferences, "assistantEngine": "local-fallback"}


def _classify_barista_intent(message: str) -> str:
    text = message.lower()
    if any(phrase in text for phrase in ("how do i make", "how to make", "make at home", "recipe", "brew this", "steps", "ingredients", "home guide")):
        return "guide"
    if any(phrase in text for phrase in ("what is", "history", "origin", "explain", "difference between", "compare", " vs", "versus", "teach me", "learn")):
        return "knowledge"
    if any(phrase in text for phrase in ("off menu", "custom", "something new", "surprise me", "outside", "different drink", "specialty", "try in")):
        return "custom"
    return "recommendation"


def _barista_extracted_preferences(message: str, barista: BaristaBot) -> dict:
    text = message.lower()
    context = barista.get_context()
    taste = "smooth"
    if any(word in text for word in ("bitter", "strong", "bold", "intense")):
        taste = "bitter"
    elif any(word in text for word in ("sweet", "dessert", "vanilla", "caramel", "chocolate")):
        taste = "sweet"
    return {
        "Mood": context.mood.title(),
        "Taste": taste.title(),
        "Temperature": context.temperature_pref.title(),
        "Effort": context.effort_pref.title(),
    }


def _match_knowledge_topic(message: str) -> dict:
    text = message.lower()
    scored = []
    for topic in KNOWLEDGE_TOPICS:
        score = sum(1 for keyword in topic["keywords"] if keyword in text)
        if score:
            scored.append((score, topic))
    return sorted(scored, key=lambda item: item[0], reverse=True)[0][1] if scored else KNOWLEDGE_TOPICS[-1]


def _match_custom_drink(message: str, preferences: dict) -> dict:
    text = message.lower()
    for drink in CUSTOM_DRINKS:
        if drink["name"].lower() in text or any(tag in text for tag in drink["tags"]):
            return drink
    return CUSTOM_DRINKS[0] if preferences.get("Temperature") == "Iced" else CUSTOM_DRINKS[2]


def _guide_from_custom(drink: dict) -> dict:
    return {
        "title": drink["name"],
        "equipment": drink["equipment"],
        "ingredients": drink["ingredients"],
        "steps": drink["steps"],
        "tips": drink["tips"],
    }


def _build_brew_guide(message: str, barista: BaristaBot) -> dict:
    profiles = load_coffee_profiles()
    text = message.lower()
    matched_name = next((name for name in profiles if name.lower() in text), None)
    if not matched_name and st.session_state.get("barista_latest", {}).get("recommendation"):
        matched_name = st.session_state["barista_latest"]["recommendation"].get("drink_name")
    if not matched_name:
        matched_name = "Cold Brew" if barista.context.temperature_pref == "iced" else "Latte"

    profile = profiles.get(str(matched_name), {})
    composition = profile.get("composition", {})
    is_iced = str(profile.get("temperature", barista.context.temperature_pref)).lower() in {"iced", "cold"}
    milk = float(composition.get("milk_percent", 0))
    foam = float(composition.get("foam_percent", 0))
    coffee = float(composition.get("coffee_percent", 100))

    equipment = ["coffee brewer or espresso setup", "serving cup"]
    if is_iced:
        equipment.append("glass and ice")
    if milk or foam:
        equipment.append("milk frother or small saucepan")

    ingredients = [f"coffee base, roughly {coffee:.0f}% of the drink"]
    if milk:
        ingredients.append(f"milk, roughly {milk:.0f}%")
    if foam:
        ingredients.append(f"foam finish, roughly {foam:.0f}%")
    if is_iced:
        ingredients.append("ice")

    steps = [
        f"Prepare the coffee base for {matched_name}; keep it concentrated enough to hold flavor.",
        "Taste the base before adding anything else so you know whether it needs dilution or softness.",
        "Build the drink in the cup using the same rough proportions shown in the result card.",
    ]
    if milk:
        steps.append("Add milk slowly and stop when the color and body look balanced.")
    if foam:
        steps.append("Finish with foam last so it stays visible on top.")
    if is_iced:
        steps.append("Serve over fresh ice so the drink stays crisp.")
    steps.append("Adjust sweetness or dilution only after tasting the finished cup.")

    return {
        "title": str(matched_name),
        "equipment": equipment,
        "ingredients": ingredients,
        "steps": steps,
        "tips": (
            "Keep ratio, grind, water temperature, and timing consistent once you like the taste.",
            "If it tastes flat, strengthen the coffee base before adding more sugar.",
        ),
    }


def _render_barista_latest(latest: dict | None, barista: BaristaBot) -> None:
    if not latest:
        st.markdown(
            """
            <aside class="barista-latest-panel empty">
              <span>Latest response</span>
              <h2>Your answer will land here.</h2>
              <p>Ask for a recommendation, a recipe, a coffee explanation, or an off-menu idea.</p>
            </aside>
            """,
            unsafe_allow_html=True,
        )
        return

    mode = latest.get("mode", "recommendation")
    prefs = latest.get("preferences", {})
    pref_html = "".join(f"<div><span>{escape(str(k))}</span><strong>{escape(str(v))}</strong></div>" for k, v in prefs.items())

    if mode in {"recommendation", "profile_recommendation"}:
        recommendation = latest.get("recommendation_card") or latest.get("recommendation", {})
        drink_name = str(recommendation.get("drink_name", "Unknown"))
        match_score = int(recommendation.get("match_score", 0))
        explanation = str(recommendation.get("explanation", "Based on our chat."))
        composition = recommendation.get("composition", {})
        is_iced = str(recommendation.get("temperature") or barista.context.temperature_pref).lower() in {"iced", "cold"}
        cup_html = _composition_cup_html(composition, is_iced) if composition else ""
        if not cup_html:
            cup_html = _cup_html(drink_name)
        engine = str(latest.get("assistantEngine", "backend"))
        st.markdown(
            f"""
            <aside class="barista-latest-panel recommendation">
              <span>Profile recommendation · {escape(engine)}</span>
              <div class="barista-latest-top">
                <h2>{escape(drink_name)}</h2>
                <b>{match_score}% match</b>
              </div>
              <p>{escape(explanation)}</p>
              <div class="barista-latest-cup">{cup_html}</div>
              <div class="barista-pref-grid">{pref_html}</div>
            </aside>
            """,
            unsafe_allow_html=True,
        )
        return

    if mode in {"guide", "custom", "custom_recommendation", "brew_guide"}:
        guide = latest.get("guide", {})
        custom = latest.get("customDrink") or latest.get("custom", {})
        title = str(guide.get("title") or custom.get("name") or "Brew Guide")
        description = str(custom.get("description") or latest.get("reply", ""))
        equipment = ", ".join(str(item) for item in guide.get("equipment", ()))
        ingredients = "".join(f"<li>{escape(str(item))}</li>" for item in guide.get("ingredients", ()))
        steps = "".join(f"<li>{escape(str(item))}</li>" for item in guide.get("steps", ()))
        tips = " ".join(str(item) for item in guide.get("tips", ()))
        kicker = "Off-menu drink" if mode in {"custom", "custom_recommendation"} else "Brew guide"
        st.markdown(
            f"""
            <aside class="barista-latest-panel guide">
              <span>{escape(kicker)}</span>
              <h2>{escape(title)}</h2>
              <p>{escape(description)}</p>
              <div class="barista-guide-block"><strong>Equipment</strong><p>{escape(equipment)}</p></div>
              <div class="barista-guide-block"><strong>Ingredients</strong><ul>{ingredients}</ul></div>
              <div class="barista-guide-block"><strong>Steps</strong><ol>{steps}</ol></div>
              <div class="barista-guide-block"><strong>Tips</strong><p>{escape(tips)}</p></div>
            </aside>
            """,
            unsafe_allow_html=True,
        )
        return

    topic = latest.get("knowledge", {})
    bullets_source = topic.get("bullets") or topic.get("facts") or ()
    bullets = "".join(f"<li>{escape(str(item))}</li>" for item in bullets_source)
    st.markdown(
        f"""
        <aside class="barista-latest-panel knowledge">
          <span>Coffee knowledge</span>
          <h2>{escape(str(topic.get("title", "Coffee Knowledge")))}</h2>
          <p>{escape(str(topic.get("summary", latest.get("reply", ""))))}</p>
          <ul>{bullets}</ul>
          <div class="barista-pref-grid">{pref_html}</div>
        </aside>
        """,
        unsafe_allow_html=True,
    )


def _score_percent(match_score: float | int) -> int:
    """Normalize backend/mock score formats for display and history."""
    score = float(match_score or 0)
    if score <= 1:
        score *= 100
    return round(max(0, min(100, score)))


def _render_profile_composition(drink_name: str, is_iced: bool) -> None:
    profiles = load_coffee_profiles()
    profile = profiles.get(drink_name)
    if not profile:
        st.info("Composition details are not available for this drink yet.")
        return

    composition = profile.get("composition", {})
    common = {
        "caffeine_mg": int(composition.get("caffeine_mg", 0)),
        "sugar_g": float(composition.get("sugar_g", 0)),
        "foam_percent": float(composition.get("foam_percent", 0)),
        "milk_percent": float(composition.get("milk_percent", 0)),
        "coffee_percent": float(composition.get("coffee_percent", 100)),
    }
    if is_iced:
        render_cold_glass(**common, ice_percent=float(composition.get("ice_percent", 30)))
    else:
        render_hot_cup(**common)


def _composition_for_drink(drink_name: str, recommendation: dict) -> dict:
    composition = recommendation.get("composition") or {}
    if composition:
        return composition
    profile = load_coffee_profiles().get(drink_name, {})
    return profile.get("composition", {})


def _render_barista_recommendation(result: dict, barista: BaristaBot) -> None:
    drink_name = str(result.get("drink_name", "Unknown"))
    match_score = int(result.get("match_score", 0))
    explanation = str(result.get("explanation", "Based on our chat."))
    warning = result.get("warning")
    composition = result.get("composition", {})
    is_iced = barista.context.temperature_pref == "iced"
    cup_html = _composition_cup_html(composition, is_iced) if composition else ""
    if not cup_html:
        cup_html = _cup_html(drink_name)
    concerns = ", ".join(barista.context.concerns) if barista.context.concerns else "None mentioned"

    st.markdown(
        f"""
        <section class="barista-result-card">
          <div class="barista-result-copy">
            <span class="barista-panel-kicker">Recommended brew</span>
            <h2>{escape(drink_name)}</h2>
            <p>{escape(explanation)}</p>
            {"<div class='barista-warning'>" + escape(str(warning)) + "</div>" if warning else ""}
            <div class="barista-why-grid">
              <div><span>Mood</span><strong>{escape(barista.context.mood.title())}</strong></div>
              <div><span>Setting</span><strong>{escape(barista.context.temperature_pref.title())} · {escape(barista.context.location.title())}</strong></div>
              <div><span>Effort</span><strong>{escape(barista.context.effort_pref.title())}</strong></div>
              <div><span>Concerns</span><strong>{escape(concerns.title())}</strong></div>
            </div>
          </div>
          <div class="barista-result-visual">
            <div class="barista-score">{match_score}%<span>match</span></div>
            {cup_html}
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _get_barista_recommendation(barista: BaristaBot, backend_client: CoffeeBackendClient):
    """Generate recommendation based on barista conversation."""
    payload = barista.get_recommendation_payload()
    history_tracker = HistoryTracker()

    try:
        recommendation = backend_client.get_recommendation(payload)
        drink_name = recommendation.get("recommended_drink", "Unknown")
        match_score = _score_percent(recommendation.get("match_score", 0))
        explanation = recommendation.get("explanation", "Based on our chat.")
        warning = recommendation.get("warning")
        composition = _composition_for_drink(str(drink_name), recommendation)

        history_tracker.add_recommendation(
            drink_name=drink_name,
            mood=barista.context.mood,
            time_of_day=payload.get("time_of_day", "afternoon"),
            temperature=barista.context.temperature_pref,
            location=barista.context.location,
            match_score=match_score,
            composition=composition,
        )

        return {
            "drink_name": drink_name,
            "match_score": match_score,
            "explanation": explanation,
            "warning": warning,
            "composition": composition,
        }

    except Exception as e:
        st.error(f"Error getting recommendation: {e}")
        return None
