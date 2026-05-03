from __future__ import annotations

import base64
import math
import random
from pathlib import Path

import streamlit as st

from backend_client import CoffeeBackendClient
from history import HistoryTracker


# ── Asset loaders ─────────────────────────────────────────────────────────────

def _img_url(filename: str) -> str:
    path = Path(__file__).parent.parent / "images" / filename
    if not path.exists():
        return ""
    ext  = filename.rsplit(".", 1)[-1]
    mime = "image/avif" if ext == "avif" else ("image/jpeg" if ext == "jpg" else f"image/{ext}")
    b64  = base64.b64encode(path.read_bytes()).decode()
    return f"url('data:{mime};base64,{b64}')"


def _img_src(filename: str) -> str:
    path = Path(__file__).parent.parent / "images" / filename
    if not path.exists():
        return ""
    ext  = filename.rsplit(".", 1)[-1]
    mime = "image/avif" if ext == "avif" else ("image/jpeg" if ext == "jpg" else f"image/{ext}")
    b64  = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{b64}"


# ── Drink data ────────────────────────────────────────────────────────────────

_CAFE_HOT  = ["Espresso", "Cappuccino", "Flat White", "Macchiato", "Cortado", "Latte", "Americano", "Oat Latte"]
_CAFE_ICED = ["Cold Brew", "Iced Latte", "Iced Americano", "Iced Cappuccino"]
_CAFE_ALL  = _CAFE_HOT + _CAFE_ICED

_HOME_HOT  = ["French Press", "Pour-Over", "Aeropress", "Moka Pot Espresso", "Drip Coffee", "Chemex"]
_HOME_ICED = ["Cold Brew (DIY)", "Iced Coffee"]
_HOME_ALL  = _HOME_HOT + _HOME_ICED

_ICED = {"Cold Brew", "Iced Latte", "Iced Americano", "Iced Cappuccino", "Cold Brew (DIY)", "Iced Coffee"}

_DESC = {
    "Espresso":          "Intense and concentrated — the pure soul of coffee in one powerful shot.",
    "Cappuccino":        "Equal espresso, steamed milk, and velvety foam. A timeless classic.",
    "Flat White":        "Ristretto shots with silky microfoam — smooth, strong, sophisticated.",
    "Macchiato":         "Espresso 'stained' with a dash of milk. Bold with a gentle edge.",
    "Cortado":           "Equal espresso and warm milk — the perfect equilibrium.",
    "Latte":             "Espresso softened by abundant steamed milk. Silky and approachable.",
    "Americano":         "Espresso diluted with hot water — long, clean, full-bodied.",
    "Oat Latte":         "Espresso with creamy oat milk — nutty, sustainable, delicious.",
    "Cold Brew":         "Steeped 12–18 hours in cold water. Ultra-smooth, naturally sweet.",
    "Iced Latte":        "Espresso over ice with cold milk — refreshing and rich.",
    "Iced Americano":    "Espresso shots over ice. Clean and bracing.",
    "Iced Cappuccino":   "Chilled cappuccino layers over ice — frothy and cool.",
    "French Press":      "Full-immersion brewing for bold, rich body with natural oils.",
    "Pour-Over":         "Slow, precise pour extracts clarity and nuanced flavour.",
    "Aeropress":         "Pressure brewing in 1–2 minutes — versatile and coffee-forward.",
    "Moka Pot Espresso": "Stovetop pressure for strong, concentrated espresso-style coffee.",
    "Drip Coffee":       "Classic automatic brewing — reliable, consistent, comforting.",
    "Chemex":            "Clean, bright cup through thick filter paper — elegant simplicity.",
    "Cold Brew (DIY)":   "Coarse grounds steeped in cold water 12–18 hrs. Worth every minute.",
    "Iced Coffee":       "Double-strength brewed coffee over ice. Quick and satisfying.",
}

