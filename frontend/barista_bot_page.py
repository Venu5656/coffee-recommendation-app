import streamlit as st
from html import escape

from barista_bot import BaristaBot
from backend_client import CoffeeBackendClient
from history import HistoryTracker
from images import HOME_BREW_ICON
from visualization import load_coffee_profiles, render_hot_cup, render_cold_glass


def render_barista_bot_page(client: CoffeeBackendClient | None = None):
    """Render the Barista Bot conversational interface."""

    st.markdown(
        """
        <section class="barista-hero">
          <div class="barista-hero-left">
            <span class="barista-hero-kicker">Conversational brew finder</span>
            <h1>Talk it out.<br><em>Find the cup.</em></h1>
            <div class="barista-hero-rule"></div>
            <p>Tell the bot what kind of day you are having. It listens for mood, temperature, effort, and concerns, then turns the chat into one clear recommendation.</p>
            <div class="barista-hero-prompts">
              <span>I'm tired but want smooth</span>
              <span>Quick iced coffee</span>
              <span>Low caffeine, not bitter</span>
            </div>
          </div>
          <div class="barista-hero-right">
            <div class="barista-cup-art">
              <div class="bca-steam">
                <div class="bca-s bca-s1"></div>
                <div class="bca-s bca-s2"></div>
                <div class="bca-s bca-s3"></div>
              </div>
              <div class="bca-cup">
                <div class="bca-liquid"></div>
                <div class="bca-handle"></div>
              </div>
              <div class="bca-saucer"></div>
            </div>
          </div>
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

    chat_col, profile_col = st.columns([1.35, 0.85], gap="large")

    with chat_col:
        st.markdown(
            """
            <div class="barista-chat-panel">
              <div class="barista-chat-heading">
                <span class="barista-panel-kicker">Live conversation</span>
                <strong>Ask like you would at the counter.</strong>
              </div>
              <div class="barista-chat-scroll">
            """,
            unsafe_allow_html=True,
        )

        total = len(st.session_state.barista_bot_messages)
        for i, message in enumerate(st.session_state.barista_bot_messages):
            role = "user" if message["role"] == "user" else "barista"
            label = "You" if role == "user" else "Barista"
            # Stagger older messages slightly so new ones feel like they arrive last
            delay = max(0.0, (total - 1 - i) * 0.055)
            st.markdown(
                f"""
                <div class="barista-message-row {role}" style="animation-delay:{delay:.2f}s">
                  <div class="barista-message">
                    <span class="msg-label">{label}</span>
                    <p>{escape(message["content"])}</p>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("</div></div>", unsafe_allow_html=True)

        st.markdown('<div class="barista-input-wrap">', unsafe_allow_html=True)
        input_col, send_col = st.columns([0.82, 0.18], gap="small")
        with input_col:
            user_input = st.text_input(
                "Message",
                placeholder="e.g. I'm tired, want something smooth and quick…",
                label_visibility="collapsed",
                key="barista_input",
            )
        with send_col:
            send_button = st.button("Send →", use_container_width=True, key="barista_send")
        st.markdown("</div>", unsafe_allow_html=True)

        if send_button and user_input.strip():
            st.session_state.barista_bot_messages.append({"role": "user", "content": user_input})
            response = barista.process_user_input(user_input)
            st.session_state.barista_bot_messages.append({"role": "barista", "content": response})
            st.rerun()

    with profile_col:
        context = barista.get_context()
        concerns = ", ".join(context.concerns) if context.concerns else "—"

        mood_icon = {"stressed": "😤", "tired": "😴", "energetic": "⚡", "relaxed": "😌", "focused": "🎯"}.get(context.mood, "💭")
        temp_icon = "❄️" if context.temperature_pref == "iced" else "🔥"
        loc_icon = (
            f'<img src="{HOME_BREW_ICON}" class="bpg-img-icon" alt="home brew"/>'
            if context.location == "home"
            else "☕"
        )
        effort_icon = {"minimal": "⚡", "moderate": "🔸", "hands-on": "🤲"}.get(context.effort_pref, "🔸")

        st.markdown(
            f"""
            <aside class="barista-profile-panel">
              <div class="barista-panel-kicker">Live profile</div>
              <h2>What the bot has learned</h2>
              <div class="barista-profile-grid">
                <div class="bpg-tile">
                  <span class="bpg-icon">{mood_icon}</span>
                  <span class="bpg-label">Mood</span>
                  <strong>{escape(context.mood.title())}</strong>
                </div>
                <div class="bpg-tile">
                  <span class="bpg-icon">{temp_icon}</span>
                  <span class="bpg-label">Temp</span>
                  <strong>{escape(context.temperature_pref.title())}</strong>
                </div>
                <div class="bpg-tile">
                  <span class="bpg-icon">{loc_icon}</span>
                  <span class="bpg-label">Location</span>
                  <strong>{escape(context.location.title())}</strong>
                </div>
                <div class="bpg-tile">
                  <span class="bpg-icon">{effort_icon}</span>
                  <span class="bpg-label">Effort</span>
                  <strong>{escape(context.effort_pref.title())}</strong>
                </div>
              </div>
              <div class="barista-concern-box">
                <span class="bpg-label">Concerns noted</span>
                <p>{escape(concerns)}</p>
              </div>
              <p class="barista-profile-note">This updates as the conversation gets more specific.</p>
            </aside>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Get My Perfect Brew", use_container_width=True, type="primary", key="barista_brew"):
            _get_barista_recommendation(barista, client or CoffeeBackendClient(use_mock=True))


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

        history_tracker.add_recommendation(
            drink_name=drink_name,
            mood=barista.context.mood,
            time_of_day=payload.get("time_of_day", "afternoon"),
            temperature=barista.context.temperature_pref,
            location=barista.context.location,
            match_score=match_score,
        )

        st.markdown(
            f"""
            <section class="barista-result-panel">
              <div class="barista-result-copy">
                <span class="barista-panel-kicker">Recommended brew</span>
                <h2>{escape(drink_name)}</h2>
                <p>{escape(explanation)}</p>
                {"<div class='barista-warning'>" + escape(str(warning)) + "</div>" if warning else ""}
              </div>
              <div class="barista-score">{match_score}% match</div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        viz_col, why_col = st.columns([0.5, 0.5], gap="large")
        with viz_col:
            _render_profile_composition(
                drink_name,
                is_iced=barista.context.temperature_pref == "iced",
            )
        with why_col:
            st.markdown(
                f"""
                <div class="barista-why-panel">
                  <span class="barista-panel-kicker">Why this works</span>
                  <p><strong>Mood:</strong> {escape(barista.context.mood.title())}</p>
                  <p><strong>Taste direction:</strong> {escape(payload.get('taste_preference', 'balanced'))}</p>
                  <p><strong>Concerns:</strong> {escape(', '.join(barista.context.concerns) if barista.context.concerns else 'None mentioned')}</p>
                  <p><strong>Setting:</strong> {escape(barista.context.temperature_pref.title())} at {escape(barista.context.location.title())}</p>
                  <p><strong>Caffeine:</strong> {escape(payload.get('caffeine_preference', 'medium'))}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

    except Exception as e:
        st.error(f"Error getting recommendation: {e}")
