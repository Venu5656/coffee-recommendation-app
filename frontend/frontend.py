import base64
from collections import Counter
from datetime import datetime
from html import escape
from pathlib import Path
from textwrap import dedent

import streamlit as st

from backend_client import CoffeeBackendClient
from barista_bot_page import render_barista_bot_page
from dashboard import render_dashboard_page
from insights import render_insights_page
from recommendation_engine import _composition_cup_html, _cup_html, render_recommendation_page
from history import HistoryTracker
from theme import CUSTOM_CSS
from visualization import load_coffee_profiles


st.set_page_config(
    page_title="Coffee Companion",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = "home"

# Handle HTML pill-button navigation via query param
_pill_nav = st.query_params.get("pill_nav", "")
if _pill_nav:
    st.session_state.page = _pill_nav
    st.query_params.clear()

# Keep recommendation routing stable when recommendation query params are present.
# This prevents mode cards and preference chips from falling back to the home page.
if (
    st.query_params.get("brew_mode", "")
    or st.query_params.get("rec_step", "")
    or any(k.startswith("set_") for k in st.query_params)
):
    st.session_state.page = "recommend"

if st.query_params.get("profile_view", ""):
    st.session_state.page = "profile"

if st.query_params.get("barista_prompt", "") or st.query_params.get("barista_action", ""):
    st.session_state.page = "barista"


def _img_b64(filename: str) -> str:
    candidates = [
        Path(__file__).parent.parent / "images" / filename,
    ]
    path = next((candidate for candidate in candidates if candidate.exists()), None)
    if path is None:
        return ""
    return base64.b64encode(path.read_bytes()).decode()


def _img_data_uri(filename: str) -> str:
    candidates = [
        Path(__file__).parent.parent / "images" / filename,
    ]
    path = next((candidate for candidate in candidates if candidate.exists()), None)
    if path is None:
        return ""

    data = path.read_bytes()
    if data.startswith(b"RIFF") and data[8:12] == b"WEBP":
        mime = "image/webp"
    elif data.startswith(b"\x89PNG"):
        mime = "image/png"
    elif data.startswith(b"\xff\xd8"):
        mime = "image/jpeg"
    else:
        mime = "image/png"

    return f"data:{mime};base64,{base64.b64encode(data).decode()}"


# ── Backend client — probe once per server lifetime, cache result ─────────────
@st.cache_resource
def _check_backend() -> bool:
    return CoffeeBackendClient().health_check()


@st.cache_resource
def _auth_cache() -> dict[str, object]:
    return {}


_backend_live = _check_backend()
client = CoffeeBackendClient(use_mock=not _backend_live)

_cached_auth = _auth_cache()
if not st.session_state.get("is_authenticated") and _cached_auth.get("token"):
    st.session_state["is_authenticated"] = True
    st.session_state["auth_user"] = _cached_auth.get("user", {})
    st.session_state["auth_token"] = str(_cached_auth.get("token", ""))
    st.session_state["display_name"] = str(_cached_auth.get("display_name", ""))

if st.session_state.get("auth_token"):
    client._token = st.session_state["auth_token"]


def _set_logged_in_user(user: dict[str, str], token: str = "") -> None:
    st.session_state["is_authenticated"] = True
    st.session_state["auth_user"] = user
    st.session_state["auth_token"] = token
    st.session_state["display_name"] = user.get("name", "")
    _auth_cache().update(
        {
            "user": user,
            "token": token,
            "display_name": user.get("name", ""),
        }
    )
    st.session_state.page = "home"


def _logout_user() -> None:
    client.logout()
    _auth_cache().clear()
    for _key in ("is_authenticated", "auth_user", "auth_token"):
        st.session_state.pop(_key, None)
    st.session_state.page = "home"


if st.query_params.get("profile_action", "") == "logout":
    st.query_params.clear()
    _logout_user()
    st.rerun()


def _login_bg_url(filename: str) -> str:
    path = next(
        (
            p
            for p in [
                Path(__file__).parent.parent / "images" / filename,
            ]
            if p.exists()
        ),
        None,
    )
    if not path:
        return ""
    ext = path.suffix.lstrip(".").lower()
    mime = {"avif": "image/avif", "jpg": "image/jpeg", "jpeg": "image/jpeg",
            "png": "image/png", "webp": "image/webp"}.get(ext, "image/png")
    b64 = base64.b64encode(path.read_bytes()).decode()
    return f"url('data:{mime};base64,{b64}')"


def _render_login_page(auth_client: CoffeeBackendClient, backend_live: bool) -> None:
    beans_url = _login_bg_url("login_bg.jpg")
    if beans_url:
        st.markdown(
            f"<style>:root{{--login-bg:{beans_url};}}</style>",
            unsafe_allow_html=True,
        )
    logo_src = _img_data_uri("coffee_logo.png") or _img_data_uri("coffe_logo.png")
    logo_markup = (
        f'<img src="{logo_src}" class="login-logo-img" alt="Coffee Companion logo"/>'
        if logo_src
        else '<div class="login-logo-mark">C</div>'
    )
    st.markdown(
        f"""
        <section class="login-page">
          <div class="login-brand">
            {logo_markup}
            <span>Coffee Companion</span>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    _, form_col, _ = st.columns([0.32, 1.9, 0.32], gap="large")
    with form_col:
        st.markdown('<div id="login-form-marker"></div>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="login-form-heading">
              <h2>Log in</h2>
              <p>{'Your tasting notes are ready. Pick up where your last cup left off.' if backend_live else 'Demo tasting room open. Use any email and password to step inside.'}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        login_tab, register_tab = st.tabs(["Login", "Create account"])
        with login_tab:
            with st.form("login_form", clear_on_submit=False):
                email = st.text_input("Email", placeholder="you@example.com", key="login_email")
                password = st.text_input("Password", type="password", key="login_password")
                submitted = st.form_submit_button("Login", use_container_width=True)

            if submitted:
                if not email.strip() or not password.strip():
                    st.error("Enter your email and password.")
                elif backend_live:
                    data = auth_client.login(email.strip(), password)
                    if data and data.get("token"):
                        user = data.get("user") or {"name": email.split("@")[0], "email": email.strip()}
                        _set_logged_in_user(user, data.get("token", ""))
                        st.rerun()
                    else:
                        st.error(auth_client.last_error or "Could not log in with those credentials.")
                else:
                    _set_logged_in_user({"name": email.split("@")[0], "email": email.strip()}, "demo-token")
                    st.rerun()

        with register_tab:
            with st.form("register_form", clear_on_submit=False):
                name = st.text_input("Name", placeholder="Alex", key="register_name")
                new_email = st.text_input("Email", placeholder="you@example.com", key="register_email")
                new_password = st.text_input("Password", type="password", key="register_password")
                created = st.form_submit_button("Create account", use_container_width=True)

            if created:
                if not name.strip() or not new_email.strip() or len(new_password) < 8:
                    st.error("Add a name, email, and password with at least 8 characters.")
                elif backend_live:
                    data = auth_client.register(name.strip(), new_email.strip(), new_password)
                    if data and data.get("token"):
                        user = data.get("user") or {"name": name.strip(), "email": new_email.strip()}
                        _set_logged_in_user(user, data.get("token", ""))
                        st.rerun()
                    else:
                        st.error(auth_client.last_error or "Could not create that account.")
                else:
                    _set_logged_in_user({"name": name.strip(), "email": new_email.strip()}, "demo-token")
                    st.rerun()


def _format_dashboard_label(value: object, fallback: str = "Still learning") -> str:
    text = str(value or "").strip()
    return text.replace("-", " ").title() if text else fallback


def _profile_for_dashboard_drink(drink_name: str, profiles: dict[str, dict]) -> dict:
    if drink_name in profiles:
        return profiles[drink_name]

    simplified = str(drink_name).replace("(DIY)", "").strip()
    if simplified in profiles:
        return profiles[simplified]

    simplified_lower = simplified.lower()
    for name, profile in profiles.items():
        if name.lower() == simplified_lower:
            return profile
    return {}


def _build_streamlit_dashboard(tracker: HistoryTracker, user_name: str) -> dict[str, object]:
    recs = tracker.get_all()
    profiles = load_coffee_profiles()
    total = len(recs)

    if not total:
        return {
            "has_data": False,
            "archetype": "New Coffee Explorer",
            "headline": "Start with a recommendation or barista chat, then this dashboard will turn your coffee history into a taste profile.",
            "user_name": user_name,
            "stats": tracker.get_stats(),
            "taste": {},
            "personality": {
                "favorite_style": "Unknown",
                "signature_time": "Unknown",
                "top_drink": "None yet",
                "brews_logged": 0,
            },
            "exploration": {"label": "Unmapped", "share": 0, "familiar": 100},
            "top_drinks": [],
            "time_drink_groups": {},
            "mood_drink_groups": {},
            "habit_notes": [
                "Your dashboard becomes more personal after a few saved recommendations.",
                "Use moods, match scores, and repeat sessions to reveal your strongest coffee patterns.",
            ],
        }

    drinks = [rec.drink_name for rec in recs]
    moods = [rec.mood for rec in recs if rec.mood]
    times = [rec.time_of_day for rec in recs if rec.time_of_day]
    locations = [rec.location for rec in recs if rec.location]
    temps = [rec.temperature for rec in recs if rec.temperature]
    scores = [int(rec.match_score or 0) for rec in recs]
    profile_rows = [_profile_for_dashboard_drink(name, profiles) for name in drinks]
    profile_rows = [profile for profile in profile_rows if profile]
    tastes = [taste for profile in profile_rows for taste in profile.get("taste", [])]
    caffeine = [profile.get("caffeine") for profile in profile_rows if profile.get("caffeine")]
    effort = [profile.get("effort") for profile in profile_rows if profile.get("effort")]

    top_counts = Counter(drinks).most_common(5)
    favorite_drink = top_counts[0][0] if top_counts else "None yet"
    favorite_mood = Counter(moods).most_common(1)[0][0] if moods else "varied"
    signature_time = Counter(times).most_common(1)[0][0] if times else "afternoon"
    dominant_taste = Counter(tastes).most_common(1)[0][0] if tastes else "balanced"
    preferred_caffeine = Counter(caffeine).most_common(1)[0][0] if caffeine else "medium"
    preferred_effort = Counter(effort).most_common(1)[0][0] if effort else "moderate"
    preferred_location = Counter(locations).most_common(1)[0][0] if locations else "cafe"
    preferred_temp = Counter(temps).most_common(1)[0][0] if temps else "hot"
    avg_score = round(sum(scores) / len(scores)) if scores else 0
    unique_share = round(len(set(drinks)) / total * 100)
    familiar_share = 100 - unique_share

    if unique_share >= 70:
        exploration_label = "Curious Coffee Wanderer"
    elif unique_share >= 40:
        exploration_label = "Balanced Explorer"
    else:
        exploration_label = "Comfort Driven Regular"

    if dominant_taste in {"bold", "intense", "classic"}:
        archetype = "Focused Minimalist"
        favorite_style = "straight"
    elif preferred_temp == "iced":
        archetype = "Cool Routine Optimizer"
        favorite_style = "refreshing"
    elif dominant_taste in {"sweet", "chocolatey", "rich"}:
        archetype = "Treat Led Sipper"
        favorite_style = "indulgent"
    elif preferred_location == "home":
        archetype = "Home Brew Loyalist"
        favorite_style = "home brewed"
    else:
        archetype = exploration_label
        favorite_style = "balanced"

    def drink_visual(name: str, count: int) -> dict[str, object]:
        rec = next((item for item in reversed(recs) if item.drink_name == name), None)
        profile = _profile_for_dashboard_drink(name, profiles)
        composition = getattr(rec, "composition", {}) if rec else {}
        if not composition:
            composition = profile.get("composition", {})
        temperature = getattr(rec, "temperature", "") if rec else ""
        if not temperature:
            temperature = profile.get("temperature", "")
        return {
            "name": name,
            "count": count,
            "composition": composition,
            "is_iced": str(temperature).lower() in {"iced", "cold"},
        }

    def drink_summaries(counts: list[tuple[str, int]]) -> list[dict[str, object]]:
        return [drink_visual(name, count) for name, count in counts]

    def leaders_for(key: str, value: str) -> list[dict[str, object]]:
        counts = Counter(getattr(rec, "drink_name") for rec in recs if getattr(rec, key) == value).most_common(3)
        return drink_summaries(counts)

    _all_times = ["morning", "afternoon", "night", "evening"]
    time_drink_groups = {
        t: leaders_for("time_of_day", t)
        for t in _all_times
        if any(getattr(rec, "time_of_day", None) == t for rec in recs)
    }
    mood_drink_groups = {
        m: leaders_for("mood", m)
        for m in sorted(set(moods))
        if m
    }

    return {
        "has_data": True,
        "archetype": archetype,
        "user_name": user_name,
        "headline": f"{user_name} tends to favor {_format_dashboard_label(favorite_style).lower()}, {_format_dashboard_label(preferred_caffeine).lower()} caffeine drinks, usually around {signature_time}.",
        "stats": tracker.get_stats(),
        "taste": {
            "Caffeine band": preferred_caffeine,
            "Sweetness tolerance": "sweet" if dominant_taste in {"sweet", "chocolatey", "rich"} else "lightly sweet",
            "Texture": "creamy" if dominant_taste in {"creamy", "smooth", "mild", "sweet", "chocolatey"} else "clean",
            "Drink style": favorite_style,
            "Flavor direction": dominant_taste,
            "Signature time": signature_time,
        },
        "personality": {
            "favorite_style": favorite_style,
            "signature_time": signature_time,
            "top_drink": favorite_drink,
            "brews_logged": total,
        },
        "exploration": {"label": exploration_label, "share": unique_share, "familiar": familiar_share},
        "top_drinks": drink_summaries(top_counts),
        "time_drink_groups": time_drink_groups,
        "mood_drink_groups": mood_drink_groups,
        "habit_notes": [
            f"Your coffee rhythm is strongest in the {signature_time}, where {favorite_drink} shows up most often.",
            f"Your taste profile leans {_format_dashboard_label(favorite_style).lower()} and {_format_dashboard_label(dominant_taste).lower()}, which points to a {archetype.lower()} personality.",
            f"You have explored {len(set(drinks))} unique drinks across {total} saved recommendations.",
            f"Your average match score is {avg_score}%, which means the recommender is finding a consistent lane.",
        ],
    }


def _render_dashboard_preview(dashboard: dict[str, object]) -> None:
    stats = dashboard.get("stats", {})
    exploration = dashboard.get("exploration", {})
    st.markdown(
        f"""
        <section class="home-dashboard-preview">
          <div class="hdp-copy">
            <span class="hdp-kicker">New dashboard</span>
            <h2>{escape(str(dashboard.get("archetype", "Coffee Passport")))}</h2>
            <p>{escape(str(dashboard.get("headline", "")))}</p>
          </div>
          <div class="hdp-metrics">
            <div><span>Total brews</span><strong>{escape(str(stats.get("total_drinks", 0)))}</strong></div>
            <div><span>Top drink</span><strong>{escape(str(stats.get("favorite_drink", "None yet")))}</strong></div>
            <div><span>Explorer score</span><strong>{escape(str(exploration.get("share", 0)))}%</strong></div>
          </div>
          <a class="hdp-link" href="?pill_nav=profile">Open profile dashboard</a>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _render_profile_dashboard(dashboard: dict[str, object]) -> None:
    personality = dashboard.get("personality", {})
    exploration = dashboard.get("exploration", {})
    taste = dashboard.get("taste", {})
    top_drinks = dashboard.get("top_drinks", [])
    habit_notes = dashboard.get("habit_notes", [])
    time_drink_groups: dict = dashboard.get("time_drink_groups", {})
    mood_drink_groups: dict = dashboard.get("mood_drink_groups", {})

    def _tile(item: dict) -> str:
        name = str(item.get("name", "Unknown"))
        count = int(item.get("count", 0))
        cup = (
            _composition_cup_html(item.get("composition", {}), bool(item.get("is_iced")), compact=True)
            or _cup_html(name)
        )
        unit = "strong match" if count == 1 else "strong matches"
        return (
            f'<article class="pp-drink-tile">'
            f'<div class="pp-cup-stage">{cup}</div>'
            f'<strong>{escape(name)}</strong>'
            f'<p>{count} {unit}</p>'
            f'</article>'
        )

    def _drink_grid_html(drinks: list, limit: int = 3, compact: bool = False) -> str:
        items = list(drinks or [])[:limit]
        if not items:
            return (
                "<p class='pp-empty-note'>"
                "No drinks logged for this filter yet.</p>"
            )
        cls = "pp-drink-grid compact" if compact else "pp-drink-grid"
        return f'<div class="{cls}">' + "".join(_tile(item) for item in items) + "</div>"

    # ── Section 1: Hero ───────────────────────────────────────────────────────
    archetype    = escape(str(dashboard.get("archetype", "New Coffee Explorer")))
    headline     = escape(str(dashboard.get("headline", "")))
    expl_label   = escape(str(exploration.get("label", "Unmapped")))
    user_name_d  = escape(str(dashboard.get("user_name", "Guest")))

    st.markdown(
        f"""
        <div class="pp-dashboard">
        <div class="pp-hero-card">
          <div class="pp-hero-copy">
            <span class="hdp-kicker">Taste Profile</span>
            <h1>{archetype}</h1>
            <p>{headline}</p>
          </div>
          <div class="pp-badge">
            <span class="pp-badge-label">Personality type</span>
            <strong>{expl_label}</strong>
            <em>{user_name_d}</em>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Section 2: 4-stat cards ───────────────────────────────────────────────
    fav_style  = escape(_format_dashboard_label(personality.get("favorite_style", "")))
    sig_time   = escape(_format_dashboard_label(personality.get("signature_time", "")))
    top_drink  = escape(str(personality.get("top_drink", "None yet")))
    brews      = escape(str(personality.get("brews_logged", 0)))

    st.markdown(
        f"""
        <div class="pp-stat-row">
          <div class="pp-stat-card">
            <span class="pp-sc-label">Favorite Style</span>
            <strong>{fav_style}</strong>
            <p>Most repeated profile in your stored coffee history.</p>
          </div>
          <div class="pp-stat-card">
            <span class="pp-sc-label">Signature Time</span>
            <strong>{sig_time}</strong>
            <p>Your recommendations cluster most strongly around this part of the day.</p>
          </div>
          <div class="pp-stat-card">
            <span class="pp-sc-label">Top Drink</span>
            <strong>{top_drink}</strong>
            <p>The drink your account returns to most often.</p>
          </div>
          <div class="pp-stat-card">
            <span class="pp-sc-label">Brews Logged</span>
            <strong>{brews}</strong>
            <p>Saved reactions used to refine future suggestions.</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Section 3: Taste Profile + Exploration Score ──────────────────────────
    taste_tags = "".join(
        f'<div class="pp-taste-tag"><span>{escape(str(lbl))}</span>'
        f'<strong>{escape(_format_dashboard_label(val))}</strong></div>'
        for lbl, val in taste.items()
    ) or "<p style='color:rgba(24,14,8,0.38);font-size:0.85rem;'>Complete a recommendation to build your taste profile.</p>"

    share   = escape(str(exploration.get("share", 0)))
    familiar = escape(str(exploration.get("familiar", 100)))

    st.markdown(
        f"""
        <div class="pp-grid-2">
          <div class="pp-section-card">
            <span class="pp-sc-kicker">Taste Profile</span>
            <h2>Your coffee identity at a glance</h2>
            <div class="pp-taste-row">{taste_tags}</div>
          </div>
          <div class="pp-section-card">
            <span class="pp-sc-kicker">Exploration Score</span>
            <h2>How far you step outside your comfort zone</h2>
            <div class="pp-exploration-bar"><span style="width:{share}%"></span></div>
            <div class="pp-expl-metrics">
              <div class="pp-expl-metric"><span>Explorer type</span><strong>{expl_label}</strong></div>
              <div class="pp-expl-metric"><span>Familiar picks</span><strong>{familiar}%</strong></div>
              <div class="pp-expl-metric"><span>Exploration picks</span><strong>{share}%</strong></div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Section 4: Drinking Rhythm + Mood Match ───────────────────────────────
    avail_times = [t for t in ["morning", "afternoon", "night", "evening"] if t in time_drink_groups]
    active_time = avail_times[0] if avail_times else ""
    time_chips = "".join(
        f'<span class="{"active" if t == active_time else ""}">{escape(_format_dashboard_label(t))}</span>'
        for t in (avail_times or ["morning", "afternoon", "night"])
    )
    time_grid = _drink_grid_html(time_drink_groups.get(active_time, []), limit=3)

    avail_moods = sorted(mood_drink_groups.keys())
    active_mood = avail_moods[0] if avail_moods else ""
    mood_chips = "".join(
        f'<span class="{"active" if m == active_mood else ""}">{escape(_format_dashboard_label(m))}</span>'
        for m in (avail_moods or ["tired", "relaxed", "energetic"])
    )
    mood_grid = _drink_grid_html(mood_drink_groups.get(active_mood, []), limit=3)

    insight_labels = ["Rhythm", "Taste Lean", "Range", "Match Strength"]
    pattern_items = "".join(
        f'<div class="pp-pattern-item">'
        f'<span class="pp-pi-index">{i + 1:02d}</span>'
        f'<div><span class="pp-pi-kicker">{escape(insight_labels[i] if i < len(insight_labels) else "Signal")}</span>'
        f'<p>{escape(str(note))}</p></div></div>'
        for i, note in enumerate(habit_notes)
    ) or (
        '<div class="pp-pattern-item">'
        '<span class="pp-pi-index">01</span>'
        '<div><span class="pp-pi-kicker">First Signal</span>'
        '<p>Log a few recommendations to reveal your habits.</p></div></div>'
    )
    insight_summary = escape(
        f"{top_drink} is your current anchor, with {sig_time.lower()} as your strongest coffee moment."
    )

    st.markdown(
        f"""
        <div class="pp-grid-2 pp-visual-grid">
          <section class="pp-section-card">
            <span class="pp-sc-kicker">Drinking Rhythm</span>
            <h2>Liked drinks by time of day</h2>
            <div class="pp-filter-chips">{time_chips}</div>
            {time_grid}
          </section>
          <section class="pp-section-card">
            <span class="pp-sc-kicker">Mood Match</span>
            <h2>Best choices from moods you have already lived through</h2>
            <div class="pp-filter-chips">{mood_chips}</div>
            {mood_grid}
          </section>
        </div>
        <div class="pp-grid-2 pp-lower-grid">
          <section class="pp-section-card">
            <span class="pp-sc-kicker">Top Drinks</span>
            <h2>Your most repeated drinks so far</h2>
            {_drink_grid_html(top_drinks, limit=5, compact=True)}
          </section>
          <section class="pp-section-card">
            <span class="pp-sc-kicker">Habit Insights</span>
            <h2>Your coffee pattern readout</h2>
            <div class="pp-insight-lede">
              <span>Current read</span>
              <strong>{insight_summary}</strong>
            </div>
            <div class="pp-pattern-list">{pattern_items}</div>
          </section>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_profile_subnav(active: str) -> None:
    dash_active = "active" if active == "dashboard" else ""
    hist_active = "active" if active == "history" else ""
    st.markdown(
        f"""
        <div class="profile-subnav">
          <a class="{dash_active}" href="?profile_view=dashboard">Dashboard</a>
          <a class="{hist_active}" href="?profile_view=history">Brew History</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_profile_corner_logout(user_name: str) -> None:
    initial = escape(str(user_name or "C").strip()[:1].upper() or "C")
    st.markdown(
        f"""
        <a class="profile-corner-logout" href="?profile_action=logout" title="Sign out">
          <span class="pcl-avatar">{initial}</span>
          <span class="pcl-copy">
            <em>Profile</em>
            <strong>Sign out</strong>
          </span>
        </a>
        """,
        unsafe_allow_html=True,
    )


def _format_history_date(timestamp: str) -> str:
    try:
        dt = datetime.fromisoformat(str(timestamp))
        return dt.strftime("%b %d, %Y · %I:%M %p").replace(" 0", " ")
    except Exception:
        return "Saved brew"


def _render_profile_history(tracker: HistoryTracker) -> None:
    recs = list(reversed(tracker.get_all()))
    stats = tracker.get_stats()

    if not recs:
        st.markdown(
            '<section class="profile-history-page">'
            '<div class="profile-history-hero">'
            '<span>Brew History</span>'
            '<h1>No saved brews yet</h1>'
            '<p>Use Save to history on a recommendation result card, then your full coffee timeline will appear here.</p>'
            '</div>'
            '</section>',
            unsafe_allow_html=True,
        )
        return

    total = escape(str(stats.get("total_drinks", len(recs))))
    unique = escape(str(stats.get("unique_drinks", len({rec.drink_name for rec in recs}))))
    avg = escape(str(stats.get("avg_match_score", 0)))
    favorite = escape(str(stats.get("favorite_drink", "None yet")))

    cards = []
    for idx, rec in enumerate(recs, start=1):
        drink = escape(str(rec.drink_name))
        date = escape(_format_history_date(rec.timestamp))
        mood = escape(_format_dashboard_label(rec.mood, "Mood not logged"))
        time = escape(_format_dashboard_label(rec.time_of_day, "Time not logged"))
        temp = escape(_format_dashboard_label(rec.temperature, "Temp not logged"))
        location = escape(_format_dashboard_label(rec.location, "Location not logged"))
        score = escape(str(rec.match_score or 0))
        cup = (
            _composition_cup_html(
                rec.composition or {},
                str(rec.temperature).lower() in {"iced", "cold"},
            )
            or _cup_html(str(rec.drink_name))
        )
        cards.append(
            f'<article class="profile-history-card">'
            f'<div class="ph-card-cup">{cup}</div>'
            f'<div class="ph-card-body">'
            f'<div class="ph-card-top"><span>{date}</span><em>{score}% match</em></div>'
            f'<h2>{drink}</h2>'
            f'<div class="ph-chip-row">'
            f'<span>{location}</span><span>{temp}</span><span>{mood}</span><span>{time}</span>'
            f'</div></div>'
            f'<strong class="ph-index">{idx:02d}</strong>'
            f'</article>'
        )

    st.markdown(
        f'<section class="profile-history-page">'
        f'<div class="profile-history-hero">'
        f'<span>Brew History</span>'
        f'<h1>Your saved coffee timeline</h1>'
        f'<p>Every recommendation you save lands here, then feeds the personality dashboard above.</p>'
        f'</div>'
        f'<div class="profile-history-stats">'
        f'<div><span>Total saved</span><strong>{total}</strong></div>'
        f'<div><span>Unique drinks</span><strong>{unique}</strong></div>'
        f'<div><span>Avg match</span><strong>{avg}%</strong></div>'
        f'<div><span>Favorite</span><strong>{favorite}</strong></div>'
        f'</div>'
        f'<div class="profile-history-list">{"".join(cards)}</div>'
        f'</section>',
        unsafe_allow_html=True,
    )


if not st.session_state.get("is_authenticated"):
    _render_login_page(client, _backend_live)
    st.stop()


# ── Navigation ────────────────────────────────────────────────────────────────
# Handle nav clicks BEFORE reading page so the same run sees the new value.
# No st.rerun() — a button click already triggers a rerun automatically.
_nav_items = {
    "n_home":     "home",
    "n_rec":      "recommend",
    "n_barista":  "barista",
    "n_ins":      "insights",
    "n_profile":  "profile",
}
for _key, _dest in _nav_items.items():
    if st.session_state.get(_key):          # button was just clicked
        st.session_state.page = _dest

page = st.session_state.page               # read AFTER potential update

# Active-page pill highlight: col index 2=Home 3=Recommend 4=Barista 5=Insights 6=Profile
_active_col = {"home": 2, "recommend": 3, "barista": 4, "insights": 5, "profile": 6}.get(page, 2)
st.markdown(
    f"<style>[data-testid='stHorizontalBlock'] "
    f"[data-testid='column']:nth-child({_active_col}) button {{"
    f"background: #FFFFFF !important; color: #0A0A0A !important;"
    f"font-weight:700 !important; transform: scale(1) !important;"
    f"transition: all 0.5s cubic-bezier(0.34, 1.1, 0.64, 1) !important;}}</style>",
    unsafe_allow_html=True,
)

nav = st.columns([1.75, 1.05, 1.26, 1.18, 1.08, 1.08])
with nav[0]:
    user_name = st.session_state.get("auth_user", {}).get("name", "Coffee Lover")
    greeting = f'<p class="nav-user">Hi, {escape(str(user_name))}</p>' if page == "home" else ""
    st.markdown(
        f'<p class="nav-brand">Coffee<br>Companion</p>{greeting}',
        unsafe_allow_html=True,
    )
with nav[1]:
    st.button("Home",      key="n_home", use_container_width=True)
with nav[2]:
    st.button("Recommend", key="n_rec",  use_container_width=True)
with nav[3]:
    st.button("Barista", key="n_barista",  use_container_width=True)
with nav[4]:
    st.button("Insights",  key="n_ins",  use_container_width=True)
with nav[5]:
    st.button("Profile", key="n_profile",  use_container_width=True)

st.markdown('<hr class="nav-divider">', unsafe_allow_html=True)

# Tiny status dot in the nav area
_status_color = "#4CAF50" if _backend_live else "#888"
_status_label = "Live" if _backend_live else "Mock"
st.markdown(
    f"<div style='position:fixed;bottom:1.1rem;right:1.4rem;z-index:999;"
    f"font-size:0.6rem;letter-spacing:2px;text-transform:uppercase;"
    f"color:{_status_color};font-family:Satoshi,sans-serif;'>"
    f"<span style='display:inline-block;width:6px;height:6px;border-radius:50%;"
    f"background:{_status_color};margin-right:5px;vertical-align:middle;'></span>"
    f"API {_status_label}</div>",
    unsafe_allow_html=True,
)

# ── Home ──────────────────────────────────────────────────────────────────────
if page == "home":
    # Get hero image
    hero_b64 = _img_b64("hero.jpg")
    bg_img = (
        f"url('data:image/jpeg;base64,{hero_b64}')"
        if hero_b64
        else "linear-gradient(160deg, #2C1810 0%, #5C3422 100%)"
    )

    # ── Hero Section with Image & Animation ──────────────────────────────────
    st.markdown(
        f"""
        <div class="hero-wrap">
            <div class="hero-bg" style="background-image:{bg_img};"></div>
            <div class="hero-overlay"></div>
            <div class="hero-content" style="--stagger-root:0s;">
                <span class="hero-eyebrow" style="animation: fadeInUp 0.9s cubic-bezier(0.22,1,0.36,1) both; animation-delay:0.20s;">Welcome back, Coffee Lover!</span>
                <h1 class="hero-title" style="color: #FFFFFF !important; animation: fadeInUp 1.0s cubic-bezier(0.22,1,0.36,1) both; animation-delay:0.35s;">Your perfect brew,<br>every time.</h1>
                <div class="hero-rule" style="animation: lineGrow 1s ease-out both; animation-delay:0.60s;"></div>
                <p class="hero-subtitle" style="animation: fadeInUp 0.9s cubic-bezier(0.22,1,0.36,1) both; animation-delay:0.75s;">Personalized. Smart. Delicious.</p>
            </div>
            <div class="hero-scroll" style="animation: fadeIn 0.9s ease-out both; animation-delay:1.05s;">
                <span></span>
                <p>Scroll</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Rowa-style CTA ────────────────────────────────────────────────────────
    rowa_l, rowa_m, rowa_r = st.columns([1.0, 1.4, 1.6], gap="large")

    with rowa_l:
        st.markdown(
            '<h2 class="home-cta-tagline" style="animation: fadeInUp 0.9s cubic-bezier(0.22,1,0.36,1) both; animation-delay:1.10s;">A crafted experience<br>for every coffee moment.</h2>',
            unsafe_allow_html=True,
        )

    with rowa_m:
        bean_b64 = _img_b64("coffee-bean-icon.png")
        bean_bg = f"url('data:image/png;base64,{bean_b64}')" if bean_b64 else "none"
        st.markdown(
            f"""
            <div id="pill-expand-circle"></div>
            <div class="rowa-pill-outer">
                <a class="rowa-pill" id="rowa-cta-pill" href="?pill_nav=recommend" style="animation: fadeInUp 0.9s cubic-bezier(0.22,1,0.36,1) both; animation-delay:1.25s;"
                   onclick="event.preventDefault();if(window._pillExpanding)return false;window._pillExpanding=true;var o=document.getElementById('pill-expand-circle');if(o){{o.classList.add('zooming');}}setTimeout(function(){{window._pillExpanding=false;window.location.href='?pill_nav=recommend';}},520);return false;">
                    <span class="rowa-pill-icon" style="background-image:{bean_bg};"></span>
                    <span class="rowa-pill-text">Get Recommendation</span>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with rowa_r:
        st.markdown(
            '<p class="home-cta-desc" style="animation: fadeInUp 0.9s cubic-bezier(0.22,1,0.36,1) both; animation-delay:1.40s;">Tell us your mood, your taste, and your moment \n we\'ll find the perfect brew that fits you right now.</p>',
            unsafe_allow_html=True,
        )

    # ── Card grid — single HTML block so layout is not subject to Streamlit columns ──
    tracker      = HistoryTracker()
    stats        = tracker.get_stats()
    total_drinks = stats.get('total_drinks', 0)
    favorite     = stats.get('favorite_drink', 'None yet')
    avg_score    = stats.get('avg_match_score', 0)
    user_name = st.session_state.get("auth_user", {}).get("name", st.session_state.get("display_name", "Coffee Lover"))
    dashboard = _build_streamlit_dashboard(tracker, str(user_name or "Coffee Lover"))

    brew_word = "brew" if total_drinks == 1 else "brews"
    fav_display = favorite if favorite != "None yet" else "Start exploring"

    st.markdown(
        f"""<div class="home-grid" style="margin-top:3rem;"><a href="?pill_nav=insights" class="home-card hc-insights"><div class="hc-arrow">&#8599;</div><div class="hc-inner"><span class="hc-label">Discover</span><div class="hc-title">Explore<br>Insights</div><div class="hc-sub">Trends, science and global facts behind your perfect cup</div></div></a><div class="home-grid-right"><div class="home-grid-top"><a href="?pill_nav=profile" class="home-card hc-stats"><div class="hc-arrow">&#8599;</div><div class="hc-inner"><span class="hc-label">Your Profile</span><span class="hc-stat-num">{total_drinks}</span><span class="hc-stat-unit">{brew_word} logged</span><div class="hc-sub">Favourite - {fav_display}</div></div></a><div class="home-card hc-tip hc-static-tip"><div class="hc-inner"><span class="hc-label">Today's Tip</span><div class="hc-title">Stay<br>Hydrated</div><div class="hc-sub">Drinking water between coffees reduces jitters and sharpens taste</div></div></div></div><div class="home-card hc-fact hc-static-fact"><div class="hc-inner"><span class="hc-label">Coffee Fact</span><div class="hc-title">Finland drinks more coffee per person than any country.</div><div class="hc-sub">10.1 kg per person each year, which is a lot of morning rituals.</div></div></div></div></div>""",
        unsafe_allow_html=True,
    )
    _render_dashboard_preview(dashboard)

    # ── Stats ticker ──────────────────────────────────────────────────────────
    items = [
        f'<div class="ticker-item"><span class="ticker-dot"></span> <strong>{total_drinks}</strong> drinks explored</div>',
        f'<div class="ticker-item"><span class="ticker-dot"></span> Favourite: <strong>{favorite}</strong></div>',
        f'<div class="ticker-item"><span class="ticker-dot"></span> Avg match score: <strong>{avg_score}%</strong></div>',
        '<div class="ticker-item"><span class="ticker-dot"></span> Finland leads global consumption: <strong>10.1 kg / person</strong></div>',
        '<div class="ticker-item"><span class="ticker-dot"></span> Culture explains <strong>85%</strong> of cross-country variance</div>',
        '<div class="ticker-item"><span class="ticker-dot"></span> Work hours ≈ <strong>no effect</strong> on coffee intake</div>',
    ]
    track = "".join(items * 2)
    st.markdown(
        f'<div class="ticker-wrap" style="animation: fadeInUp 0.9s ease-out both; animation-delay:2.25s;"><div class="ticker-track">{track}</div></div>',
        unsafe_allow_html=True,
    )

elif page == "recommend":
    render_recommendation_page(client)

elif page == "barista":
    render_barista_bot_page(client)

elif page == "insights":
    render_insights_page(client)

elif page == "profile":
    tracker = HistoryTracker()
    user_name = st.session_state.get("display_name") or st.session_state.get("auth_user", {}).get("name", "Coffee Lover")
    dashboard = _build_streamlit_dashboard(tracker, str(user_name or "Coffee Lover"))
    _render_profile_corner_logout(str(user_name or "Coffee Lover"))
    profile_view = st.query_params.get("profile_view", "dashboard")
    if profile_view not in {"dashboard", "history"}:
        profile_view = "dashboard"
    _render_profile_subnav(profile_view)
    if profile_view == "history":
        _render_profile_history(tracker)
    else:
        _render_profile_dashboard(dashboard)
        # Display name editor — compact, at bottom
        with st.expander("Edit display name"):
            display_name = st.text_input("Display name", value=st.session_state.get("display_name", ""), label_visibility="collapsed", placeholder="Your name")
            if st.button("Save", key="save_display_name"):
                st.session_state["display_name"] = display_name
                st.success("Saved")