_CAFE_TIPS = {
    "Espresso":       "Ask for a double shot and drink within 30 seconds for peak flavour.",
    "Cappuccino":     "Request 'wet' for more milk or 'dry' for extra foam.",
    "Flat White":     "Order with ristretto shots for sweeter, less bitter flavour.",
    "Macchiato":      "Ask for 'latte macchiato' if you prefer milk-forward.",
    "Cortado":        "Usually 2 oz espresso + 2 oz milk — a perfect afternoon pick-me-up.",
    "Latte":          "Specify milk type — oat adds nuttiness, almond adds sweetness.",
    "Americano":      "Ask for hot water added to espresso, not the reverse.",
    "Oat Latte":      "Request barista-blend oat milk for the best foam texture.",
    "Cold Brew":      "Ask for it straight or with a splash of heavy cream.",
    "Iced Latte":     "Request light ice so it doesn't dilute too fast.",
    "Iced Americano": "A single pump of syrup perfectly balances the sharpness.",
    "Iced Cappuccino":"Ask for extra foam on top for the classic cappuccino feel.",
}

_BREW_STEPS = {
    "French Press":      ["Coarse grind · 30g : 450ml water", "Heat water to 93°C (just off boil)", "Pour all at once, stir gently", "Steep 4 minutes with lid on", "Press slowly · serve immediately"],
    "Pour-Over":         ["Medium grind · 1:15 ratio", "Pre-wet filter, discard water", "Bloom 30s with 2× coffee weight in water", "Pour in slow circles every 30–45s", "Total brew time: 3–4 minutes"],
    "Aeropress":         ["Medium-fine grind · 15g : 200ml", "Add grounds, pour at 90°C", "Stir 10s, steep for 1 minute", "Press firmly in 20–30 seconds", "Dilute with water or milk to taste"],
    "Moka Pot Espresso": ["Fine grind · fill basket level (no tamp)", "Fill base to below the pressure valve", "Assemble and heat on low-medium", "Remove at first gurgling sound", "Pour immediately, enjoy concentrated"],
    "Drip Coffee":       ["Medium grind · 1:15 ratio", "Pre-wet the paper filter", "Add coffee and press start", "Total brew: 5–7 minutes", "Serve fresh — don't let it sit on the warmer"],
    "Chemex":            ["Medium-coarse grind · 1:15 ratio", "Pre-wet thick filter, discard water", "Bloom 45s with 2× coffee weight", "Pour in slow circles every 45s", "Total: ~4 minutes for a clear, clean cup"],
    "Cold Brew (DIY)":   ["Coarse grind · 1:4 ratio (100g : 400ml)", "Combine in jar, stir gently", "Cover and refrigerate", "Steep 12–18 hours", "Strain through fine mesh or paper filter"],
    "Iced Coffee":       ["Medium grind · brew at 1:8 ratio (double strength)", "Fill glass with ice", "Pour hot coffee directly over ice", "Add milk or cream to taste", "Drink immediately for best flavour"],
}

_METHOD_TO_DRINK = {
    "french-press": "French Press",
    "pour-over":    "Pour-Over",
    "aeropress":    "Aeropress",
    "chemex":       "Chemex",
    "drip":         "Drip Coffee",
    "moka-pot":     "Moka Pot Espresso",
    "cold-brew":    "Cold Brew (DIY)",
    "iced-coffee":  "Iced Coffee",
}

# Cup layers list: (hex_color, label, flex_weight) — bottom → top
_LAYERS: dict[str, list[tuple[str, str, int]]] = {
    "Espresso":          [("#2A0E04","Espresso",4)],
    "Cappuccino":        [("#2A0E04","Espresso",2),("#C8A882","Milk",1),("#EDD8B8","Foam",1)],
    "Flat White":        [("#2A0E04","Espresso",2),("#C0966A","Milk",2)],
    "Macchiato":         [("#2A0E04","Espresso",3),("#EDD8B8","Foam",1)],
    "Cortado":           [("#2A0E04","Espresso",2),("#C0966A","Milk",2)],
    "Latte":             [("#2A0E04","Espresso",1),("#C8A882","Milk",3),("#EDD8B8","Foam",1)],
    "Americano":         [("#2A0E04","Espresso",1),("#5A2A10","Water",3)],
    "Oat Latte":         [("#2A0E04","Espresso",1),("#B89060","Oat Milk",3),("#E0C89A","Foam",1)],
    "Cold Brew":         [("#0C0402","Cold Brew",3),("#C0966A","Cream",1)],
    "Iced Latte":        [("#0C0402","Espresso",1),("#C8A882","Milk",2),("#C8E8F8","Ice",1)],
    "Iced Americano":    [("#0C0402","Espresso",1),("#4A2010","Water",2),("#C8E8F8","Ice",1)],
    "Iced Cappuccino":   [("#0C0402","Espresso",1),("#C8A882","Milk",1),("#C8E8F8","Ice",1),("#EDD8B8","Foam",1)],
    "French Press":      [("#2A1208","Coffee",4)],
    "Pour-Over":         [("#3A1A08","Coffee",4)],
    "Aeropress":         [("#2A0E04","Concentrate",3),("#B88850","Water",1)],
    "Moka Pot Espresso": [("#180604","Espresso",4)],
    "Drip Coffee":       [("#3A1A08","Coffee",3),("#C0966A","Milk",1)],
    "Chemex":            [("#402010","Coffee",4)],
    "Cold Brew (DIY)":   [("#0C0402","Cold Brew",3),("#C8E8F8","Ice",1)],
    "Iced Coffee":       [("#2A1208","Coffee",2),("#C8E8F8","Ice",1),("#C8A882","Milk",1)],
}

