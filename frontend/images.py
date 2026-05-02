"""Central registry for all static images used in the frontend.

Small icons are base64-encoded into data URIs for inline HTML use.
Large backgrounds are exposed as Path objects for CSS/st.image use.
"""
from __future__ import annotations

import base64
from pathlib import Path

_STATIC = Path(__file__).parent.parent / "images"

_MIME = {"jpg": "jpeg", "jpeg": "jpeg", "png": "png", "avif": "avif", "webp": "webp"}


def _b64(filename: str) -> str:
    """Return a base64 data URI for a file in the static folder."""
    path = _STATIC / filename
    if not path.exists():
        return ""
    suffix = path.suffix.lstrip(".").lower()
    mime = _MIME.get(suffix, suffix)
    return f"data:image/{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def static(filename: str) -> Path:
    """Return the absolute Path for a static file."""
    return _STATIC / filename


# ── Small icons (base64 data URIs, safe for inline HTML) ─────────────────────

HOME_BREW_ICON  = _b64("home-brew-icon.png")   # home + coffee cup — barista location tile
COFFEE_BEAN_ICON = _b64("coffee-bean-icon.png") # coffee bean — general branding

# ── Backgrounds (Path objects, used via st.image or CSS url()) ────────────────

HERO_BG   = static("hero.jpg")   # main landing hero
CAFE_BG   = static("cafe.jpg")   # café atmosphere
HOME_BG   = static("home.jpg")   # home brewing
BEANS_BG  = static("beans.avif") # coffee beans texture
CUP_BG    = static("cup.avif")   # close-up cup
PATTERN   = static("pattern.avif") # decorative background pattern
