import streamlit as st
from html import escape
from urllib.parse import quote

from barista_bot import BaristaBot
from backend_client import CoffeeBackendClient
from history import HistoryTracker
from recommendation_engine import _composition_cup_html, _cup_html
from visualization import load_coffee_profiles, render_hot_cup, render_cold_glass


def render_barista_bot_page(client: CoffeeBackendClient | None = None):
    """Render the Barista Bot conversational interface."""
    if st.query_params.get("barista_action", "") == "reset":
        for key in (
            "barista_bot",
            "barista_bot_started",
            "barista_bot_messages",
            "barista_last_recommendation",
        ):
            st.session_state.pop(key, None)
        st.query_params.clear()
        st.rerun()

    prompt_examples = [
        "I'm tired but want smooth",
        "Quick iced coffee",
        "Low caffeine, not bitter",
    ]
    prompt_links = "".join(
        f'<a href="?barista_prompt={quote(prompt)}"><span>Try</span>{escape(prompt)}</a>'
        for prompt in prompt_examples
    )

    st.markdown(
        f"""
        <section class="barista-desk-hero">
          <div class="bdh-copy">
            <span>Barista Bot</span>
            <h1>Find a coffee that fits today.</h1>
            <p>Tell me your mood, taste, and time. I'll suggest one drink.</p>
          </div>
        </section>
        <section class="barista-desk-prompts">
          <div>
            <span>Quick starts</span>
            <strong>Use one, then refine it in chat.</strong>
          </div>
          <nav>{prompt_links}</nav>
        </section>
        """,
        unsafe_allow_html=True,
    )

    if "barista_bot" not in st.session_state:
        st.session_state.barista_bot = BaristaBot()
        st.session_state.barista_bot_started = False
        st.session_state.barista_bot_messages = []

    barista = st.session_state.barista_bot

    if not st.session_state.barista_bot_started:
        greeting = barista.start_conversation()
        st.session_state.barista_bot_messages.append({"role": "barista", "content": greeting})
        st.session_state.barista_bot_started = True
        st.rerun()

    quick_prompt = st.query_params.get("barista_prompt", "")
    if quick_prompt:
        st.session_state.barista_bot_messages.append({"role": "user", "content": quick_prompt})
        response = barista.process_user_input(quick_prompt)
        st.session_state.barista_bot_messages.append({"role": "barista", "content": response})
        st.query_params.clear()
        st.rerun()

    context = barista.get_context()
    concerns = ", ".join(context.concerns) if context.concerns else "None yet"

    brief_col, chat_col, decision_col = st.columns([0.72, 1.18, 0.78], gap="large")

    with brief_col:
        st.markdown(
            f"""
            <aside class="barista-ticket-panel">
              <span class="btp-kicker">Tasting brief</span>
              <h2>Current read</h2>
              <div class="btp-list">
                <div><span>01 Mood</span><strong>{escape(context.mood.title())}</strong></div>
                <div><span>02 Temperature</span><strong>{escape(context.temperature_pref.title())}</strong></div>
                <div><span>03 Setting</span><strong>{escape(context.location.title())}</strong></div>
                <div><span>04 Effort</span><strong>{escape(context.effort_pref.title())}</strong></div>
              </div>
              <div class="btp-note">
                <span>Avoid or consider</span>
                <p>{escape(concerns)}</p>
              </div>
            </aside>
            """,
            unsafe_allow_html=True,
        )

    with chat_col:
        st.markdown(
            """
            <section class="barista-transcript-panel">
              <header>
                <div>
                  <span>Transcript</span>
                  <strong>Tell the bot what should be true about the cup.</strong>
                </div>
                <a href="?barista_action=reset">Clear ticket</a>
              </header>
              <div class="barista-transcript-scroll">
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
                <div class="barista-transcript-row {role}" style="animation-delay:{delay:.2f}s">
                  <div>
                    <span>{label}</span>
                    <p>{escape(message["content"])}</p>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div></section>", unsafe_allow_html=True)

        st.markdown('<div class="barista-desk-input">', unsafe_allow_html=True)
        input_col, send_col = st.columns([0.82, 0.18], gap="small")
        with input_col:
            user_input = st.text_input(
                "Message",
                placeholder="e.g. I'm tired, want something smooth and quick...",
                label_visibility="collapsed",
                key="barista_input",
            )
        with send_col:
            send_button = st.button("Send", use_container_width=True, key="barista_send")
        st.markdown("</div>", unsafe_allow_html=True)

        if send_button and user_input.strip():
            st.session_state.barista_bot_messages.append({"role": "user", "content": user_input})
            response = barista.process_user_input(user_input)
            st.session_state.barista_bot_messages.append({"role": "barista", "content": response})
            st.session_state.pop("barista_last_recommendation", None)
            st.rerun()

    with decision_col:
        st.markdown(
            """
            <aside class="barista-decision-panel">
              <span class="btp-kicker">Decision</span>
              <h2>Ready when the brief feels right.</h2>
              <p>Generate after the transcript has enough detail. The recommendation is saved to history so profile insights can learn from it.</p>
              <div class="bdp-checks">
                <div><span>Captured</span><strong>Mood and timing</strong></div>
                <div><span>Captured</span><strong>Setting and effort</strong></div>
                <div><span>Optional</span><strong>Concerns or limits</strong></div>
              </div>
            </aside>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Get My Perfect Brew", use_container_width=True, type="primary", key="barista_brew"):
            st.session_state.barista_last_recommendation = _get_barista_recommendation(
                barista,
                client or CoffeeBackendClient(use_mock=True),
            )
            st.rerun()

    if st.session_state.get("barista_last_recommendation"):
        _render_barista_recommendation(st.session_state["barista_last_recommendation"], barista)


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