_WARNINGS = {
    "high":   "High caffeine — consider avoiding after 3 pm.",
    "medium": "Stay hydrated — pair with a glass of water.",
    "low":    "Low caffeine — great for a relaxed afternoon.",
    "none":   "Caffeine-free — enjoy any time of day.",
}

_BASE_REQUIRED_FIELDS = [
    "mood",
    "taste",
    "time_of_day",
    "temperature",
    "effort",
    "caffeine",
    "sweetness_preference",
    "texture_preference",
    "drink_style",
]

_COMPOSITION_COLORS = {
    "coffee": "#6E2F19",
    "espresso": "#3F160A",
    "milk": "#FFE7A8",
    "foam": "#FFF9DE",
    "ice": "#A9E2F2",
    "water": "#C89A72",
    "sugar": "#D39A3F",
    "chocolate": "#4E2719",
    "cream": "#E7C88C",
}

_COMPOSITION_FILL_COLORS = {
    "coffee": "#6E2F19",
    "espresso": "#3F160A",
    "milk": "#FFE7A8",
    "foam": "#FFF9DE",
    "ice": "#A9E2F2",
    "water": "#C89A72",
    "sugar": "#D39A3F",
    "chocolate": "#4E2719",
    "cream": "#E7C88C",
}

_COMPOSITION_STACK_ORDER = {
    "espresso": 0,
    "coffee": 1,
    "water": 2,
    "chocolate": 3,
    "sugar": 4,
    "ice": 5,
    "cream": 6,
    "milk": 7,
    "foam": 8,
}


# ── Visual helpers ────────────────────────────────────────────────────────────

def _pick_drink(pool: list[str], temperature: str, is_home: bool = False) -> str:
    if temperature == "iced":
        filtered = _HOME_ICED if is_home else _CAFE_ICED
    else:
        filtered = _HOME_HOT if is_home else _CAFE_HOT
    return random.choice(filtered) if filtered else random.choice(pool)


def _score_ring(score: int) -> str:
    r      = 48
    circ   = 2 * math.pi * r
    offset = circ * (1 - score / 100)
    return f"""
    <div class="score-ring-wrap">
      <svg viewBox="0 0 112 112" class="score-ring" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <linearGradient id="sg{score}" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%"   stop-color="#D4A96A"/>
            <stop offset="100%" stop-color="#A87340"/>
          </linearGradient>
        </defs>
        <circle cx="56" cy="56" r="{r}" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="5"/>
        <circle cx="56" cy="56" r="{r}" fill="none"
                stroke="url(#sg{score})" stroke-width="5" stroke-linecap="round"
                transform="rotate(-90 56 56)" class="score-arc"
                style="--arc-offset:{offset:.2f}; stroke-dasharray:{circ:.2f}"/>
        <text x="56" y="52" text-anchor="middle"
              font-family="Cormorant Garamond,serif" font-size="20" font-weight="300"
              fill="rgba(255,255,255,0.92)">{score}%</text>
        <text x="56" y="66" text-anchor="middle"
              font-family="Satoshi,sans-serif" font-size="6.5" letter-spacing="2.5"
              fill="rgba(201,168,124,0.65)">MATCH</text>
      </svg>
    </div>"""


def _cup_html(drink: str) -> str:
    layers = _LAYERS.get(drink, [("#2A1208","Coffee",4)])
    is_iced = drink in _ICED
    layers_html = "".join(
        f'<div class="cup-layer" style="--lbg:{c};--lf:{f};--ld:{i*0.15:.2f}s;">'
        f'<span class="cup-lbl">{lbl}</span></div>'
        for i, (c, lbl, f) in enumerate(layers)
    )
    if is_iced:
        return f"""<div class="cup-viz cup-glass">
          <div class="cup-glass-body">
            <div class="cup-glass-layers">{layers_html}</div>
            <div class="cup-glass-shine"></div>
          </div>
          <div class="cup-glass-straw"></div>
          <div class="cup-glass-base"></div>
        </div>"""
    return f"""<div class="cup-viz cup-mug">
      <div class="cup-steam">
        <span style="--sd:0s"></span><span style="--sd:0.65s"></span><span style="--sd:1.3s"></span>
      </div>
      <div class="cup-mug-wrap">
        <div class="cup-mug-body">
          <div class="cup-mug-layers">{layers_html}</div>
          <div class="cup-mug-shine"></div>
        </div>
        <div class="cup-mug-handle"></div>
      </div>
      <div class="cup-mug-saucer"></div>
    </div>"""


def _composition_cup_html(composition: dict, is_iced: bool, compact: bool = False) -> str:
    composition = composition or {}
    percent_map = {
        "coffee_percent": "coffee",
        "espresso_percent": "espresso",
        "milk_percent": "milk",
        "foam_percent": "foam",
        "ice_percent": "ice",
        "water_percent": "water",
        "cream_percent": "cream",
        "sugar_percent": "sugar",
        "chocolate_percent": "chocolate",
    }
    normalized = {
        percent_map[key]: value
        for key, value in composition.items()
        if key in percent_map and isinstance(value, (int, float)) and value > 0
    }
    if normalized:
        composition = normalized
    else:
        visual_keys = set(_COMPOSITION_COLORS)
        visual_composition = {
            key: value
            for key, value in composition.items()
            if key in visual_keys and isinstance(value, (int, float)) and value > 0
        }
        if visual_composition:
            composition = visual_composition

    segments = [
        (name, float(value))
        for name, value in (composition or {}).items()
        if isinstance(value, (int, float)) and value > 0
    ]
    segments.sort(key=lambda item: _COMPOSITION_STACK_ORDER.get(item[0], 50))
    total = sum(value for _, value in segments)
    if not segments or total <= 0:
        return ""

    stops = []
    label_blocks = []
    cursor = 0.0
    for name, value in segments:
        pct = value / total * 100
        start = cursor
        cursor += pct
        color = _COMPOSITION_FILL_COLORS.get(name, _COMPOSITION_COLORS.get(name, "#8B6B4A"))
        stops.append(f"{color} {start:.2f}% {cursor:.2f}%")
        label_blocks.append(
            f'<span class="cup-composition-label" style="bottom:{start:.2f}%;height:{pct:.2f}%;">'
            f'{_format_choice(name)} {pct:.0f}%</span>'
        )
    fill_gradient = f"linear-gradient(to top, {', '.join(stops)})"
    labels_html = "".join(label_blocks)

    layers_html = "".join(
        f'<div class="cup-layer" style="--lbg:{_COMPOSITION_COLORS.get(name, "#8B6B4A")};'
        f'--lf:{max(1, value)};--ld:{i*0.12:.2f}s;">'
        f'<span class="cup-lbl">{_format_choice(name)} {value / total * 100:.0f}%</span></div>'
        for i, (name, value) in enumerate(segments)
    )
    legend_html = "".join(
        f'<div class="composition-legend-item">'
        f'<span style="background:{_COMPOSITION_COLORS.get(name, "#8B6B4A")}"></span>'
        f'<b>{_format_choice(name)}</b><em>{value / total * 100:.0f}%</em></div>'
        for name, value in segments
    )

    if compact:
        labels_html = ""
        layers_html = ""
        legend_html = ""

    if is_iced:
        cup = f"""<div class="cup-viz cup-glass">
          <div class="cup-glass-body cup-fill-body" style="--drink-fill:{fill_gradient};">
            <div class="cup-composition-fill" style="background:{fill_gradient};"></div>
            <div class="cup-composition-labels">{labels_html}</div>
            <div class="cup-glass-layers">{layers_html}</div>
            <div class="cup-glass-shine"></div>
          </div>
          <div class="cup-glass-straw"></div>
          <div class="cup-glass-base"></div>
        </div>"""
    else:
        cup = f"""<div class="cup-viz cup-mug">
          <div class="cup-steam">
            <span style="--sd:0s"></span><span style="--sd:0.65s"></span><span style="--sd:1.3s"></span>
          </div>
          <div class="cup-mug-wrap">
            <div class="cup-mug-body cup-fill-body" style="--drink-fill:{fill_gradient};">
              <div class="cup-composition-fill" style="background:{fill_gradient};"></div>
              <div class="cup-composition-labels">{labels_html}</div>
              <div class="cup-mug-layers">{layers_html}</div>
              <div class="cup-mug-shine"></div>
            </div>
            <div class="cup-mug-handle"></div>
          </div>
          <div class="cup-mug-saucer"></div>
        </div>"""

    if compact:
        return cup
    return f'<div class="composition-wrap">{cup}<div class="composition-legend">{legend_html}</div></div>'


def _format_choice(value: str) -> str:
    return value.replace("-", " ").title()


def _chips(label: str, key: str, options: list[str]) -> None:
    st.markdown(f'<p class="rec-chip-label">{label}</p>', unsafe_allow_html=True)
    st.radio(
        label,
        options,
        index=None,
        key=key,
        format_func=_format_choice,
        label_visibility="collapsed",
        horizontal=True,
    )


def _missing_required_fields() -> list[str]:
    required = _BASE_REQUIRED_FIELDS
    labels = {
        "mood": "How are you feeling?",
        "taste": "Taste profile",
        "time_of_day": "Time of day",
        "temperature": "Temperature",
        "effort": "Preparation effort",
        "caffeine": "Caffeine",
        "sweetness_preference": "Sweetness",
        "texture_preference": "Texture",
        "drink_style": "Drink style",
    }
    return [labels[key] for key in required if not st.session_state.get(key)]


def _render_selection_status() -> None:
    selected_count = sum(1 for key in _BASE_REQUIRED_FIELDS if st.session_state.get(key))
    total_count = len(_BASE_REQUIRED_FIELDS)
    pct = int(selected_count / total_count * 100)
    selected_html = "".join(
        f'<span>{label}: <strong>{_format_choice(str(st.session_state[key]))}</strong></span>'
        for key, label in [
            ("mood", "Mood"),
            ("taste", "Taste"),
            ("time_of_day", "Time"),
            ("temperature", "Temp"),
            ("effort", "Effort"),
            ("caffeine", "Caffeine"),
            ("sweetness_preference", "Sweetness"),
            ("texture_preference", "Texture"),
            ("drink_style", "Style"),
        ]
        if st.session_state.get(key)
    )
    st.markdown(
        f"""
        <div class="brew-progress-panel">
          <div class="brew-progress-head">
            <span>Brew Profile</span>
            <strong>{selected_count}/{total_count}</strong>
          </div>
          <div class="brew-progress-track"><div style="width:{pct}%"></div></div>
          <div class="brew-summary-chips">{selected_html or '<em>Choose each category to build your cup.</em>'}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Sub-renderers ─────────────────────────────────────────────────────────────

def _show_mode_select() -> None:
    cafe_bg  = _img_url("cafe.jpg")
    home_bg  = _img_url("home.jpg")
    cafe_src = _img_src("cafe.png")
    home_src = _img_src("home-brew-icon.png")
    cafe_icon = f'<img src="{cafe_src}" class="mc-icon" alt="">' if cafe_src else ""
    home_icon = f'<img src="{home_src}" class="mc-icon mc-icon--home" alt="">' if home_src else ""
    cafe_bg_s = f'style="background-image:{cafe_bg};"' if cafe_bg else ""
    home_bg_s = f'style="background-image:{home_bg};"' if home_bg else ""

    st.markdown(f"""
    <div class="mode-select-page">
      <div class="mode-select-hdr">
        <span class="mode-select-eyebrow">Personalized · Precise · Perfect</span>
        <h1 class="mode-select-title">How are you brewing today?</h1>
        <p class="mode-select-sub">Choose your experience to begin</p>
      </div>
      <div class="mode-cards-grid">
        <a class="mode-card" href="?brew_mode=cafe&rec_step=form" {cafe_bg_s}>
          <div class="mc-overlay"></div>
          <div class="mc-inner">
            <div class="mc-icon-wrap">{cafe_icon}</div>
            <div class="mc-body">
              <h2 class="mc-title">Café Order</h2>
              <p class="mc-desc">Build a clean, café-style order with barista-ready suggestions and quick choices.</p>
              <div class="mc-tags">
                <span>Espresso</span><span>Cappuccino</span><span>Cold Brew</span><span>Flat White</span>
              </div>
            </div>
            <div class="mc-cta">Open Menu <span class="mc-arrow">→</span></div>
          </div>
        </a>
        <a class="mode-card" href="?brew_mode=home&rec_step=form" {home_bg_s}>
          <div class="mc-overlay mc-overlay--home"></div>
          <div class="mc-inner">
            <div class="mc-icon-wrap">{home_icon}</div>
            <div class="mc-body">
              <h2 class="mc-title">Homebrew</h2>
              <p class="mc-desc">Slow down and craft something beautiful. Artisan brewing in your kitchen</p>
              <div class="mc-tags">
                <span>French Press</span><span>Pour-Over</span><span>Aeropress</span><span>Chemex</span>
              </div>
            </div>
            <div class="mc-cta">Choose Home <span class="mc-arrow">→</span></div>
          </div>
        </a>
      </div>
    </div>""", unsafe_allow_html=True)


def _show_result(result: dict, payload: dict, is_home: bool) -> None:
    drink    = result.get("recommended_drink", "Unknown")
    score    = result.get("match_score", 0)
    caffeine = payload.get("caffeine_preference", "medium")
    temp     = payload.get("temperature_preference", "hot")
    mood     = payload.get("mood", "")
    label    = "Homebrew" if is_home else "Café Order"
    desc     = result.get("description") or _DESC.get(drink, "A perfect cup crafted just for you.")
    warning  = _WARNINGS.get(caffeine, "")
    order_tip = _CAFE_TIPS.get(drink, "Enjoy your coffee!")
    composition = result.get("composition", {})
    cup_html = _composition_cup_html(composition, temp == "iced") or _cup_html(drink)

    if is_home:
        steps   = _BREW_STEPS.get(drink, ["Brew and enjoy!"])
        steps_h = "".join(
            f'<li class="res-step" style="--d:{0.1 + i * 0.1:.2f}s">'
            f'<span class="res-step-n">{i + 1}</span><span>{s}</span></li>'
            for i, s in enumerate(steps)
        )
        detail = f'<div class="res-detail-label">PREPARATION</div><ul class="res-steps">{steps_h}</ul>'
    else:
      detail = (
        '<div class="res-detail-label">HOW TO ORDER</div>'
        f'<p class="res-tip">{order_tip}</p>'
        '<div class="cafe-order-note">Quick café order · minimal friction · barista friendly</div>'
      )

    badges = (
        f'<span class="res-badge">{temp.capitalize()}</span>'
        f'<span class="res-badge">{caffeine.capitalize()} caffeine</span>'
        f'{"<span class=\"res-badge\">" + mood.capitalize() + " mood</span>" if mood else ""}'
    )

    st.markdown(f"""
    <div class="res-layout">
      <div class="res-left">
        <span class="res-mode-lbl">{label}</span>
        <h2 class="res-name">{drink}</h2>
        <div class="res-badges">{badges}</div>
        <p class="res-desc">{desc}</p>
        {detail}
        {"<div class=\"res-warning\">" + warning + "</div>" if warning else ""}
      </div>
      <div class="res-right">
        {_score_ring(score)}
        {cup_html}
      </div>
    </div>""", unsafe_allow_html=True)


# ── Main page entry ───────────────────────────────────────────────────────────

def render_recommendation_page(client: CoffeeBackendClient) -> None:
    # Handle query params for step / mode transitions
    _mp = st.query_params.get("brew_mode", "")
    _sp = st.query_params.get("rec_step",  "")
    _action = st.query_params.get("result_action", "")

    if _mp or _sp:
        if _mp in ("cafe", "home"):
            if st.session_state.get("_brew_mode_val") != _mp:
                st.session_state.pop("last_result",  None)
                st.session_state.pop("last_payload", None)
                for key in (*_BASE_REQUIRED_FIELDS, "try_something_new", "brew_method"):
                    st.session_state.pop(key, None)
            st.session_state["_brew_mode_val"] = _mp
        if _sp:
            st.session_state["rec_step"] = _sp
            if _sp == "select":
                st.session_state.pop("last_result",  None)
                st.session_state.pop("last_payload", None)
        st.query_params.clear()

    brew_mode = st.session_state.get("_brew_mode_val", "")
    is_home   = brew_mode == "home"
    rec_step  = st.session_state.get("rec_step", "select")

    if _action and "last_result" in st.session_state:
        if _action == "try":
            current = st.session_state["last_result"].get("recommended_drink", "")
            payload = {
                **st.session_state.get("last_payload", {}),
                "try_something_new": True,
            }
            result = client.get_recommendation(payload)
            if (not result.get("_from_backend")) or result.get("recommended_drink") == current:
                pool = _HOME_ALL if is_home else _CAFE_ALL
                nxt = random.choice([d for d in pool if d != current] or pool)
                result = {
                    **result,
                    "recommended_drink": nxt,
                    "match_score": random.randint(70, 94),
                }
            st.session_state["last_payload"] = payload
            st.session_state["last_result"] = result
        elif _action == "save":
            r = st.session_state["last_result"]
            p = st.session_state.get("last_payload", {})
            HistoryTracker().add_recommendation(
                drink_name=r.get("recommended_drink", "Unknown"),
                mood=p.get("mood", ""),
                time_of_day=p.get("time_of_day", ""),
                temperature=p.get("temperature_preference", "hot"),
                location="home" if st.session_state.get("last_is_home") else "cafe",
                match_score=r.get("match_score", 0),
                composition=r.get("composition", {}),
            )
            st.session_state["rec_saved_notice"] = True
        elif _action == "start":
            for k in ("last_result", "last_payload", "_brew_mode_val"):
                st.session_state.pop(k, None)
            st.session_state["rec_step"] = "select"
        st.query_params.clear()
        st.rerun()

    # ── Step 0: mode selection ────────────────────────────────────────────────
    if rec_step == "select" or not brew_mode:
        _show_mode_select()
        return

    # ── Back header ───────────────────────────────────────────────────────────
    mode_label = "Homebrew" if is_home else "Café Order"
    icon_src   = _img_src("home-brew-icon.png" if is_home else "cafe.png")
    icon_cls   = "fh-icon fh-icon--home" if is_home else "fh-icon"
    icon_tag   = f'<img src="{icon_src}" class="{icon_cls}" alt="">' if icon_src else ""
    bg_url     = _img_url("home.jpg" if is_home else "cafe.jpg")
    bg_style   = f'style="background-image:{bg_url};"' if bg_url else ""

    cafe_shell_cls = " cafe-shell" if not is_home else ""
    st.markdown(f"""
    <div class="form-header{cafe_shell_cls}" {bg_style}>
      <div class="fh-overlay"></div>
      <div class="fh-content">
        <a class="fh-back" href="?rec_step=select">← Back</a>
        <div class="fh-badge">
          <div class="fh-icon-wrap">{icon_tag}</div>
          <span class="fh-mode-name">{mode_label}</span>
        </div>
      </div>
    </div>""", unsafe_allow_html=True)

    # ── Result display ────────────────────────────────────────────────────────
    if "last_result" in st.session_state:
        _show_result(
            st.session_state["last_result"],
            st.session_state.get("last_payload", {}),
            st.session_state.get("last_is_home", is_home),
        )
        if st.session_state.pop("rec_saved_notice", False):
            st.success("Saved to history.")
        st.markdown(
            """
            <div class="rec-result-action-row">
              <a href="?result_action=try">Try another</a>
              <a href="?result_action=save">Save to history</a>
              <a href="?result_action=start">Start over</a>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    # ── Preference form ───────────────────────────────────────────────────────
    st.markdown(
        f"""
        <div class="rec-builder-hero">
          <span>{mode_label}</span>
          <h1>Build your brew profile</h1>
          <p>Select each category below. The backend weighs every choice to brew a cup that matches your moment.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    _render_selection_status()
    st.markdown("<div style='height:1.45rem'></div>", unsafe_allow_html=True)
    fl, fr = st.columns([1.04, 0.96], gap="large")

    with fl:
        st.markdown('<div id="rec-quiz-marker"></div>', unsafe_allow_html=True)
        st.markdown(
            f'<p class="rec-col-title">{"Your Style" if is_home else "Your Vibe"}</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="rec-col-subtitle">Flavor, timing, and personality of the drink.</p>',
            unsafe_allow_html=True,
        )
        if not is_home:
            st.markdown('<p class="cafe-subtitle">A faster café menu with clear choices and less clutter.</p>', unsafe_allow_html=True)
        _chips("How are you feeling?", "mood", ["tired", "relaxed", "energetic"])
        _chips("Taste profile", "taste", ["bitter", "smooth", "sweet"])
        _chips("Time of day", "time_of_day", ["morning", "afternoon", "night"])
        _chips("Drink style", "drink_style", ["straight", "milky", "refreshing", "indulgent"])
        if is_home:
            _chips(
                "Brewing method",
                "brew_method",
                ["french-press", "pour-over", "aeropress", "chemex", "drip", "moka-pot", "cold-brew"],
            )

    with fr:
        st.markdown('<div id="rec-quiz-marker-2"></div>', unsafe_allow_html=True)
        st.markdown(
            f'<p class="rec-col-title">{"Your Brew" if is_home else "Your Cup"}</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="rec-col-subtitle">Temperature, caffeine, texture, and preparation feel.</p>',
            unsafe_allow_html=True,
        )
        _chips("Temperature", "temperature", ["hot", "iced"])
        _chips("Preparation effort", "effort", ["quick", "elaborate"])
        _chips("Caffeine", "caffeine", ["low", "medium", "high"])
        _chips("Sweetness", "sweetness_preference", ["not-sweet", "lightly-sweet", "sweet"])
        _chips("Texture", "texture_preference", ["light", "creamy", "foamy"])
        st.checkbox("Try something new", key="try_something_new")

    # ── Submit ────────────────────────────────────────────────────────────────
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    cta_label = "BREW MY CUP" if is_home else "BREW MY CUP"
    if st.button(cta_label, type="primary", use_container_width=True, key="brew_btn"):
        missing = _missing_required_fields()
        if missing:
            st.warning("Please select: " + ", ".join(missing))
            return

        payload = {
            "mood":                   st.session_state["mood"],
            "taste_preference":       st.session_state["taste"],
            "time_of_day":            st.session_state["time_of_day"],
            "temperature_preference": st.session_state["temperature"],
            "effort_level":           st.session_state["effort"],
            "caffeine_preference":    st.session_state["caffeine"],
            "sweetness_preference":   st.session_state["sweetness_preference"],
            "texture_preference":     st.session_state["texture_preference"],
            "drink_style":            st.session_state["drink_style"],
            "try_something_new":      st.session_state.get("try_something_new", False),
        }
        with st.spinner("Brewing your recommendation..."):
            result = client.get_recommendation(payload)
        # Only override with local pick when the backend is unavailable (mock mode)
        if not result.get("_from_backend"):
            chosen_method = st.session_state.get("brew_method") if is_home else None
            if chosen_method and chosen_method in _METHOD_TO_DRINK:
                result["recommended_drink"] = _METHOD_TO_DRINK[chosen_method]
            else:
                pool = _HOME_ALL if is_home else _CAFE_ALL
                result["recommended_drink"] = _pick_drink(
                    pool,
                    payload["temperature_preference"],
                    is_home,
                )
        st.session_state["last_result"]  = result
        st.session_state["last_payload"] = payload
        st.session_state["last_is_home"] = is_home
        st.rerun()
