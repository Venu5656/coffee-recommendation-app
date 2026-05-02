CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300&display=swap');
@import url('https://api.fontshare.com/v2/css?f[]=satoshi@900,700,500,400,300&display=swap');

/* ── Variables ──────────────────────────────────────────────────────────── */
:root {
    --bg:       #F9F6F1;
    --white:    #FFFFFF;
    --black:    #0A0A0A;
    --text:     #1C1C1C;
    --muted:    #888;
    --border:   #E5DDD3;
    --accent:   #C9A87C;
    --gold:     #B8936A;
    --espresso: #180E08;
    --dark:     #1A1008;
    --cream:    #F2EDE4;
}

/* ── Keyframes ──────────────────────────────────────────────────────────── */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(36px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes heroZoom {
    from { transform: scale(1.1);  filter: brightness(0.38); }
    to   { transform: scale(1.04); filter: brightness(0.48); }
}
@keyframes scrollBob {
    0%, 100% { transform: translateY(0) translateX(-50%); opacity: 0.6; }
    50%       { transform: translateY(8px) translateX(-50%); opacity: 1; }
}
@keyframes lineGrow {
    from { width: 0; opacity: 0; }
    to   { width: 100%; opacity: 1; }
}
@keyframes pulseDot {
    0%, 100% { box-shadow: 0 0 0 0 rgba(201,168,124,0.6); }
    50%       { box-shadow: 0 0 0 7px rgba(201,168,124,0); }
}
@keyframes marquee {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(40px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes fillBar {
    from { width: 0%; }
    to { width: 100%; }
}
@keyframes fadeInForm {
    from { opacity: 0; }
    to { opacity: 1; }
}
@keyframes scaleIn {
    from { opacity: 0; transform: scale(0.93) translateY(16px); }
    to   { opacity: 1; transform: scale(1) translateY(0); }
}
@keyframes recommendZoomIn {
    from { opacity: 0; transform: scale(1.08); filter: blur(10px); }
    to   { opacity: 1; transform: scale(1);    filter: blur(0); }
}
@keyframes categoryFloatIn {
    from {
        opacity: 0;
        transform: translateY(18px);
        filter: blur(5px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }
}
@keyframes cardHover {
    to { transform: translateY(-8px); box-shadow: 0 12px 32px rgba(0,0,0,0.15); }
}
@keyframes shimmer {
    0% { background-position: -1000px 0; }
    100% { background-position: 1000px 0; }
}
@keyframes slideIn {
    from { opacity: 0; transform: translateX(-20px); }
    to { opacity: 1; transform: translateX(0); }
}
@keyframes slideRight {
    from { opacity: 0; transform: translateX(-24px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes floatUp {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-10px); }
}
@keyframes borderPulse {
    0%, 100% { border-color: transparent; }
    50%       { border-color: var(--accent); }
}
@keyframes shimmerGold {
    0%   { background-position: -300% center; }
    100% { background-position:  300% center; }
}
@keyframes steamRise {
    0%   { opacity: 0;    transform: translateY(0)     scaleX(1);   }
    25%  { opacity: 0.55; }
    75%  { opacity: 0.2;  transform: translateY(-38px) scaleX(1.5); }
    100% { opacity: 0;    transform: translateY(-55px) scaleX(0.5); }
}
@keyframes liquidFill {
    from { transform: scaleY(0); transform-origin: bottom; }
    to   { transform: scaleY(1); transform-origin: bottom; }
}
@keyframes revealMask {
    from { clip-path: inset(0 100% 0 0); }
    to   { clip-path: inset(0 0%   0 0); }
}
@keyframes breathe {
    0%, 100% { opacity: 0.7; transform: scale(1);    }
    50%       { opacity: 1;   transform: scale(1.04); }
}
@keyframes dropIn {
    0%   { opacity: 0; transform: translateY(-26px) scale(0.97); }
    60%  { transform: translateY(4px) scale(1.01); }
    100% { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes staggerSlide {
    from { opacity: 0; transform: translateX(-12px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes glowPulse {
    0%, 100% { box-shadow: 0 0 30px rgba(201,168,124,0.07), 0 24px 64px rgba(0,0,0,0.4); }
    50%       { box-shadow: 0 0 60px rgba(201,168,124,0.15), 0 24px 64px rgba(0,0,0,0.4); }
}
@keyframes shimmerSweep {
    0%   { left: -150%; }
    100% { left:  150%; }
}
@keyframes arcDraw {
    from { stroke-dashoffset: 327; }
    to   { stroke-dashoffset: var(--arc-offset, 0); }
}
@keyframes cardSlideUp {
    from { opacity: 0; transform: translateY(36px) scale(0.96); }
    to   { opacity: 1; transform: translateY(0)    scale(1);    }
}
@keyframes mcEnter {
    0%   { opacity: 0; transform: translateY(40px) scale(0.97); }
    65%  { opacity: 1; transform: translateY(-4px) scale(1.005); }
    100% { opacity: 1; transform: translateY(0)    scale(1);     }
}
@keyframes pourIn {
    from { transform: scaleY(0); opacity: 0.4; }
    to   { transform: scaleY(1); opacity: 1;   }
}
@keyframes steamRiseNew {
    0%   { opacity: 0;    transform: translateY(10px) scaleY(0.62) scaleX(0.72); }
    18%  { opacity: 0.94; }
    58%  { opacity: 0.48; transform: translateY(-38px) scaleY(1.18) scaleX(1.08); }
    100% { opacity: 0;    transform: translateY(-78px) scaleY(1.7) scaleX(0.46); }
}
@keyframes resultCupFloat {
    0%, 100% { transform: translateY(0) rotate(-0.4deg); }
    50%      { transform: translateY(-9px) rotate(0.5deg); }
}
@keyframes resultCupWake {
    0%   { opacity: 0; transform: translateY(24px) scale(0.88) rotate(-2deg); filter: blur(2px); }
    62%  { opacity: 1; transform: translateY(-5px) scale(1.04) rotate(0.8deg); filter: blur(0); }
    100% { opacity: 1; transform: translateY(0) scale(1) rotate(0deg); filter: blur(0); }
}
@keyframes resultLiquidGlow {
    0%, 100% { background-position: 0% 0%, 0% 0%, 0% 0%; }
    50%      { background-position: 110% 0%, 0% 0%, 0% 0%; }
}
@keyframes resultSaucerGlow {
    0%, 100% { transform: scaleX(0.96); opacity: 0.52; }
    50%      { transform: scaleX(1.08); opacity: 0.92; }
}
@keyframes resultSteamDance {
    0%   { opacity: 0;    transform: translateY(12px) scaleY(0.25) scaleX(0.7);  filter: blur(1.2px); }
    14%  { opacity: 0.82; transform: translateY(0)    scaleY(0.8)  scaleX(0.95); filter: blur(0.85px); }
    48%  { opacity: 0.46; transform: translateY(-46px) scaleY(1.55) scaleX(1.12); filter: blur(1.4px); }
    76%  { opacity: 0.18; transform: translateY(-84px) scaleY(2.2)  scaleX(0.58); filter: blur(2px); }
    100% { opacity: 0;    transform: translateY(-116px) scaleY(2.85) scaleX(0.22); filter: blur(2.6px); }
}
@keyframes resSlideLeft {
    from { opacity: 0; transform: translateX(-28px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes resSlideRight {
    from { opacity: 0; transform: translateX(28px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes fhFade {
    from { opacity: 0; transform: translateY(-12px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes tilePop {
    0%   { opacity: 0; transform: translateY(14px) scale(0.95); }
    60%  { opacity: 1; transform: translateY(-3px) scale(1.01); }
    100% { opacity: 1; transform: translateY(0)    scale(1);    }
}
@keyframes checkBounce {
    0%   { transform: scale(0) rotate(-15deg); }
    55%  { transform: scale(1.28) rotate(5deg); }
    80%  { transform: scale(0.92) rotate(-2deg); }
    100% { transform: scale(1) rotate(0deg); }
}
@keyframes tileShimmer {
    0%   { left: -160%; }
    100% { left:  160%; }
}
@keyframes glowRing {
    0%, 100% { box-shadow: 0 0 0 0   rgba(201,168,124,0.35); }
    50%       { box-shadow: 0 0 0 6px rgba(201,168,124,0);    }
}
@keyframes loginBrandRise {
    from { opacity: 0; transform: translateY(18px) scale(0.96); filter: blur(6px); }
    to   { opacity: 1; transform: translateY(0) scale(1);       filter: blur(0);  }
}
@keyframes loginLogoGlow {
    0%, 100% { filter: drop-shadow(0 0 0 rgba(201,168,124,0)); }
    50%      { filter: drop-shadow(0 0 18px rgba(201,168,124,0.38)); }
}
@keyframes loginTitleShine {
    0%   { background-position: 0% center; }
    100% { background-position: 220% center; }
}

/* ── Base ───────────────────────────────────────────────────────────────── */
*, *::before, *::after { font-family: 'Satoshi', 'Satoshi Placeholder', sans-serif !important; box-sizing: border-box; }
h1, h2, h3, h4, h5     { font-family: 'Cormorant Garamond', serif !important; color: var(--text) !important; }
.stApp                  { background: var(--bg) !important; }

/* Dark sections must fully own their text colours — inherit defeats the global override */
.timeline-section,
.feat-main-card,
.ticker-wrap,
.ticker-track,
.ticker-item,
.home-card { color: #FFFFFF !important; }

.timeline-section *,
.feat-main-card *,
.ticker-item *,
.home-card .hc-inner * { color: #FFFFFF !important; }

.home-card .hc-label { color: var(--accent) !important; }

/* ── Sidebar → zero ─────────────────────────────────────────────────────── */
[data-testid="collapsedControl"],
button[kind="header"],
.st-emotion-cache-zq5wmm { display: none !important; }
section[data-testid="stSidebar"] {
    width: 0 !important; min-width: 0 !important;
    max-width: 0 !important; overflow: hidden !important; padding: 0 !important;
}
.main .block-container {
    max-width: 100% !important;
    padding: 0 3rem 6rem !important;
    animation: fadeIn 0.35s ease-out;
}

/* ── Login ─────────────────────────────────────────────────────────────── */
.login-page {
    width: calc(100% + 6rem);
    margin-left: -3rem;
    min-height: 100vh;
    padding: 3rem 4rem 5rem;
    background-image:
        linear-gradient(170deg, rgba(6,3,1,0.74) 0%, rgba(12,6,2,0.38) 48%, rgba(6,3,1,0.80) 100%),
        var(--login-bg, linear-gradient(180deg,#2A1208 0%,#0F0804 100%));
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
.login-brand {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1.1rem;
    color: #FFF8EE;
    font-size: clamp(2.2rem, 4vw, 3.2rem);
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    animation: loginBrandRise 0.75s cubic-bezier(0.22,1,0.36,1) both;
    transition: transform 0.35s ease, letter-spacing 0.35s ease;
}
.login-brand:hover {
    transform: translateY(-2px);
    letter-spacing: 2px;
}
.login-brand span {
    background: linear-gradient(90deg, #FFF8EE 0%, #D4A96A 42%, #FFF8EE 72%);
    background-size: 220% 100%;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: loginTitleShine 5.5s ease-in-out infinite alternate;
}
.login-logo-mark {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    height: 42px;
    color: #180E08;
    background: linear-gradient(135deg, var(--accent), var(--gold));
    border-radius: 50%;
    font-weight: 900;
}
.login-logo-img {
    width: 108px;
    height: 108px;
    object-fit: contain;
    display: block;
    filter: drop-shadow(0 4px 28px rgba(201,168,124,0.45));
    animation: loginLogoGlow 3.8s ease-in-out infinite;
    transition: transform 0.35s ease, filter 0.35s ease;
}
.login-brand:hover .login-logo-img {
    transform: scale(1.07) rotate(-2deg);
    filter: drop-shadow(0 6px 36px rgba(201,168,124,0.65));
}
[data-testid="column"]:has(#login-form-marker) {
    margin-top: -80vh;
    width: min(980px, calc(100vw - 8rem)) !important;
    max-width: 980px !important;
    justify-self: center;
    padding: 2.6rem 5.2rem 2.4rem;
    background: transparent !important;
    backdrop-filter: blur(18px) saturate(1.4);
    -webkit-backdrop-filter: blur(18px) saturate(1.4);
    border: 1px solid rgba(255,255,255,0.18) !important;
    border-radius: 12px !important;
    box-shadow:
        0 24px 72px rgba(0,0,0,0.28),
        inset 0 1px 0 rgba(255,255,255,0.16) !important;
    animation: categoryFloatIn 0.7s cubic-bezier(0.22,1,0.36,1) 0.12s both;
    transition: border-color 0.35s ease, box-shadow 0.35s ease, transform 0.35s ease;
}
[data-testid="column"]:has(#login-form-marker):hover {
    border-color: rgba(255,255,255,0.22) !important;
    box-shadow:
        0 36px 96px rgba(0,0,0,0.38),
        inset 0 1px 0 rgba(255,255,255,0.16),
        inset 0 -1px 0 rgba(0,0,0,0.06) !important;
    transform: translateY(-2px);
}
.login-form-heading h2 {
    color: #FFF8EE !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(4rem, 7vw, 6.5rem) !important;
    font-weight: 700 !important;
    line-height: 0.96 !important;
    text-align: center;
    margin: 0 0 1.1rem !important;
    letter-spacing: -0.01em !important;
}
.login-form-heading p {
    color: rgba(255,248,238,0.52);
    margin: 0.15rem 0 1rem;
    font-size: 0.82rem;
    text-align: center;
    line-height: 1.6;
}
[data-testid="column"]:has(#login-form-marker) [data-baseweb="tab-list"] {
    gap: 0.4rem;
    border-bottom: 1px solid rgba(255,255,255,0.12);
    margin-bottom: 1rem;
    overflow: visible !important;
}
[data-testid="column"]:has(#login-form-marker) [data-baseweb="tab"] {
    color: rgba(255,248,238,0.42);
    font-weight: 700;
    min-width: 0 !important;
    width: auto !important;
    padding-left: 1.1rem !important;
    padding-right: 1.1rem !important;
    white-space: nowrap !important;
}
[data-testid="column"]:has(#login-form-marker) [aria-selected="true"] {
    color: #FFF8EE !important;
}
[data-testid="column"]:has(#login-form-marker) .stTextInput input {
    background: rgba(255,252,245,0.10) !important;
    border: 1px solid rgba(255,255,255,0.16) !important;
    border-radius: 6px !important;
    color: #2A1208 !important;
    min-height: 48px !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease, background 0.25s ease !important;
}
[data-testid="column"]:has(#login-form-marker) .stTextInput input::placeholder {
    color: rgba(255,248,238,0.30) !important;
}
[data-testid="column"]:has(#login-form-marker) .stTextInput input:focus {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(212,169,106,0.18) !important;
    background: rgba(255,252,245,0.16) !important;
}
[data-testid="column"]:has(#login-form-marker) .stForm {
    border: 0;
    padding: 0;
}
[data-testid="column"]:has(#login-form-marker) .stForm label,
[data-testid="column"]:has(#login-form-marker) .stTextInput label {
    color: rgba(255,248,238,0.72) !important;
    font-weight: 700 !important;
}
[data-testid="column"]:has(#login-form-marker) .stFormSubmitButton button {
    background: linear-gradient(135deg, #8B5E34 0%, #5E3A18 100%) !important;
    color: #FFF8EE !important;
    border: 0 !important;
    border-radius: 999px !important;
    min-height: 48px !important;
    font-weight: 900 !important;
    letter-spacing: 0.6px !important;
    text-transform: uppercase !important;
    box-shadow: 0 4px 20px rgba(0,0,0,0.30) !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease, filter 0.25s ease !important;
}
[data-testid="column"]:has(#login-form-marker) .stFormSubmitButton button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 14px 36px rgba(0,0,0,0.40) !important;
    filter: brightness(1.12) !important;
}

/* ── Nav ────────────────────────────────────────────────────────────────── */

/* Let the first nav column overflow without clipping */
[data-testid="stHorizontalBlock"] > div:first-child {
    overflow: visible !important;
}

.nav-brand {
    font-family: 'Satoshi', sans-serif !important;
    font-size: clamp(1.35rem, 2vw, 1.75rem) !important; font-weight: 700 !important;
    letter-spacing: 2px !important; text-transform: uppercase !important;
    color: var(--black) !important; margin: 0 !important; line-height: 1.15 !important;
    padding-top: 0.2rem !important;
    transition: color 0.7s ease, text-shadow 0.7s ease;
    animation: slideInRight 1.2s cubic-bezier(0.34, 1.1, 0.64, 1) both;
    white-space: normal;
}
.nav-user {
    color: rgba(10,10,10,0.46) !important;
    font-size: 0.68rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    margin: -0.35rem 0 0 !important;
}
.nav-divider {
    border: none !important;
    border-top: 1px solid var(--border) !important;
    margin: 0 !important;
    transition: border-color 0.7s ease;
    animation: slideRight 1.4s cubic-bezier(0.34, 1.1, 0.64, 1) 0.2s both;
}
/* Nav row: segmented control with sliding active state */
[data-testid="stHorizontalBlock"] .stButton > button {
    background: #0A0A0A !important;
    border: none !important;
    border-radius: 0 !important;
    color: #FFFFFF !important;
    font-weight: 600 !important;
    font-size: 0.75rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    padding: 0.65rem 1.5rem !important;
    box-shadow: none !important;
    transition: all 0.8s cubic-bezier(0.34, 1.1, 0.64, 1) !important;
    margin: 0 !important;
    position: relative;
    animation: fadeIn 1s ease-out 0.3s both;
}
[data-testid="stHorizontalBlock"] .stButton:first-child > button {
    border-radius: 9999px 0 0 9999px !important;
}
[data-testid="stHorizontalBlock"] .stButton:last-child > button {
    border-radius: 0 9999px 9999px 0 !important;
}
[data-testid="stHorizontalBlock"] .stButton > button:not(:last-child) {
    border-right: 1px solid rgba(255,255,255,0.1) !important;
}
[data-testid="stHorizontalBlock"] .stButton > button:hover,
[data-testid="stHorizontalBlock"] .stButton > button:focus {
    background: #1A1008 !important;
    color: var(--accent) !important;
    box-shadow: inset 0 0 12px rgba(201,168,124,0.15) !important;
    transition: all 0.5s cubic-bezier(0.34, 1.1, 0.64, 1) !important;
}

/* ── All other buttons (page-level CTAs) ────────────────────────────────── */
.stButton > button {
    background: var(--black) !important; color: #FFFFFF !important;
    border: 1.5px solid var(--black) !important; border-radius: 0 !important;
    font-size: 0.75rem !important; font-weight: 600 !important;
    letter-spacing: 2px !important; text-transform: uppercase !important;
    padding: 0.75rem 2rem !important;
    transition: background 0.25s ease, color 0.25s ease, transform 0.15s ease !important;
    box-shadow: none !important;
}
.stButton > button:hover {
    background: transparent !important; color: var(--black) !important;
    border-color: var(--black) !important;
    transform: translateY(-1px) !important; box-shadow: none !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Selectbox ──────────────────────────────────────────────────────────── */
.stSelectbox [data-baseweb="select"] > div {
    border: 1px solid var(--border) !important; border-radius: 0 !important;
    background: var(--white) !important; transition: border-color 0.2s ease !important;
    font-size: 0.88rem !important;
}
.stSelectbox [data-baseweb="select"] > div:hover { border-color: var(--accent) !important; }

/* ── Progress bar ───────────────────────────────────────────────────────── */
.stProgress > div > div {
    background: rgba(0,0,0,0.06) !important; border-radius: 0 !important; height: 4px !important;
}
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--accent) 0%, var(--gold) 60%, #8B5E3C 100%) !important;
    border-radius: 0 !important; transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

/* ── Metrics ────────────────────────────────────────────────────────────── */
[data-testid="metric-container"] {
    background: var(--white) !important; border: 1px solid var(--border) !important;
    border-radius: 0 !important; padding: 1.5rem !important;
    transition: transform 0.22s ease, box-shadow 0.22s ease !important;
}
[data-testid="metric-container"]:hover {
    transform: translateY(-4px) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08) !important;
}
[data-testid="metric-container"] [data-testid="stMetricLabel"] {
    font-size: 0.65rem !important; letter-spacing: 2.5px !important;
    text-transform: uppercase !important; color: var(--muted) !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.2rem !important; color: var(--text) !important; line-height: 1.1 !important;
}

/* ── Tabs ───────────────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important; background: transparent !important;
}
.stTabs [data-baseweb="tab"] {
    font-size: 0.7rem !important; letter-spacing: 2.5px !important;
    text-transform: uppercase !important; color: var(--muted) !important;
    border-bottom: 2px solid transparent !important;
    padding: 1rem 2rem !important; font-weight: 500 !important;
    background: transparent !important; transition: color 0.2s ease !important;
}
.stTabs [aria-selected="true"] {
    color: var(--text) !important; border-bottom: 2px solid var(--accent) !important;
}

/* ── Alerts ─────────────────────────────────────────────────────────────── */
.stSuccess, .stInfo { border-radius:0 !important; border-left:3px solid var(--accent) !important; background:var(--cream) !important; }
.stWarning          { border-radius:0 !important; border-left:3px solid var(--gold)   !important; background:#FDF6EC !important; }

/* ── HR ─────────────────────────────────────────────────────────────────── */
hr { border:none !important; border-top:1px solid var(--border) !important; margin:2rem 0 !important; }

/* Choice card controls (replacement for simple radios) */
.choice-cards-grid {
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
}
.choice-card {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.45rem 0.85rem;
    min-width: 72px;
    border-radius: 6px;
    border: 1px solid rgba(255,255,255,0.06);
    background: transparent;
    color: rgba(255,255,255,0.9);
    text-decoration: none;
    transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, color 0.18s ease;
    font-family: 'Satoshi', sans-serif !important;
    font-size: 0.82rem !important;
    letter-spacing: 0.6px !important;
}
.choice-card .cc-label { font-weight: 600; font-size: 0.88rem; text-transform: none; color: inherit; }
.choice-card:hover { transform: translateY(-4px); box-shadow: 0 12px 28px rgba(0,0,0,0.14); border-color: rgba(200,160,120,0.9); color: var(--white); }
.choice-card.cc-selected { background: linear-gradient(90deg, rgba(201,168,124,0.08), rgba(168,120,60,0.02)); border-color: var(--accent); color: var(--white); box-shadow: 0 14px 36px rgba(0,0,0,0.20); position: relative; }
.choice-card.cc-selected::after { content: '\2713'; position: absolute; top: 6px; right: 8px; background: var(--accent); color: #fff; font-size: 0.65rem; padding: 2px 6px; border-radius: 6px; }

.brew-progress-panel {
    background:
        radial-gradient(circle at 18% 0%, rgba(255,236,194,0.16), transparent 34%),
        linear-gradient(135deg, #120B06 0%, #241207 55%, #0E0804 100%);
    border: 1px solid rgba(201,168,124,0.34);
    border-radius: 18px;
    padding: 1.05rem 1.25rem;
    box-shadow: 0 22px 58px rgba(0,0,0,0.30), inset 0 1px 0 rgba(255,255,255,0.06);
    max-width: 1180px;
    margin: 0 auto;
    animation: fadeInUp 0.65s cubic-bezier(0.22,1,0.36,1) 0.1s both;
}
.brew-progress-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.65rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 0.75rem;
}
.brew-progress-head strong {
    color: #FFFFFF;
    font-size: 0.8rem;
}
.brew-progress-track {
    width: 100%;
    height: 9px;
    background: rgba(255,255,255,0.08);
    border-radius: 999px;
    overflow: hidden;
    box-shadow: inset 0 1px 3px rgba(0,0,0,0.26);
}
.brew-progress-track div {
    height: 100%;
    background: linear-gradient(90deg, #8A4A28 0%, #C9A87C 54%, #FFF0B8 100%);
    border-radius: 999px;
    transition: width 0.35s ease;
    box-shadow: 0 0 18px rgba(241,212,155,0.28);
}
.brew-summary-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.85rem;
}
.brew-summary-chips span,
.brew-summary-chips em {
    border: 1px solid rgba(201,168,124,0.18);
    border-radius: 999px;
    padding: 0.38rem 0.68rem;
    color: rgba(255,255,255,0.72);
    background: rgba(255,255,255,0.035);
    font-size: 0.74rem;
    font-style: normal;
}
.brew-summary-chips strong {
    color: #FFFFFF;
}

.rec-builder-hero {
    max-width: 1180px;
    margin: 1.45rem auto 0;
    padding: 1.25rem 1.35rem;
    border: 1px solid rgba(126,83,46,0.13);
    border-radius: 18px;
    background:
        radial-gradient(circle at 92% 18%, rgba(201,168,124,0.22), transparent 32%),
        linear-gradient(135deg, rgba(255,253,248,0.96), rgba(245,232,207,0.70));
    box-shadow: 0 18px 46px rgba(90,55,27,0.10), inset 0 1px 0 rgba(255,255,255,0.80);
    animation: fadeInUp 0.7s cubic-bezier(0.22,1,0.36,1) both;
    position: relative;
    overflow: hidden;
}
.rec-builder-hero::after {
    content: '';
    position: absolute;
    right: 1.4rem;
    top: 1.1rem;
    width: 82px;
    height: 82px;
    border-radius: 50%;
    border: 1px solid rgba(126,83,46,0.18);
    box-shadow: inset 0 0 0 12px rgba(255,255,255,0.30);
    opacity: 0.72;
}
.rec-builder-hero span {
    display: block;
    color: #9B6B3F;
    font-size: 0.58rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.rec-builder-hero h1 {
    color: var(--text) !important;
    font-size: clamp(2.05rem, 3.2vw, 3.25rem) !important;
    font-weight: 900 !important;
    letter-spacing: 0 !important;
    margin: 0 !important;
    line-height: 0.98 !important;
    max-width: 680px;
}
.rec-builder-hero p {
    color: rgba(24,14,8,0.58);
    max-width: 620px;
    margin: 0.75rem 0 0;
    line-height: 1.65;
    font-size: 0.9rem;
}

/* ══════════════════════════════════════════════════════════════════════════
   BARISTA BOT — REDESIGNED
══════════════════════════════════════════════════════════════════════════ */

/* Barista-specific keyframes */
@keyframes messageBubbleIn {
    from { opacity: 0; transform: translateY(14px) scale(0.97); }
    to   { opacity: 1; transform: translateY(0)    scale(1);    }
}
@keyframes heroRuleGrow {
    from { transform: scaleX(0); transform-origin: left; }
    to   { transform: scaleX(1); transform-origin: left; }
}
@keyframes heroTextSlide {
    from { opacity: 0; transform: translateY(22px); }
    to   { opacity: 1; transform: translateY(0);    }
}
@keyframes cupFloat {
    0%, 100% { transform: translateY(0px);   }
    50%       { transform: translateY(-11px); }
}
@keyframes resultBloom {
    from { opacity: 0; transform: translateY(26px) scale(0.96); filter: blur(8px); }
    to   { opacity: 1; transform: translateY(0)    scale(1);    filter: blur(0);   }
}
@keyframes scoreCountUp {
    from { opacity: 0; transform: scale(0.72); }
    to   { opacity: 1; transform: scale(1);    }
}
@keyframes tileStagger {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0);    }
}

/* ── Hero ─────────────────────────────────────────────────────────────── */
.barista-hero {
    width: calc(100% + 6rem);
    margin-left: -3rem;
    min-height: 280px;
    padding: 3.5rem 4rem 3rem;
    background:
        linear-gradient(135deg, rgba(8,4,2,0.97) 52%, rgba(22,12,5,0.92) 100%),
        radial-gradient(ellipse at 88% 50%, rgba(201,168,124,0.16) 0%, transparent 55%);
    border-bottom: 1px solid rgba(201,168,124,0.14);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
    overflow: hidden;
}
.barista-hero-left {
    flex: 1;
    animation: heroTextSlide 0.75s cubic-bezier(0.22,1,0.36,1) both;
}
.barista-hero-right {
    flex-shrink: 0;
    animation: heroTextSlide 0.75s cubic-bezier(0.22,1,0.36,1) 0.12s both;
}
.barista-hero-kicker {
    display: block;
    color: var(--accent);
    font-size: 0.59rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-weight: 800;
    margin-bottom: 1rem;
}
.barista-hero h1 {
    font-family: 'Cormorant Garamond', serif !important;
    color: #FFFFFF !important;
    font-size: clamp(3.2rem, 6vw, 5.6rem) !important;
    font-weight: 300 !important;
    letter-spacing: 1px !important;
    line-height: 0.92 !important;
    margin: 0 0 1.3rem !important;
}
.barista-hero h1 em {
    font-style: italic;
    color: var(--accent) !important;
}
.barista-hero-rule {
    width: 60px;
    height: 1px;
    background: var(--accent);
    margin: 0 0 1.15rem;
    animation: heroRuleGrow 0.65s cubic-bezier(0.22,1,0.36,1) 0.28s both;
}
.barista-hero p {
    max-width: 500px;
    color: rgba(255,255,255,0.44);
    font-size: 0.91rem;
    line-height: 1.8;
    margin: 0;
}
.barista-hero-prompts {
    display: flex;
    flex-wrap: wrap;
    gap: 0.55rem;
    margin-top: 1.25rem;
}
.barista-hero-prompts span {
    color: rgba(255,255,255,0.68);
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(201,168,124,0.16);
    border-radius: 999px;
    padding: 0.46rem 0.72rem;
    font-size: 0.76rem;
    line-height: 1;
}

/* ── CSS coffee cup art ───────────────────────────────────────────────── */
.barista-cup-art {
    display: flex;
    flex-direction: column;
    align-items: center;
    animation: cupFloat 4.2s ease-in-out infinite;
}
.bca-steam {
    display: flex;
    gap: 13px;
    height: 50px;
    align-items: flex-end;
    margin-bottom: 2px;
}
.bca-s {
    width: 2px;
    border-radius: 2px;
    background: linear-gradient(to top, rgba(201,168,124,0.72), transparent);
    animation: steamRiseNew 2.8s ease-in-out infinite;
}
.bca-s1 { height: 34px; animation-delay: 0s;    }
.bca-s2 { height: 48px; animation-delay: 0.55s; }
.bca-s3 { height: 28px; animation-delay: 1.1s;  }
.bca-cup {
    width: 96px;
    height: 76px;
    background: linear-gradient(160deg, #2C1708, #160B04);
    border: 1.5px solid rgba(201,168,124,0.42);
    border-radius: 6px 6px 22px 22px;
    position: relative;
}
.bca-liquid {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 46%;
    background: linear-gradient(to top, rgba(201,168,124,0.52), rgba(201,168,124,0.1));
    border-radius: 0 0 20px 20px;
    animation: breathe 3.6s ease-in-out infinite;
}
.bca-handle {
    position: absolute;
    right: -17px; top: 16px;
    width: 17px; height: 34px;
    border: 1.5px solid rgba(201,168,124,0.42);
    border-left: none;
    border-radius: 0 17px 17px 0;
}
.bca-saucer {
    width: 126px; height: 11px;
    background: linear-gradient(90deg, transparent, rgba(201,168,124,0.13), transparent);
    border-radius: 50%;
    margin-top: 3px;
    border: 1px solid rgba(201,168,124,0.18);
}

/* ── Shared kicker label ──────────────────────────────────────────────── */
.barista-panel-kicker {
    display: block;
    color: var(--accent);
    font-size: 0.58rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-weight: 800;
    margin-bottom: 0.45rem;
}

/* ── Shared panel base ────────────────────────────────────────────────── */
.barista-chat-panel {
    background:
        radial-gradient(circle at top left, rgba(201,168,124,0.07), transparent 40%),
        linear-gradient(158deg, #121008, #1C1108 55%, #0F0804);
    border: 1px solid rgba(201,168,124,0.17);
    border-radius: 18px;
    box-shadow: 0 22px 68px rgba(0,0,0,0.34), inset 0 1px 0 rgba(255,255,255,0.04);
    animation: categoryFloatIn 0.7s cubic-bezier(0.22,1,0.36,1) both;
}

/* ── Chat panel ───────────────────────────────────────────────────────── */
.barista-chat-panel {
    padding: 1.35rem 1.35rem 1.1rem;
    min-height: 520px;
    display: flex;
    flex-direction: column;
}
.barista-chat-heading {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 1rem;
    border-bottom: 1px solid rgba(201,168,124,0.1);
    padding-bottom: 0.95rem;
}
.barista-chat-heading .barista-panel-kicker {
    margin-bottom: 0;
}
.barista-chat-heading strong {
    color: rgba(255,255,255,0.72);
    font-size: 0.86rem;
    font-weight: 500;
    text-align: right;
}
.barista-chat-scroll {
    flex: 1;
    margin-top: 1rem;
    max-height: 400px;
    overflow-y: auto;
    padding-right: 0.25rem;
    scrollbar-width: thin;
    scrollbar-color: rgba(201,168,124,0.2) transparent;
}
.barista-chat-scroll::-webkit-scrollbar       { width: 3px; }
.barista-chat-scroll::-webkit-scrollbar-track { background: transparent; }
.barista-chat-scroll::-webkit-scrollbar-thumb { background: rgba(201,168,124,0.22); border-radius: 3px; }

/* ── Messages ─────────────────────────────────────────────────────────── */
.barista-message-row {
    display: flex;
    margin: 0 0 0.85rem;
    animation: messageBubbleIn 0.42s cubic-bezier(0.22,1,0.36,1) both;
}
.barista-message-row.user    { justify-content: flex-end; }
.barista-message-row.barista { justify-content: flex-start; }
.barista-message {
    max-width: min(80%, 580px);
    padding: 0.88rem 1.1rem;
    border-radius: 20px;
    border: 1px solid rgba(201,168,124,0.13);
    background: rgba(255,255,255,0.03);
}
.msg-label {
    display: block;
    color: rgba(201,168,124,0.6);
    font-size: 0.54rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 0.38rem;
}
.barista-message p {
    margin: 0;
    color: rgba(255,255,255,0.74);
    line-height: 1.65;
    font-size: 0.9rem;
}
.barista-message-row.user .barista-message {
    background: rgba(255,248,238,0.93);
    border-color: rgba(201,168,124,0.26);
}
.barista-message-row.user .barista-message p {
    color: #1A0D06;
}
.barista-message-row.user .msg-label {
    color: rgba(176,118,58,0.72);
    text-align: right;
}
.barista-input-wrap {
    margin-top: 1rem;
    padding-top: 0.9rem;
    border-top: 1px solid rgba(201,168,124,0.09);
}

/* ── Profile panel ────────────────────────────────────────────────────── */
.barista-profile-panel {
    padding: 0.2rem 0 0 0.35rem;
    min-height: 420px;
    border-left: 1px solid rgba(24,14,8,0.16);
    animation: categoryFloatIn 0.7s cubic-bezier(0.22,1,0.36,1) both;
}
.barista-profile-panel h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 500 !important;
    font-size: 1.85rem !important;
    line-height: 1.08 !important;
    margin: 0.45rem 0 1.35rem !important;
}
.barista-profile-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0;
    border-top: 1px solid rgba(24,14,8,0.12);
}
.bpg-tile {
    display: grid;
    grid-template-columns: 34px 1fr auto;
    align-items: center;
    gap: 0.65rem;
    border: 0;
    border-bottom: 1px solid rgba(24,14,8,0.12);
    background: transparent;
    border-radius: 0;
    padding: 0.82rem 0;
    animation: tileStagger 0.5s cubic-bezier(0.22,1,0.36,1) both;
    transition: background 0.3s ease;
}
.bpg-tile:hover {
    background: rgba(201,168,124,0.08);
}
.bpg-tile:nth-child(1) { animation-delay: 0.06s; }
.bpg-tile:nth-child(2) { animation-delay: 0.12s; }
.bpg-tile:nth-child(3) { animation-delay: 0.18s; }
.bpg-tile:nth-child(4) { animation-delay: 0.24s; }
.bpg-icon     { font-size: 1.05rem; line-height: 1; margin-bottom: 0; }
.bpg-img-icon {
    width: 22px; height: 22px;
    object-fit: contain;
    display: block;
    margin-bottom: 0;
    filter: none;
    mix-blend-mode: multiply;
    opacity: 0.72;
}
.bpg-label {
    display: block;
    color: rgba(24,14,8,0.48);
    font-size: 0.53rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 700;
}
.bpg-tile strong {
    color: var(--espresso);
    font-size: 0.87rem;
    font-weight: 600;
    text-align: right;
}
.barista-concern-box {
    margin-top: 1.1rem;
    border-left: 2px solid var(--accent);
    background: rgba(201,168,124,0.08);
    border-radius: 0;
    padding: 0.78rem 0.9rem;
}
.barista-concern-box p {
    margin: 0.2rem 0 0;
    color: rgba(24,14,8,0.7);
    font-size: 0.87rem;
    line-height: 1.55;
}
.barista-profile-note {
    color: rgba(24,14,8,0.48);
    font-size: 0.78rem;
    line-height: 1.55;
    margin: 1rem 0 0;
}

/* ── Result panel ─────────────────────────────────────────────────────── */
.barista-result-panel {
    margin-top: 2rem;
    padding: 1.55rem 0;
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 1.5rem;
    border-top: 1px solid rgba(24,14,8,0.12);
    border-bottom: 1px solid rgba(24,14,8,0.12);
    animation: resultBloom 0.7s cubic-bezier(0.22,1,0.36,1) both !important;
}
.barista-result-panel h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 500 !important;
    font-size: 2.45rem !important;
    margin: 0.45rem 0 0.4rem !important;
}
.barista-score {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    color: #1A0D06;
    background: linear-gradient(135deg, var(--accent), var(--gold));
    border-radius: 50%;
    width: 94px;
    height: 94px;
    padding: 0.5rem;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    text-align: center;
    animation: scoreCountUp 0.5s cubic-bezier(0.22,1,0.36,1) 0.3s both;
    box-shadow: 0 4px 16px rgba(201,168,124,0.28);
}
.barista-result-panel p {
    color: rgba(24,14,8,0.64);
    line-height: 1.75;
    margin: 0;
    max-width: 780px;
}
.barista-warning {
    margin-top: 1rem;
    border-left: 2px solid var(--accent);
    color: rgba(24,14,8,0.7);
    padding-left: 1rem;
    font-size: 0.88rem;
}

/* ── Why panel ────────────────────────────────────────────────────────── */
.barista-why-panel {
    padding: 0.25rem 0 0 0.6rem;
    border-left: 1px solid rgba(24,14,8,0.12);
}
.barista-why-panel p {
    color: rgba(24,14,8,0.62);
    line-height: 1.72;
    font-size: 0.9rem;
    margin: 0.38rem 0;
}
.barista-why-panel strong {
    color: var(--espresso);
}

.composition-wrap {
    display: grid;
    grid-template-columns: minmax(160px, 0.9fr) minmax(150px, 1fr);
    gap: 1rem;
    align-items: center;
    width: 100%;
}
.composition-legend {
    display: grid;
    gap: 0.5rem;
}
.composition-legend-item {
    display: grid;
    grid-template-columns: 12px 1fr auto;
    align-items: center;
    gap: 0.55rem;
    padding: 0.48rem 0.6rem;
    border: 1px solid rgba(201,168,124,0.18);
    border-radius: 10px;
    background: rgba(255,255,255,0.04);
}
.composition-legend-item span {
    width: 12px;
    height: 12px;
    border-radius: 999px;
    border: 1px solid rgba(255,255,255,0.18);
}
.composition-legend-item b {
    color: rgba(255,255,255,0.86);
    font-size: 0.72rem;
    font-weight: 600;
}
.composition-legend-item em {
    color: var(--accent);
    font-size: 0.72rem;
    font-style: normal;
    font-weight: 700;
}


/* ══════════════════════════════════════════════════════════════════════════
   HERO
══════════════════════════════════════════════════════════════════════════ */
.hero-wrap {
    position: relative;
    width: calc(100% + 6rem);
    margin-left: -3rem;
    height: 95vh;
    min-height: 580px;
    max-height: 900px;
    overflow: hidden;
    display: flex; align-items: center; justify-content: center; text-align: center;
    margin-bottom: 0;
}
.hero-bg {
    position: absolute; inset: 0;
    background-size: cover; background-position: center 38%;
    animation: heroZoom 14s ease-out both;
}
.hero-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(to bottom, rgba(10,8,5,0.25) 0%, rgba(10,8,5,0.55) 60%, rgba(10,8,5,0.85) 100%);
}
.hero-content {
    position: relative; z-index: 2;
    animation: fadeInUp 1.1s cubic-bezier(0.22, 1, 0.36, 1) 0.25s both;
}
.hero-eyebrow {
    font-size: 0.68rem; letter-spacing: 5px; text-transform: uppercase;
    color: #FFFFFF; margin-bottom: 1.2rem; display: block;
    font-family: 'Satoshi', sans-serif;
    transition: opacity 0.6s ease, color 0.6s ease;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.5rem, 6vw, 5.5rem) !important;
    font-weight: 700 !important; color: #FFFFFF !important;
    letter-spacing: 10px !important; text-transform: uppercase !important;
    line-height: 1.0 !important; margin: 0 0 1.5rem !important;
    transition: font-size 0.8s ease, color 0.8s ease;
}
.hero-rule {
    width: 48px; height: 1px;
    background: var(--accent); margin: 0 auto 1.5rem;
    animation: lineGrow 1s ease-out 0.9s both;
}
.hero-subtitle {
    font-size: 0.78rem; letter-spacing: 3px; text-transform: uppercase;
    color: rgba(255,255,255,0.55); font-weight: 300;
    font-family: 'Satoshi', sans-serif;
    transition: color 0.6s ease, opacity 0.6s ease;
}
.hero-scroll {
    position: absolute; bottom: 2.5rem; left: 50%;
    animation: scrollBob 2.2s ease-in-out infinite;
    z-index: 3;
}
.hero-scroll span {
    display: block; width: 1px; height: 52px;
    background: linear-gradient(to bottom, rgba(255,255,255,0.6), transparent);
    margin: 0 auto;
}
.hero-scroll p {
    font-size: 0.6rem; letter-spacing: 3px; text-transform: uppercase;
    color: rgba(255,255,255,0.4); margin: 0.4rem 0 0;
    font-family: 'Satoshi', sans-serif;
}

/* ══════════════════════════════════════════════════════════════════════════
   DARK TIMELINE SECTION
══════════════════════════════════════════════════════════════════════════ */
.timeline-section {
    background: var(--espresso);
    width: calc(100% + 6rem);
    margin-left: -3rem;
    padding: 6rem 4rem;
    margin-bottom: 5rem;
}
.timeline-eyebrow {
    text-align: center; font-size: 0.65rem; letter-spacing: 4px;
    text-transform: uppercase; color: var(--accent); margin-bottom: 0.75rem;
    font-family: 'Satoshi', sans-serif; display: block;
}
.timeline-heading {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.5rem, 4vw, 3.8rem);
    font-weight: 300; color: #FFFFFF; text-align: center;
    letter-spacing: 2px; margin: 0 0 4rem;
}
.timeline-track {
    display: flex; align-items: flex-start;
    position: relative; gap: 0;
    max-width: 900px; margin: 0 auto;
}
.timeline-track::after {
    content: '';
    position: absolute; top: 10px; left: 10%; right: 10%; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(201,168,124,0.4) 20%, rgba(201,168,124,0.4) 80%, transparent);
    animation: lineGrow 1.4s ease-out 0.3s both;
}
.tl-step {
    flex: 1; text-align: center; padding: 0 1.5rem;
    position: relative;
    animation: fadeInUp 0.7s ease-out var(--d,0s) both;
}
.tl-dot {
    width: 10px; height: 10px; background: var(--accent);
    border-radius: 50%; margin: 5px auto 2rem;
    animation: pulseDot 2.5s ease-in-out var(--d,0s) infinite;
    position: relative; z-index: 1;
}
.tl-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 0.65rem; letter-spacing: 3px;
    text-transform: uppercase; color: var(--accent); margin-bottom: 0.6rem;
    display: block;
}
.tl-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.3rem; font-weight: 400; color: #FFFFFF;
    margin: 0 0 0.5rem; letter-spacing: 0.5px;
}
.tl-desc {
    font-size: 0.8rem; color: rgba(255,255,255,0.4);
    line-height: 1.7; font-weight: 300;
    font-family: 'Satoshi', sans-serif;
}

/* ══════════════════════════════════════════════════════════════════════════
   CLICKABLE CARD BUTTON  — the main dark recommend card IS the button
   Targeted via a #marker-div that lives in the same column via :has()
══════════════════════════════════════════════════════════════════════════ */
[data-testid="column"]:has(#card-btn-marker) .stButton > button {
    background: var(--espresso) !important;
    color: rgba(255,255,255,0.88) !important;
    border: none !important;
    min-height: 380px !important;
    width: 100% !important;
    text-align: left !important;
    align-items: flex-start !important;
    justify-content: flex-end !important;
    flex-direction: column !important;
    padding: 3rem !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.4rem !important;
    font-weight: 300 !important;
    letter-spacing: 1px !important;
    text-transform: none !important;
    line-height: 1.25 !important;
    position: relative !important;
    overflow: hidden !important;
    transition: background 0.35s ease !important;
    transform: none !important;
    display: flex !important;
}
[data-testid="column"]:has(#card-btn-marker) .stButton > button::before {
    content: '';
    position: absolute;
    font-size: 11rem; line-height: 1;
    opacity: 0.05; top: -1.5rem; right: -1.5rem;
    transition: transform 0.5s ease, opacity 0.4s ease;
    pointer-events: none;
}
[data-testid="column"]:has(#card-btn-marker) .stButton > button:hover {
    background: #2A1810 !important;
    color: #FFFFFF !important;
    transform: none !important;
    box-shadow: 0 24px 64px rgba(0,0,0,0.28) !important;
}
[data-testid="column"]:has(#card-btn-marker) .stButton > button:hover::before {
    transform: scale(1.08) rotate(8deg);
    opacity: 0.09;
}

/* ══════════════════════════════════════════════════════════════════════════
   FEATURE CARDS
══════════════════════════════════════════════════════════════════════════ */
.feat-section-label {
    font-size: 0.65rem; letter-spacing: 4px; text-transform: uppercase;
    color: var(--accent); margin-bottom: 0.5rem; display: block;
    transition: color 0.5s ease, opacity 0.5s ease;
}
.feat-section-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 3.5vw, 3rem);
    font-weight: 400; color: var(--text); margin: 0 0 3rem; line-height: 1.15;
    transition: color 0.5s ease, transform 0.5s ease;
}
.feat-main-card {
    background: var(--espresso);
    padding: 3.5rem 3rem;
    position: relative; overflow: hidden;
    min-height: 280px;
    display: flex; flex-direction: column; justify-content: flex-end;
    transition: box-shadow 0.7s ease, transform 0.7s ease, border-color 0.7s ease;
    animation: fadeInUp 0.8s ease-out 0.2s both;
}
.feat-main-card:hover { box-shadow: 0 24px 64px rgba(0,0,0,0.25); }
.feat-main-card::before {
    content: '';
    position: absolute; font-size: 11rem; opacity: 0.05;
    top: -2rem; right: -2rem; line-height: 1;
    transition: transform 0.6s ease, opacity 0.4s ease;
}
.feat-main-card:hover::before { transform: scale(1.08) rotate(8deg); opacity: 0.08; }
.feat-badge {
    display: inline-block;
    font-size: 0.6rem; letter-spacing: 3px; text-transform: uppercase;
    border: 1px solid rgba(201,168,124,0.4);
    color: var(--accent); padding: 0.3rem 0.75rem;
    margin-bottom: 1.25rem;
    transition: all 0.4s ease, border-color 0.4s ease, color 0.4s ease;
}
.feat-main-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.2rem; font-weight: 300; color: #FFFFFF;
    margin: 0 0 0.75rem; letter-spacing: 1px; line-height: 1.2;
    transition: color 0.5s ease, transform 0.5s ease, font-size 0.5s ease;
}
.feat-main-desc {
    font-size: 0.82rem; color: rgba(255,255,255,0.5);
    line-height: 1.7; margin: 0; font-weight: 300;
    font-family: 'Satoshi', sans-serif;
    transition: color 0.5s ease, opacity 0.5s ease;
}
.feat-side-card {
    border: 1px solid var(--border);
    background: var(--white);
    padding: 2rem 2rem;
    display: flex; align-items: flex-start; gap: 1.25rem;
    transition: transform 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease, background 0.4s ease;
    animation: fadeInUp 0.6s ease-out var(--d,0.2s) both;
    cursor: default;
}
.feat-side-card:hover {
    transform: translateX(5px);
    border-color: var(--accent);
    box-shadow: -4px 0 0 var(--accent), 4px 4px 20px rgba(0,0,0,0.06);
}
.feat-icon {
    font-size: 1.8rem; flex-shrink: 0; line-height: 1.3;
}
.feat-side-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem; font-weight: 500; margin: 0 0 0.3rem; color: var(--text);
}
.feat-side-desc {
    font-size: 0.8rem; color: var(--muted); line-height: 1.6;
    margin: 0; font-weight: 300; font-family: 'Satoshi', sans-serif;
}

/* ══════════════════════════════════════════════════════════════════════════
   STATS TICKER
══════════════════════════════════════════════════════════════════════════ */
.ticker-wrap {
    background: var(--espresso);
    width: calc(100% + 6rem);
    margin-left: -3rem;
    overflow: hidden;
    padding: 1.1rem 0;
    margin-top: 4rem;
    position: relative;
}
.ticker-wrap::before,
.ticker-wrap::after {
    content: '';
    position: absolute; top: 0; bottom: 0; width: 80px; z-index: 2;
}
.ticker-wrap::before { left: 0;  background: linear-gradient(to right, var(--espresso), transparent); }
.ticker-wrap::after  { right: 0; background: linear-gradient(to left,  var(--espresso), transparent); }
.ticker-track {
    display: flex; gap: 0; white-space: nowrap;
    animation: marquee 22s linear infinite;
    width: max-content;
}
.ticker-item {
    font-size: 0.72rem !important; letter-spacing: 2.5px; text-transform: uppercase;
    color: rgba(255,255,255,0.55) !important; padding: 0 2.5rem;
    display: flex; align-items: center; gap: 0.75rem;
    font-family: 'Satoshi', sans-serif !important;
}
.ticker-dot {
    display: inline-block; width: 4px; height: 4px;
    background: var(--accent); border-radius: 50%; flex-shrink: 0;
}
.ticker-item strong { color: rgba(255,255,255,0.9) !important; font-weight: 600; }

/* ══════════════════════════════════════════════════════════════════════════
   RECOMMENDER PAGE
══════════════════════════════════════════════════════════════════════════ */

/* ── Step 1: Quiz form setup ─────────────────────────────────────────── */
/* ── Step 2: Quiz form cards (both columns) ──────────────────────────── */
[data-testid="column"]:has(#rec-quiz-marker),
[data-testid="column"]:has(#rec-quiz-marker-2) {
    background:
        linear-gradient(90deg, rgba(126,83,46,0.14) 0 7px, transparent 7px),
        radial-gradient(circle at 12% 0%, rgba(201,168,124,0.24), transparent 30%),
        radial-gradient(circle at 100% 0%, rgba(255,249,229,0.72), transparent 28%),
        linear-gradient(150deg, rgba(255,250,242,0.98) 0%, rgba(242,226,199,0.94) 58%, rgba(255,253,248,0.96) 100%) !important;
    border: 1px solid rgba(126,83,46,0.16) !important;
    border-radius: 18px !important;
    padding: 2rem 2.15rem 2.15rem !important;
    min-height: 0;
    box-shadow: 0 20px 46px rgba(90,55,27,0.11), inset 0 1px 0 rgba(255,255,255,0.76) !important;
    transition: border-color 0.4s ease, box-shadow 0.4s ease, transform 0.4s ease;
    position: relative;
    overflow: hidden;
}
[data-testid="column"]:has(#rec-quiz-marker):hover,
[data-testid="column"]:has(#rec-quiz-marker-2):hover {
    border-color: rgba(126,83,46,0.28) !important;
    box-shadow: 0 28px 62px rgba(90,55,27,0.15), inset 0 1px 0 rgba(255,255,255,0.78) !important;
    transform: translateY(-2px);
}

/* Column section title */
.rec-col-title {
    font-family: 'Satoshi', 'Satoshi Placeholder', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 900 !important;
    color: var(--espresso) !important;
    letter-spacing: 0 !important;
    margin: 0 0 0.35rem !important;
    padding-bottom: 0 !important;
    border-bottom: none !important;
    text-shadow: none !important;
}
.rec-col-subtitle {
    margin: 0 0 1.15rem !important;
    padding-bottom: 0.95rem !important;
    border-bottom: 1px solid rgba(126,83,46,0.14);
    color: rgba(24,14,8,0.62) !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    line-height: 1.6 !important;
}

.rec-chip-label {
    font-size: 0.58rem !important; font-weight: 900 !important;
    color: #6F4525 !important;
    margin: 0 !important;
    letter-spacing: 2.2px !important; text-transform: uppercase !important;
}
.rec-filter-head {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin: 1.16rem 0 0.55rem;
}
.rec-filter-head > span {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    flex: 0 0 auto;
    background: #24140C;
    color: #F6DFAF;
    border: 1px solid rgba(126,83,46,0.28);
    font-size: 0.66rem;
    font-weight: 900;
    font-family: 'Satoshi', sans-serif;
    letter-spacing: 0;
    box-shadow: 0 7px 18px rgba(90,55,27,0.12);
}
.rec-filter-head small {
    display: block;
    margin-top: 0.18rem;
    color: rgba(24,14,8,0.42);
    font-size: 0.7rem;
    line-height: 1;
    font-weight: 700;
}

/* Backend-backed recommendation picker: native Streamlit pills, styled as premium controls */
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"],
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] {
    margin-bottom: 1.05rem !important;
    --primary-color: #C9A87C !important;
    --primary-color-background: rgba(201,168,124,0.18) !important;
    accent-color: #C9A87C !important;
}

[class*="st-key-rec_group_"] {
    opacity: 0;
    animation: categoryFloatIn 0.82s cubic-bezier(0.22, 1, 0.36, 1) both;
    will-change: transform, opacity, filter;
}
[class*="st-key-rec_group_"] .rec-chip-label,
[class*="st-key-rec_group_"] [data-testid="stPills"] {
    animation: none !important;
    opacity: 1 !important;
    transform: none !important;
    filter: none !important;
}
.st-key-rec_group_mood { animation-delay: 0.18s; }
.st-key-rec_group_taste { animation-delay: 0.30s; }
.st-key-rec_group_time_of_day { animation-delay: 0.42s; }
.st-key-rec_group_drink_style { animation-delay: 0.54s; }
.st-key-rec_group_temperature { animation-delay: 0.66s; }
.st-key-rec_group_effort { animation-delay: 0.78s; }
.st-key-rec_group_caffeine { animation-delay: 0.90s; }
.st-key-rec_group_sweetness_preference { animation-delay: 1.02s; }
.st-key-rec_group_texture_preference { animation-delay: 1.14s; }
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button,
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button {
    border: 1px solid rgba(201,168,124,0.22) !important;
    border-radius: 999px !important;
    background: rgba(255,255,255,0.04) !important;
    background-color: rgba(255,255,255,0.04) !important;
    color: rgba(255,255,255,0.72) !important;
    min-height: 2.65rem !important;
    padding: 0.58rem 1.05rem !important;
    margin: 0.18rem 0.32rem !important;
    transition: transform 0.18s ease, border-color 0.18s ease, background 0.18s ease, color 0.18s ease !important;
}
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button:hover,
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button:hover {
    transform: translateY(-2px) !important;
    border-color: rgba(201,168,124,0.7) !important;
    color: #FFFFFF !important;
    background: rgba(201,168,124,0.10) !important;
}
/* Selected pill — scoped to rec columns */
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button[aria-pressed="true"],
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button[aria-pressed="true"],
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button[aria-selected="true"],
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button[aria-selected="true"],
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button[aria-checked="true"],
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button[aria-checked="true"],
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button[data-selected="true"],
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button[data-selected="true"],
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button:focus,
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button:focus {
    background: #7B4A28 !important;
    background-color: #7B4A28 !important;
    border-color: #A06535 !important;
    color: #FFFFFF !important;
    box-shadow: 0 6px 20px rgba(0,0,0,0.22), inset 0 1px 0 rgba(255,255,255,0.10) !important;
}
/* Force white on ALL child nodes of selected pill — covers Streamlit's internal spans */
[data-testid="stPills"] button[aria-pressed="true"],
[data-testid="stPills"] button[aria-selected="true"],
[data-testid="stPills"] button[aria-checked="true"],
[data-testid="stPills"] button[data-selected="true"] {
    color: #FFFFFF !important;
}
[data-testid="stPills"] button[aria-pressed="true"] p,
[data-testid="stPills"] button[aria-pressed="true"] span,
[data-testid="stPills"] button[aria-pressed="true"] div,
[data-testid="stPills"] button[aria-pressed="true"] small,
[data-testid="stPills"] button[aria-selected="true"] p,
[data-testid="stPills"] button[aria-selected="true"] span,
[data-testid="stPills"] button[aria-selected="true"] div,
[data-testid="stPills"] button[aria-selected="true"] small,
[data-testid="stPills"] button[aria-checked="true"] p,
[data-testid="stPills"] button[aria-checked="true"] span,
[data-testid="stPills"] button[aria-checked="true"] div,
[data-testid="stPills"] button[aria-checked="true"] small,
[data-testid="stPills"] button[data-selected="true"] p,
[data-testid="stPills"] button[data-selected="true"] span,
[data-testid="stPills"] button[data-selected="true"] div,
[data-testid="stPills"] button[data-selected="true"] small {
    color: #FFFFFF !important;
}
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] button *,
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] button * {
    color: inherit !important;
}

/* ── Pill chips: hide native radio circle, style label as pill ── */
/* Works across Streamlit versions by targeting both data-baseweb and role attrs */
[data-testid="column"]:has(#rec-quiz-marker) .stRadio [data-baseweb="radio"] > div:first-child,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio [data-baseweb="radio"] > div:first-child,
[data-testid="column"]:has(#rec-quiz-marker) .stRadio div[role="radio"],
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio div[role="radio"] {
    display: none !important;
}
[data-testid="column"]:has(#rec-quiz-marker) .stRadio > label,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio > label,
[data-testid="column"]:has(#rec-quiz-marker) .stRadio [data-testid="stWidgetLabel"],
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio [data-testid="stWidgetLabel"] {
    display: none !important;
}
[data-testid="column"]:has(#rec-quiz-marker) .stRadio [data-baseweb="radio-group"],
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio [data-baseweb="radio-group"],
[data-testid="column"]:has(#rec-quiz-marker) .stRadio > div > div,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio > div > div {
    display: flex !important;
    flex-wrap: wrap !important;
    gap: 0.62rem !important;
    margin: 0.1rem 0 1.05rem !important;
}
/* Label pill styling — all descendants of the marked columns */
[data-testid="column"]:has(#rec-quiz-marker) .stRadio label,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio label {
    border: 1px solid rgba(126,83,46,0.22) !important;
    border-radius: 14px !important;
    padding: 0.62rem 1rem !important;
    cursor: pointer !important;
    font-size: 0.86rem !important; font-weight: 700 !important;
    color: rgba(24,14,8,0.70) !important;
    background:
        linear-gradient(180deg, rgba(255,255,255,0.86), rgba(255,250,240,0.76)) !important;
    transition: all 0.2s ease !important;
    white-space: nowrap !important;
    letter-spacing: 0.3px !important;
    margin: 0 !important;
    display: inline-flex !important;
    align-items: center !important;
    min-height: 2.65rem !important;
    user-select: none !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.74), 0 7px 16px rgba(90,55,27,0.06);
}
[data-testid="column"]:has(#rec-quiz-marker) .stRadio label:hover,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio label:hover {
    border-color: rgba(126,83,46,0.52) !important;
    color: var(--espresso) !important;
    background: rgba(255,248,237,0.96) !important;
    transform: translateY(-1px);
}
/* Selected state via :has(input:checked) */
[data-testid="column"]:has(#rec-quiz-marker) .stRadio label:has(input:checked),
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio label:has(input:checked) {
    background: linear-gradient(135deg, #9B6942, #7E4C2C) !important;
    border-color: rgba(95,54,28,0.72) !important;
    color: #FFF8EE !important;
    font-weight: 800 !important;
    box-shadow: 0 12px 26px rgba(90,55,27,0.16), inset 0 1px 0 rgba(255,255,255,0.22);
}
/* Fallback selected state via aria-checked on parent div */
[data-testid="column"]:has(#rec-quiz-marker) .stRadio [aria-checked="true"] label,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio [aria-checked="true"] label {
    background: linear-gradient(135deg, #9B6942, #7E4C2C) !important;
    border-color: rgba(95,54,28,0.72) !important;
    color: #FFF8EE !important;
    font-weight: 800 !important;
}
[data-testid="column"]:has(#rec-quiz-marker) .stRadio label:has(input:checked) *,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio label:has(input:checked) *,
[data-testid="column"]:has(#rec-quiz-marker) .stRadio [aria-checked="true"] label *,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio [aria-checked="true"] label * {
    color: #FFF8EE !important;
}
/* Hide the native radio input inside the label */
[data-testid="column"]:has(#rec-quiz-marker) .stRadio label input,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio label input {
    position: absolute !important;
    opacity: 0 !important;
    width: 0 !important; height: 0 !important;
    pointer-events: none !important;
}

[data-testid="column"]:has(#rec-quiz-marker-2) .stCheckbox {
    margin-top: 1.1rem !important;
    padding: 0.85rem 0.95rem !important;
    border-radius: 14px !important;
    border: 1px solid rgba(126,83,46,0.18) !important;
    background: rgba(255,253,248,0.70) !important;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.72);
}
[data-testid="column"]:has(#rec-quiz-marker-2) .stCheckbox label {
    color: var(--espresso) !important;
    font-weight: 800 !important;
    letter-spacing: 0.2px !important;
}
[data-testid="column"]:has(#rec-quiz-marker-2) .stCheckbox label span {
    color: inherit !important;
}

button[kind="primary"],
.stButton > button[kind="primary"] {
    min-height: 3.55rem !important;
    border-radius: 999px !important;
    background:
        linear-gradient(135deg, #1B0E08 0%, #5A331E 58%, #9B6B3F 100%) !important;
    border: 1px solid rgba(126,83,46,0.58) !important;
    color: #FFF8EE !important;
    letter-spacing: 3.5px !important;
    text-transform: uppercase !important;
    font-weight: 900 !important;
    box-shadow: 0 18px 38px rgba(90,55,27,0.18), inset 0 1px 0 rgba(255,255,255,0.13) !important;
}
button[kind="primary"]:hover,
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 24px 46px rgba(90,55,27,0.24), inset 0 1px 0 rgba(255,255,255,0.16) !important;
}

/* Slider inside right quiz column */
[data-testid="column"]:has(#rec-quiz-marker-2) .stSlider > div > div > div {
    background: rgba(201,168,124,0.15) !important;
}
[data-testid="column"]:has(#rec-quiz-marker-2) .stSlider [role="slider"] {
    background: var(--accent) !important;
    box-shadow: 0 0 0 4px rgba(201,168,124,0.2) !important;
}
[data-testid="column"]:has(#rec-quiz-marker-2) .stSlider > div > div > p,
[data-testid="column"]:has(#rec-quiz-marker-2) .stSlider [data-testid="stTickBarMin"],
[data-testid="column"]:has(#rec-quiz-marker-2) .stSlider [data-testid="stTickBarMax"] {
    color: rgba(255,255,255,0.3) !important;
}

/* Full-width submit button — gold shimmer */
[data-testid="stButton"]:has(button[data-testid="baseButton-primary"]) > button,
.stButton > button[kind="primary"] {
    padding: 1.1rem 2rem !important;
    font-size: 0.78rem !important; font-weight: 700 !important;
    letter-spacing: 3px !important; border-radius: 8px !important;
    background: linear-gradient(120deg, #A87C5A 0%, var(--accent) 35%, #D4B896 65%, var(--gold) 100%) !important;
    background-size: 250% auto !important;
    color: var(--espresso) !important; border: none !important;
    box-shadow: 0 8px 32px rgba(201,168,124,0.28) !important;
    text-transform: uppercase !important;
    transition: background-position 0.5s ease, transform 0.3s ease, box-shadow 0.3s ease !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 16px 48px rgba(201,168,124,0.42) !important;
    background-position: right center !important;
}
.stButton > button[kind="primary"]:active { transform: translateY(0) !important; }

/* ── Reasons Box ─────────────────────────────────────────────────────── */
.reasons-box {
    border-left: 2px solid var(--accent);
    background: rgba(255,255,255,0.03);
    border-radius: 0 10px 10px 0;
    padding: 1.25rem 1.5rem; margin: 1.75rem 0 1rem;
    animation: slideRight 0.4s ease-out 0.3s both;
}
.reasons-title {
    font-size: 0.6rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--accent) !important; margin: 0 0 0.75rem; font-weight: 700; display: block;
}
.reason-row {
    display: flex; align-items: center; gap: 0.6rem;
    font-size: 0.84rem; color: rgba(255,255,255,0.5) !important;
    margin: 0.4rem 0; line-height: 1.6;
    animation: staggerSlide 0.35s ease-out var(--d, 0.35s) both;
}
.reason-check { color: var(--accent) !important; font-weight: 800; font-size: 0.95rem; }

/* ── Badges ──────────────────────────────────────────────────────────── */
.badge-row { display: flex; gap: 0.6rem; flex-wrap: wrap; margin: 1rem 0; }
.pill-badge {
    border: 1px solid rgba(201,168,124,0.25);
    padding: 0.45rem 1rem; font-size: 0.72rem;
    color: rgba(255,255,255,0.58) !important;
    background: rgba(201,168,124,0.07);
    font-weight: 600; letter-spacing: 0.5px;
    display: inline-flex; align-items: center; gap: 0.4rem;
    border-radius: 20px;
    animation: fadeIn 0.4s ease-out 0.5s both;
    transition: all 0.3s ease;
}
.pill-badge:hover {
    background: rgba(201,168,124,0.17) !important;
    border-color: var(--accent) !important;
    color: #FFFFFF !important;
    box-shadow: 0 4px 20px rgba(201,168,124,0.25);
    transform: translateY(-2px);
}

/* ── Tip banner ──────────────────────────────────────────────────────── */
.tip-banner {
    padding: 1rem 1.5rem;
    background: rgba(201,168,124,0.06);
    border-left: 2px solid var(--accent);
    border-radius: 0 8px 8px 0;
    font-size: 0.8rem; color: rgba(255,255,255,0.42) !important;
    margin: 1.25rem 0; line-height: 1.7;
    animation: fadeIn 0.4s ease-out 0.5s both;
}

/* ── Homebrew guide ──────────────────────────────────────────────────── */
.homebrew-guide {
    background: rgba(0,0,0,0.35);
    border: 1px solid rgba(201,168,124,0.1);
    border-radius: 10px;
    padding: 1.5rem; margin: 1.25rem 0;
    font-family: 'Courier New', monospace;
    font-size: 0.8rem; line-height: 1.9;
    color: rgba(255,255,255,0.48) !important;
    white-space: pre-wrap; word-wrap: break-word;
    animation: fadeIn 0.5s ease-out 0.4s both;
    box-shadow: inset 0 0 40px rgba(0,0,0,0.2);
}
.homebrew-guide strong {
    color: var(--accent) !important; font-weight: 700; font-family: 'Satoshi', sans-serif;
}

/* ── Steam ───────────────────────────────────────────────────────────── */
.steam-container {
    display: flex; justify-content: center; gap: 9px;
    height: 44px; margin-bottom: -6px; align-items: flex-end;
}
.steam-line {
    width: 3px; border-radius: 3px;
    background: linear-gradient(to top, rgba(255,255,255,0.65), transparent);
    animation: steamRise 2.4s ease-in-out infinite;
    transform-origin: bottom center;
}
.steam-line:nth-child(1) { height: 28px; animation-delay: 0s;    }
.steam-line:nth-child(2) { height: 40px; animation-delay: 0.65s; }
.steam-line:nth-child(3) { height: 22px; animation-delay: 1.3s;  }

/* ══════════════════════════════════════════════════════════════════════════
   DRINK VISUALIZATION (CUP & GLASS)
══════════════════════════════════════════════════════════════════════════ */
.drink-viz {
    display: flex; justify-content: center; align-items: flex-end;
    margin: 1.5rem 0; padding: 1.5rem 0;
    animation: fadeIn 0.6s ease-out 0.4s both;
}

/* ── Cup Visualization ──────────────────────────────────────────────── */
.cup-container {
    position: relative; display: flex; flex-direction: column;
    align-items: center; gap: 0.5rem;
}

.cup-shape {
    width: 120px; height: 160px;
    background: linear-gradient(135deg, #F5EFE6 0%, #E8DCC8 100%);
    border: 2px solid #8B7355;
    border-radius: 0 0 20px 20px;
    box-shadow: inset -2px -2px 8px rgba(0, 0, 0, 0.1),
                0 4px 12px rgba(0, 0, 0, 0.15);
    display: flex; flex-direction: column;
    overflow: hidden;
    position: relative;
}

.cup-shape::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 8px;
    background: linear-gradient(135deg, #8B7355, #6B5345);
    border-radius: 50% 50% 0 0;
}

.cup-handle {
    position: absolute;
    right: -24px; top: 20px;
    width: 32px; height: 60px;
    border: 2.5px solid #8B7355;
    border-radius: 0 20px 20px 0;
    border-left: none;
}

.cup-label {
    font-size: 0.75rem; font-weight: 700;
    color: #1C1C1C; letter-spacing: 0.5px;
    margin-top: 0.75rem; text-align: center;
    text-transform: uppercase;
}

/* ── Glass Visualization ────────────────────────────────────────────── */
.glass-container {
    position: relative; display: flex; flex-direction: column;
    align-items: center; gap: 0.5rem;
}

.glass-shape {
    width: 100px; height: 160px;
    background: linear-gradient(135deg, #E8F1F8 0%, #D4E6F0 100%);
    border: 2px solid #4A7BA7;
    border-radius: 0 0 16px 16px;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
    box-shadow: inset -1px -1px 6px rgba(0, 0, 0, 0.08),
                0 4px 12px rgba(74, 123, 167, 0.15);
    display: flex; flex-direction: column;
    overflow: hidden;
    position: relative;
}

.glass-shape::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 4px;
    background: linear-gradient(135deg, #4A7BA7, #2E5266);
}

.ice-cubes {
    height: 20px;
    background: linear-gradient(135deg, #D4F1FF, #B3E5FC);
    color: #66BBFF;
    font-size: 0.8rem;
    display: flex; justify-content: center; align-items: center;
    gap: 4px;
    letter-spacing: 2px;
    border-bottom: 1px solid rgba(66, 187, 255, 0.3);
}

.glass-label {
    font-size: 0.75rem; font-weight: 700;
    color: #1C1C1C; letter-spacing: 0.5px;
    margin-top: 0.75rem; text-align: center;
    text-transform: uppercase;
}

/* ── Layers (Coffee, Milk, Foam, Sugar) ─────────────────────────── */
.layer {
    flex: 1;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.6rem;
    font-weight: 600;
    color: var(--white);
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: opacity 0.3s ease;
    letter-spacing: 0.3px;
    animation: liquidFill 0.9s cubic-bezier(0.34,1,0.64,1) var(--d, 0.5s) both;
}

.layer-label {
    display: inline-block;
    line-height: 1.2;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    animation: fadeIn 0.5s ease-out;
}

.layer-coffee {
    background: linear-gradient(135deg, #4A2511 0%, #6B4423 100%);
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.2);
}

.layer-milk {
    background: linear-gradient(135deg, #E8D4B8 0%, #D9B8A0 100%);
    color: #4A2511;
}

.layer-milk .layer-label {
    text-shadow: 0 1px 2px rgba(255, 255, 255, 0.3);
}

.layer-foam {
    background: linear-gradient(135deg, #F5E6D3 0%, #EDD5B8 100%);
    color: #8B5A2B;
    border-top: 1px solid rgba(255, 255, 255, 0.6);
}

.layer-foam .layer-label {
    text-shadow: 0 1px 1px rgba(255, 255, 255, 0.5);
}

.layer-sugar {
    background: linear-gradient(135deg, #B8936A 0%, #9F7E55 100%);
    color: var(--white);
    border-top: 1px solid rgba(255, 255, 255, 0.4);
}

.layer::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 1px;
    background: rgba(255, 255, 255, 0.2);
}

/* ══════════════════════════════════════════════════════════════════════════
   INSIGHTS / DID YOU KNOW
══════════════════════════════════════════════════════════════════════════ */
.stat-strip {
    display: flex; border-bottom: 1px solid var(--border);
    margin-bottom: 3rem;
}
.stat-block {
    flex: 1; padding: 2rem 1.5rem; text-align: center;
    border-right: 1px solid var(--border);
    animation: fadeInUp 0.6s ease-out var(--d,0s) both;
    transition: background 0.7s ease, border-color 0.7s ease, transform 0.7s ease, box-shadow 0.7s ease;
}
.stat-block:last-child { border-right: none; }
.stat-block:hover { background: var(--cream); }
.stat-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.5rem; font-weight: 400;
    background: linear-gradient(135deg, var(--accent) 0%, var(--espresso) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; line-height: 1; margin: 0 0 0.3rem;
    display: block;
    transition: font-size 0.8s ease, transform 0.8s ease;
}
.stat-label {
    font-size: 0.65rem; letter-spacing: 2.5px; text-transform: uppercase;
    color: var(--muted); font-family: 'Satoshi', sans-serif;
    transition: color 0.8s ease, text-shadow 0.8s ease;
}


/* ══════════════════════════════════════════════════════════════════════════
   INSIGHTS PAGE  (.ip-*)
══════════════════════════════════════════════════════════════════════════ */

/* Hero banner */
.ip-hero {
    background:
        radial-gradient(ellipse 55% 60% at 95% 5%, rgba(201,168,124,0.13), transparent 55%),
        linear-gradient(140deg, #1C110A 0%, #2E1B10 55%, #150D07 100%);
    border-radius: 14px;
    padding: 2.8rem 2.6rem 2.2rem;
    margin-bottom: 1.4rem;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.5s ease-out both;
}
.ip-hero h1 {
    color: #FFF8EE !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.6rem, 5.5vw, 5rem) !important;
    font-weight: 700 !important;
    line-height: 0.91 !important;
    letter-spacing: -0.01em !important;
    margin: 0.3rem 0 0.75rem !important;
}
.ip-hero .ip-hero-sub {
    color: rgba(255,248,238,0.52);
    font-size: 0.9rem;
    line-height: 1.65;
    white-space: nowrap;
    margin: 0 0 2rem;
}
.ip-hero-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    border-top: 1px solid rgba(255,255,255,0.08);
    padding-top: 1.4rem;
    gap: 0;
}
.ip-hero-stat {
    padding: 0 1.4rem;
    border-right: 1px solid rgba(255,255,255,0.08);
}
.ip-hero-stat:first-child { padding-left: 0; }
.ip-hero-stat:last-child  { border-right: none; }
.ip-hero-stat strong {
    display: block;
    color: var(--accent);
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 3.5vw, 3rem);
    font-weight: 700;
    line-height: 1;
}
.ip-hero-stat span {
    display: block;
    color: rgba(255,248,238,0.44);
    font-size: 0.63rem;
    letter-spacing: 1.4px;
    text-transform: uppercase;
    font-weight: 700;
    margin-top: 0.38rem;
}

/* Explorer section header */
.ip-explorer-head {
    margin: 0.4rem 0 0.9rem;
    padding-bottom: 0.65rem;
    border-bottom: 1px solid rgba(126,83,46,0.12);
}
.ip-explorer-head h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.8rem, 3vw, 2.8rem) !important;
    font-weight: 700 !important;
    line-height: 0.95 !important;
    margin: 0.15rem 0 0 !important;
}
.ip-explorer-head p {
    color: rgba(24,14,8,0.48);
    font-size: 0.84rem;
    margin: 0.35rem 0 0;
}

/* Per-chart card header */
.ip-chart-head {
    margin-bottom: 0.5rem;
}
.ip-chart-kicker {
    display: block;
    font-size: 0.54rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: rgba(24,14,8,0.36);
    font-weight: 800;
    margin-bottom: 0.15rem;
}
.ip-chart-title {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    margin: 0 0 0.55rem !important;
    line-height: 1.15 !important;
}

/* Findings section */
.ip-findings-head {
    margin: 1.6rem 0 1rem;
    padding-bottom: 0.65rem;
    border-bottom: 1px solid rgba(126,83,46,0.12);
}
.ip-findings-head h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.8rem, 3vw, 2.8rem) !important;
    font-weight: 700 !important;
    line-height: 0.95 !important;
    margin: 0.15rem 0 0 !important;
}

/* Finding cards in 2-col grid */
.ip-findings-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.9rem;
    margin-bottom: 1.5rem;
}
.ip-finding-card {
    background: #FFF9F3;
    border: 1px solid rgba(126,83,46,0.11);
    border-radius: 10px;
    padding: 1.2rem 1.3rem 1.1rem;
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
    transition: border-color 0.2s, box-shadow 0.2s;
    animation: fadeInUp 0.45s ease-out var(--d,0s) both;
}
.ip-finding-card:hover {
    border-color: rgba(126,83,46,0.22);
    box-shadow: 0 6px 22px rgba(90,55,27,0.08);
}
.ip-fn-num {
    font-size: 0.56rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 800;
}
.ip-finding-card h3 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.2rem !important;
    font-weight: 700 !important;
    line-height: 1.15 !important;
    margin: 0 !important;
}
.ip-finding-card p {
    color: rgba(24,14,8,0.60);
    font-size: 0.84rem;
    line-height: 1.62;
    margin: 0;
    flex: 1;
}
.ip-finding-card p strong { color: var(--espresso); }
.ip-fn-badge {
    display: inline-block;
    background: rgba(201,168,124,0.16);
    color: var(--espresso);
    font-size: 0.66rem;
    font-weight: 700;
    letter-spacing: 0.4px;
    padding: 0.26rem 0.65rem;
    border-radius: 999px;
    border: 1px solid rgba(201,168,124,0.28);
    align-self: flex-start;
    margin-top: 0.15rem;
}

/* Evidence strip (dark horizontal bar) */
.ip-evidence-strip {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    background: var(--espresso);
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 1.5rem;
}
.ip-ev-item {
    padding: 1.25rem 1.1rem;
    border-right: 1px solid rgba(255,255,255,0.07);
    display: flex;
    flex-direction: column;
    gap: 0.22rem;
}
.ip-ev-item:last-child { border-right: none; }
.ip-ev-item span {
    display: block;
    font-size: 0.52rem;
    letter-spacing: 1.6px;
    text-transform: uppercase;
    color: rgba(201,168,124,0.55);
    font-weight: 800;
}
.ip-ev-item strong {
    display: block;
    color: #FFF8EE;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.35rem;
    font-weight: 700;
    line-height: 1;
}
.ip-ev-item em {
    display: block;
    font-style: normal;
    color: rgba(255,248,238,0.44);
    font-size: 0.72rem;
    line-height: 1.3;
}

/* Model notes card */
.ip-model-card {
    background: #FFF9F3;
    border: 1px solid rgba(126,83,46,0.11);
    border-radius: 10px;
    padding: 1.3rem 1.4rem;
    margin-bottom: 1.5rem;
}
.ip-model-card h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.5rem, 2.5vw, 2.2rem) !important;
    font-weight: 700 !important;
    line-height: 1 !important;
    margin: 0.1rem 0 0.9rem !important;
}
.ip-model-list { list-style: none; padding: 0; margin: 0; }
.ip-model-item {
    padding: 0.75rem 0 0.75rem 1.05rem;
    border-bottom: 1px solid rgba(126,83,46,0.08);
    color: rgba(24,14,8,0.65);
    font-size: 0.86rem;
    line-height: 1.6;
    position: relative;
    animation: fadeInUp 0.45s ease-out var(--d,0s) both;
}
.ip-model-item::before {
    content: '';
    position: absolute;
    left: 0; top: 50%;
    transform: translateY(-50%);
    width: 3px; height: 55%;
    background: var(--gold);
    border-radius: 2px;
}
.ip-model-item:last-child { border-bottom: none; }

/* Legacy selectors kept for safety */
.ip-shell { padding: 0.5rem 0 1.5rem; }
.ip-section-head { margin: 1.5rem 0 1.1rem; }
.ip-section-head h2 { font-size: 1.8rem !important; }
.ip-finding-body strong { color: var(--espresso); }
.ip-model-section { margin-top: 1.5rem; }

/* ══════════════════════════════════════════════════════════════════════════
   PROFILE PAGE  (.pp-*)
══════════════════════════════════════════════════════════════════════════ */

/* Hero card */
.pp-hero-card {
    background: #FFF9F3;
    border: 1px solid rgba(126,83,46,0.13);
    border-radius: 14px;
    padding: 2rem 2.2rem 1.8rem;
    margin-bottom: 1.1rem;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 1.5rem;
    animation: fadeInUp 0.45s ease-out both;
}
.pp-hero-copy h1 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.4rem, 5vw, 4.4rem) !important;
    font-weight: 700 !important;
    line-height: 0.93 !important;
    margin: 0.25rem 0 0.6rem !important;
}
.pp-hero-copy > p {
    color: rgba(24,14,8,0.50);
    font-size: 0.9rem;
    line-height: 1.65;
    margin: 0;
    max-width: 580px;
}
.pp-badge {
    flex-shrink: 0;
    background: var(--espresso);
    color: #FFF8EE;
    border-radius: 9px;
    padding: 0.7rem 1.1rem;
    text-align: center;
    min-width: 130px;
}
.pp-badge .pp-badge-label {
    display: block;
    font-size: 0.54rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: rgba(201,168,124,0.65);
    font-weight: 800;
}
.pp-badge strong {
    display: block;
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.1rem;
    font-weight: 700;
    text-transform: capitalize;
    margin-top: 0.2rem;
    color: #FFF8EE;
    line-height: 1.2;
}
.pp-badge em {
    display: block;
    font-style: normal;
    color: rgba(255,248,238,0.50);
    font-size: 0.78rem;
    margin-top: 0.2rem;
}

/* 4-stat row */
.pp-stat-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.85rem;
    margin-bottom: 1.1rem;
}
.pp-stat-card {
    background: #FFF9F3;
    border: 1px solid rgba(126,83,46,0.12);
    border-radius: 10px;
    padding: 1.1rem 1.15rem 1rem;
    animation: fadeInUp 0.5s ease-out both;
}
.pp-stat-card .pp-sc-label {
    display: block;
    font-size: 0.56rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: rgba(24,14,8,0.38);
    font-weight: 800;
    margin-bottom: 0.3rem;
}
.pp-stat-card strong {
    display: block;
    color: var(--espresso);
    font-size: 1.06rem;
    font-weight: 700;
    text-transform: capitalize;
    margin-bottom: 0.28rem;
    line-height: 1.2;
}
.pp-stat-card p {
    color: rgba(24,14,8,0.40);
    font-size: 0.7rem;
    line-height: 1.45;
    margin: 0;
}

/* Two-column grid */
.pp-grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;
}

/* Generic section card */
.pp-section-card {
    background: #FFF9F3;
    border: 1px solid rgba(126,83,46,0.12);
    border-radius: 10px;
    padding: 1.25rem 1.4rem 1.15rem;
}
.pp-section-card .pp-sc-kicker,
.pp-sc-kicker {
    display: block;
    font-size: 0.56rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: rgba(24,14,8,0.38);
    font-weight: 800;
    margin-bottom: 0.2rem;
}
.pp-section-card h2,
.pp-section-h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.45rem, 2.5vw, 2.05rem) !important;
    font-weight: 700 !important;
    line-height: 1.05 !important;
    margin: 0.1rem 0 0.9rem !important;
}

/* Taste tags */
.pp-taste-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}
.pp-taste-tag {
    padding: 0.52rem 0.8rem;
    border-radius: 7px;
    background: rgba(255,243,232,0.9);
    border: 1px solid rgba(126,83,46,0.09);
}
.pp-taste-tag span {
    display: block;
    font-size: 0.54rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: rgba(24,14,8,0.38);
    font-weight: 800;
}
.pp-taste-tag strong {
    display: block;
    font-size: 0.87rem;
    font-weight: 600;
    color: var(--espresso);
    text-transform: capitalize;
    margin-top: 0.1rem;
}

/* Exploration */
.pp-exploration-bar {
    height: 5px;
    background: rgba(126,83,46,0.12);
    border-radius: 999px;
    margin: 0.55rem 0 1rem;
    overflow: hidden;
}
.pp-exploration-bar span {
    display: block;
    height: 100%;
    background: linear-gradient(90deg, var(--gold), var(--accent));
    border-radius: 999px;
    transition: width 0.8s cubic-bezier(0.22,1,0.36,1);
}
.pp-expl-metrics {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.6rem;
}
.pp-expl-metric {
    background: rgba(255,243,232,0.7);
    border: 1px solid rgba(126,83,46,0.09);
    border-radius: 8px;
    padding: 0.65rem 0.6rem;
}
.pp-expl-metric span {
    display: block;
    font-size: 0.54rem;
    letter-spacing: 1.3px;
    text-transform: uppercase;
    color: rgba(24,14,8,0.38);
    font-weight: 800;
    margin-bottom: 0.22rem;
}
.pp-expl-metric strong {
    display: block;
    font-size: 0.94rem;
    color: var(--espresso);
    font-weight: 700;
    text-transform: capitalize;
}

/* Drink tile */
.pp-drink-tile {
    background: #FFF9F3;
    border: 1px solid rgba(126,83,46,0.11);
    border-radius: 10px;
    padding: 1rem 0.5rem 0.85rem;
    text-align: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.pp-drink-tile:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 24px rgba(90,55,27,0.10);
}
.pp-drink-tile strong {
    display: block;
    color: var(--espresso);
    font-size: 0.83rem;
    font-weight: 700;
    margin-top: 0.5rem;
    line-height: 1.25;
}
.pp-drink-tile p {
    color: rgba(24,14,8,0.43);
    font-size: 0.7rem;
    margin: 0.18rem 0 0;
}

/* Pattern list (habit insights) */
.pp-pattern-list { display: flex; flex-direction: column; gap: 0.7rem; }
.pp-pattern-item {
    padding: 0.8rem 1rem 0.8rem 1.05rem;
    background: rgba(255,243,232,0.65);
    border: 1px solid rgba(126,83,46,0.09);
    border-radius: 8px;
}
.pp-pattern-item .pp-pi-kicker {
    display: block;
    font-size: 0.52rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 800;
    margin-bottom: 0.3rem;
}
.pp-pattern-item p {
    color: rgba(24,14,8,0.64);
    font-size: 0.85rem;
    line-height: 1.6;
    margin: 0;
}

/* Profile dashboard refresh: editorial coffee personality board */
.pp-dashboard {
    width: calc(100% + 2rem);
    margin: 0 -1rem;
    padding: 0.65rem 0.9rem 1.4rem;
    background:
        radial-gradient(circle at 9% 0%, rgba(236,205,154,0.36), transparent 24%),
        radial-gradient(circle at 100% 12%, rgba(126,83,46,0.15), transparent 24%),
        linear-gradient(180deg, #F3E5CA 0%, #EFE0C4 48%, #F7EDDC 100%);
    border: 1px solid rgba(126,83,46,0.10);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.60);
}
.pp-dashboard .pp-hero-card {
    background:
        radial-gradient(circle at 7% 12%, rgba(255,248,230,0.16), transparent 28%),
        linear-gradient(90deg, #8C633C 0%, #B9905D 48%, #D6BB86 100%);
    border-radius: 10px;
    border-color: rgba(90,55,27,0.24);
    padding: 0.9rem 1rem 0.95rem;
    margin-bottom: 0.85rem;
    align-items: flex-start;
    min-height: 150px;
    box-shadow: 0 18px 42px rgba(90,55,27,0.18), inset 0 1px 0 rgba(255,255,255,0.18);
}
.pp-dashboard .pp-hero-copy h1 {
    font-size: clamp(2.6rem, 4.2vw, 4.5rem) !important;
    letter-spacing: 0 !important;
    margin: 0.1rem 0 0.45rem !important;
    color: rgba(255,248,234,0.88) !important;
}
.pp-dashboard .pp-hero-copy > p {
    color: rgba(255,248,234,0.80);
    max-width: 850px;
    font-size: 0.88rem;
}
.pp-dashboard .pp-hero-copy .hdp-kicker {
    color: rgba(255,232,188,0.82);
}
.pp-dashboard .pp-badge {
    margin-top: -0.9rem;
    border-radius: 0 0 12px 12px;
    background: #5A341E;
    min-width: 190px;
    text-align: left;
    box-shadow: 0 14px 26px rgba(48,28,14,0.24);
}
.pp-dashboard .pp-stat-row {
    gap: 0.65rem;
    margin: -3.6rem 0 0.9rem;
    padding: 0 0.35rem;
    position: relative;
    z-index: 2;
}
.pp-dashboard .pp-stat-card,
.pp-dashboard .pp-section-card,
.pp-dashboard .pp-drink-tile,
.pp-dashboard .pp-taste-tag,
.pp-dashboard .pp-expl-metric,
.pp-dashboard .pp-pattern-item {
    background: rgba(255,249,241,0.84);
    border-color: rgba(126,83,46,0.11);
    box-shadow: 0 10px 26px rgba(90,55,27,0.055), inset 0 1px 0 rgba(255,255,255,0.70);
}
.pp-dashboard .pp-stat-card {
    border-radius: 9px;
    padding: 0.85rem 0.9rem 0.78rem;
}
.pp-dashboard .pp-stat-card strong {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.45rem;
}
.pp-dashboard .pp-grid-2 {
    gap: 0.85rem;
    margin-bottom: 0.85rem;
}
.pp-dashboard .pp-section-card {
    border-radius: 12px;
    padding: 1rem 1.1rem 1rem;
    overflow: hidden;
}
.pp-dashboard .pp-sc-kicker,
.pp-dashboard .pp-section-card .pp-sc-kicker {
    color: rgba(90,55,27,0.60);
    letter-spacing: 3px;
    font-size: 0.58rem;
}
.pp-dashboard .pp-section-card h2,
.pp-dashboard .pp-section-h2 {
    font-size: clamp(1.9rem, 3vw, 3rem) !important;
    line-height: 0.98 !important;
    margin-bottom: 0.75rem !important;
}
.pp-dashboard .pp-taste-row {
    display: grid;
    grid-template-columns: repeat(6, minmax(0, 1fr));
}
.pp-dashboard .pp-taste-tag {
    border-radius: 9px;
    padding: 0.62rem 0.72rem;
}
.pp-dashboard .pp-exploration-bar {
    height: 15px;
    background: rgba(218,188,145,0.50);
}
.pp-dashboard .pp-exploration-bar span {
    background: linear-gradient(90deg, #6B4423 0%, #B78145 65%, #E2BB73 100%);
}
.pp-filter-chips {
    display: flex;
    flex-wrap: wrap;
    gap: 0.42rem;
    margin: -0.35rem 0 0.7rem;
}
.pp-filter-chips span {
    border-radius: 999px;
    padding: 0.35rem 0.58rem;
    background: rgba(255,249,241,0.72);
    color: rgba(24,14,8,0.66);
    font-size: 0.72rem;
    font-weight: 800;
}
.pp-filter-chips span.active {
    background: #6B4423;
    color: #FFF8EE;
}
.pp-drink-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.7rem;
}
.pp-drink-grid.compact {
    grid-template-columns: repeat(5, minmax(0, 1fr));
}
.pp-dashboard .pp-drink-tile {
    border-radius: 9px;
    padding: 0.55rem 0.55rem 0.75rem;
    min-height: 250px;
    justify-content: flex-start;
}
.pp-dashboard .pp-drink-grid.compact .pp-drink-tile {
    min-height: 205px;
}
.pp-cup-stage {
    width: 100%;
    min-height: 178px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 9px;
    margin-bottom: 0.5rem;
    background:
        radial-gradient(ellipse at 50% 82%, rgba(90,55,27,0.14), transparent 44%),
        linear-gradient(135deg, #FFF8E9 0%, #E8D3AA 100%);
}
.pp-drink-grid.compact .pp-cup-stage {
    min-height: 138px;
}
.pp-dashboard .pp-drink-tile .cup-viz {
    transform: scale(0.74);
    transform-origin: center bottom;
}
.pp-dashboard .pp-drink-grid.compact .cup-viz {
    transform: scale(0.56);
}
.pp-dashboard .pp-drink-tile .cup-steam {
    display: none;
}
.pp-dashboard .pp-drink-tile .cup-mug-body,
.pp-dashboard .pp-drink-tile .cup-glass-body {
    border: 5px solid #6B4423;
    box-shadow: inset 0 0 0 3px rgba(255,255,255,0.38), 0 8px 18px rgba(90,55,27,0.10);
}
.pp-dashboard .pp-drink-tile .cup-mug-body {
    border-radius: 26px 26px 38px 38px / 24px 24px 34px 34px;
}
.pp-dashboard .pp-drink-tile .cup-glass-body {
    width: 126px;
    height: 190px;
    border-color: rgba(107,68,35,0.82);
    border-width: 4px;
    border-radius: 20px 20px 34px 34px / 12px 12px 30px 30px;
    clip-path: polygon(4% 0%, 96% 0%, 86% 100%, 14% 100%);
    box-shadow: inset 0 0 0 3px rgba(255,255,255,0.34), 0 8px 18px rgba(90,55,27,0.10);
}
.pp-dashboard .pp-drink-tile .cup-mug-body::before,
.pp-dashboard .pp-drink-tile .cup-glass-body::before,
.pp-dashboard .pp-drink-tile .cup-mug-body::after,
.pp-dashboard .pp-drink-tile .cup-glass-body::after,
.pp-dashboard .pp-drink-tile .cup-mug-shine,
.pp-dashboard .pp-drink-tile .cup-glass-shine,
.pp-dashboard .pp-drink-tile .cup-glass-straw {
    display: none;
}
.pp-dashboard .pp-drink-tile .cup-glass .cup-steam,
.pp-dashboard .pp-drink-tile .cup-glass .cup-mug-handle {
    display: none !important;
}
.pp-dashboard .pp-drink-tile .cup-mug-handle {
    right: -29px;
    top: 48px;
    width: 52px;
    height: 62px;
    border: 5px solid #6B4423;
    border-left: 0;
    border-radius: 0 38px 38px 0;
    background: transparent;
}
.pp-dashboard .pp-drink-tile .cup-mug-saucer,
.pp-dashboard .pp-drink-tile .cup-glass-base {
    width: 160px;
    height: 22px;
    background: radial-gradient(ellipse at center, rgba(90,55,27,0.22), rgba(90,55,27,0.08) 52%, transparent 74%);
    border: 0;
    filter: none;
    margin-top: 2px;
}
.pp-dashboard .pp-drink-tile .cup-glass-base {
    width: 145px;
    margin-top: 6px;
}
.pp-dashboard .pp-drink-tile .cup-composition-labels,
.pp-dashboard .pp-drink-tile .cup-mug-layers,
.pp-dashboard .pp-drink-tile .cup-glass-layers {
    display: none;
}
.pp-dashboard .pp-drink-tile strong {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.28rem;
    color: var(--espresso);
}
.pp-dashboard .pp-drink-tile p {
    color: rgba(24,14,8,0.56);
    font-weight: 700;
}
.pp-dashboard .pp-pattern-list {
    gap: 0.55rem;
    position: relative;
}
.pp-dashboard .pp-pattern-item {
    border-radius: 12px;
    padding: 0.72rem 0.85rem;
    display: grid;
    grid-template-columns: 42px 1fr;
    gap: 0.72rem;
    align-items: start;
    background:
        linear-gradient(90deg, rgba(107,68,35,0.10), rgba(255,249,241,0.88));
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.72), 0 8px 20px rgba(90,55,27,0.04);
}
.pp-dashboard .pp-pattern-item:hover {
    transform: translateX(3px);
    border-color: rgba(126,83,46,0.18);
}
.pp-insight-lede {
    display: grid;
    gap: 0.25rem;
    margin: -0.2rem 0 0.75rem;
    padding: 0.85rem 0.95rem;
    border-radius: 14px;
    background:
        radial-gradient(circle at 92% 0%, rgba(226,187,115,0.34), transparent 36%),
        linear-gradient(135deg, #6B4423, #2B160C);
    box-shadow: 0 14px 28px rgba(90,55,27,0.13);
}
.pp-insight-lede span {
    color: rgba(255,248,238,0.58);
    font-size: 0.55rem;
    letter-spacing: 2.6px;
    text-transform: uppercase;
    font-weight: 900;
}
.pp-insight-lede strong {
    color: #FFF8EE;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.35rem;
    line-height: 1.08;
}
.pp-pi-index {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #6B4423;
    color: #F7DDAA;
    font-family: 'Satoshi', sans-serif;
    font-size: 0.66rem;
    font-weight: 900;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.14);
}
.pp-dashboard .pp-pattern-item .pp-pi-kicker {
    color: rgba(107,68,35,0.72);
    font-size: 0.56rem;
    letter-spacing: 2.4px;
    margin-bottom: 0.22rem;
}
.pp-dashboard .pp-pattern-item p {
    color: rgba(24,14,8,0.66);
    font-size: 0.82rem;
    line-height: 1.5;
}

.profile-subnav {
    width: min(520px, 100%);
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.45rem;
    margin: 1.35rem auto 1.15rem;
    padding: 0.35rem;
    border-radius: 999px;
    background: rgba(255,249,241,0.74);
    border: 1px solid rgba(126,83,46,0.12);
    box-shadow: 0 12px 30px rgba(90,55,27,0.06), inset 0 1px 0 rgba(255,255,255,0.80);
}
.profile-subnav a {
    min-height: 2.75rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 999px;
    text-decoration: none !important;
    color: rgba(24,14,8,0.64) !important;
    font-family: 'Satoshi', sans-serif;
    font-size: 0.72rem;
    font-weight: 900;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    transition: transform 0.2s ease, background 0.2s ease, color 0.2s ease;
}
.profile-subnav a:hover {
    transform: translateY(-1px);
    color: var(--espresso) !important;
    background: rgba(126,83,46,0.08);
}
.profile-subnav a.active {
    background: linear-gradient(135deg, #8C633C, #6B4423);
    color: #FFF8EE !important;
    box-shadow: 0 10px 22px rgba(90,55,27,0.18), inset 0 1px 0 rgba(255,255,255,0.18);
}

.profile-corner-logout {
    position: fixed;
    top: 7.4rem;
    right: 2.1rem;
    z-index: 950;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.36rem 0.5rem 0.36rem 0.4rem;
    border-radius: 999px;
    background: rgba(255,249,241,0.88);
    border: 1px solid rgba(126,83,46,0.14);
    color: var(--espresso) !important;
    text-decoration: none !important;
    box-shadow: 0 12px 28px rgba(90,55,27,0.12), inset 0 1px 0 rgba(255,255,255,0.78);
    backdrop-filter: blur(12px);
    transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
}
.profile-corner-logout:hover {
    transform: translateY(-2px);
    background: #FFF8EE;
    box-shadow: 0 16px 34px rgba(90,55,27,0.18), inset 0 1px 0 rgba(255,255,255,0.86);
}
.pcl-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #8C633C, #5A341E);
    color: #FFF8EE;
    font-family: 'Satoshi', sans-serif;
    font-size: 0.78rem;
    font-weight: 900;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.20);
}
.pcl-copy {
    display: grid;
    gap: 0.05rem;
    padding-right: 0.25rem;
}
.pcl-copy em,
.pcl-copy strong {
    font-family: 'Satoshi', sans-serif;
    line-height: 1;
}
.pcl-copy em {
    display: none;
    color: rgba(90,55,27,0.56);
    font-size: 0.52rem;
    font-style: normal;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 900;
}
.pcl-copy strong {
    color: var(--espresso);
    font-size: 0.68rem;
    letter-spacing: 0.2px;
    font-weight: 900;
}

.profile-history-page {
    width: min(1180px, 100%);
    margin: 0 auto 1.5rem;
    padding: 0.9rem;
    background:
        radial-gradient(circle at 10% 0%, rgba(236,205,154,0.32), transparent 25%),
        radial-gradient(circle at 95% 8%, rgba(126,83,46,0.13), transparent 24%),
        linear-gradient(180deg, #F3E5CA 0%, #F7EDDC 100%);
    border: 1px solid rgba(126,83,46,0.10);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.62);
}
.profile-history-hero {
    min-height: 210px;
    border-radius: 12px;
    padding: 1.15rem 1.35rem 1.35rem;
    background:
        radial-gradient(circle at 9% 12%, rgba(255,248,230,0.16), transparent 28%),
        linear-gradient(95deg, #7C5330 0%, #B58A58 55%, #D7BC86 100%);
    border: 1px solid rgba(90,55,27,0.22);
    box-shadow: 0 18px 42px rgba(90,55,27,0.16), inset 0 1px 0 rgba(255,255,255,0.18);
}
.profile-history-hero span,
.profile-history-stats span,
.profile-history-card .ph-card-top span {
    font-family: 'Satoshi', sans-serif;
    font-size: 0.58rem;
    font-weight: 900;
    letter-spacing: 3px;
    text-transform: uppercase;
}
.profile-history-hero span {
    color: rgba(255,232,188,0.86);
}
.profile-history-hero h1 {
    margin: 0.55rem 0 0.75rem !important;
    color: rgba(255,248,234,0.92) !important;
    font-family: 'Satoshi', sans-serif !important;
    font-size: clamp(2.4rem, 4.5vw, 4.6rem) !important;
    line-height: 0.98 !important;
    letter-spacing: 0 !important;
}
.profile-history-hero p {
    max-width: 760px;
    color: rgba(255,248,234,0.80);
    font-size: 0.9rem;
    line-height: 1.65;
    margin: 0;
}
.profile-history-stats {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 0.65rem;
    margin: 0.85rem 0 1rem;
    position: relative;
    z-index: 2;
}
.profile-history-stats div {
    padding: 0.82rem 0.9rem;
    border-radius: 10px;
    background: rgba(255,249,241,0.88);
    border: 1px solid rgba(126,83,46,0.11);
    box-shadow: 0 10px 26px rgba(90,55,27,0.055), inset 0 1px 0 rgba(255,255,255,0.72);
}
.profile-history-stats span {
    color: rgba(90,55,27,0.58);
    display: block;
    margin-bottom: 0.25rem;
}
.profile-history-stats strong {
    display: block;
    color: var(--espresso);
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.25rem, 2vw, 1.65rem);
    line-height: 1.05;
}
.profile-history-list {
    display: grid;
    grid-template-columns: 1fr;
    gap: 0.85rem;
}
.profile-history-card {
    position: relative;
    overflow: hidden;
    min-height: 250px;
    display: grid;
    grid-template-columns: 240px 1fr;
    gap: 1.15rem;
    align-items: stretch;
    padding: 0.85rem;
    border-radius: 14px;
    background:
        radial-gradient(circle at 0% 0%, rgba(226,187,115,0.18), transparent 28%),
        rgba(255,249,241,0.86);
    border: 1px solid rgba(126,83,46,0.12);
    box-shadow: 0 12px 30px rgba(90,55,27,0.06), inset 0 1px 0 rgba(255,255,255,0.72);
}
.ph-card-cup {
    min-height: 230px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 12px;
    background:
        radial-gradient(ellipse at 50% 82%, rgba(90,55,27,0.16), transparent 45%),
        linear-gradient(135deg, #FFF8E9 0%, #E6CEA3 100%);
}
.ph-card-cup .cup-viz {
    transform: scale(0.72);
    transform-origin: center bottom;
}
.ph-card-cup .cup-steam {
    display: none;
}
.ph-card-cup .cup-composition-labels,
.ph-card-cup .cup-mug-layers,
.ph-card-cup .cup-glass-layers {
    display: none;
}
.ph-card-body {
    min-width: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-right: 2.3rem;
}
.ph-card-top {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 0.5rem;
}
.profile-history-card .ph-card-top span {
    color: rgba(90,55,27,0.56);
}
.ph-card-top em {
    padding: 0.22rem 0.54rem;
    border-radius: 999px;
    background: #6B4423;
    color: #FFF8EE;
    font-family: 'Satoshi', sans-serif;
    font-size: 0.62rem;
    font-style: normal;
    font-weight: 900;
    letter-spacing: 0.6px;
}
.profile-history-card h2 {
    margin: 0 0 0.75rem !important;
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.8rem, 3vw, 2.7rem) !important;
    line-height: 0.98 !important;
}
.ph-chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.42rem;
}
.ph-chip-row span {
    border-radius: 999px;
    padding: 0.34rem 0.58rem;
    background: rgba(255,255,255,0.62);
    border: 1px solid rgba(126,83,46,0.10);
    color: rgba(24,14,8,0.62);
    font-family: 'Satoshi', sans-serif;
    font-size: 0.7rem;
    font-weight: 800;
}
.ph-index {
    position: absolute;
    top: 0.7rem;
    right: 0.85rem;
    color: rgba(107,68,35,0.12);
    font-family: 'Satoshi', sans-serif;
    font-size: 3.4rem;
    line-height: 1;
    font-weight: 900;
}

@media (max-width: 980px) {
    .profile-history-stats,
    .profile-history-list {
        grid-template-columns: 1fr;
    }
    .profile-history-stats {
        margin-top: 0.75rem;
    }
    .profile-history-card {
        grid-template-columns: 170px 1fr;
    }
    .ph-card-cup {
        min-height: 180px;
    }
    .ph-card-cup .cup-viz {
        transform: scale(0.56);
    }
}

@media (max-width: 640px) {
    .profile-subnav {
        width: 100%;
    }
    .profile-corner-logout {
        top: 5.5rem;
        right: 0.85rem;
        padding-right: 0.45rem;
    }
    .pcl-copy {
        display: none;
    }
    .profile-history-card {
        grid-template-columns: 1fr;
    }
    .ph-card-body {
        padding-right: 0;
    }
    .ph-index {
        font-size: 2.4rem;
    }
}

/* Section header spacing when used outside a card */
.pp-rhythm-head {
    margin-bottom: 0.65rem;
}

/* Keep old note-row for any remaining references */
.pp-note-row {
    padding: 0.8rem 0 0.8rem 1.1rem;
    border-bottom: 1px solid rgba(126,83,46,0.08);
    position: relative;
}
.pp-note-row:last-child { border-bottom: none; }
.pp-note-row::before {
    content: '';
    position: absolute;
    left: 0; top: 50%;
    transform: translateY(-50%);
    width: 3px; height: 55%;
    background: var(--gold);
    border-radius: 2px;
}
.pp-note-row p {
    color: rgba(24,14,8,0.68);
    font-size: 0.88rem;
    line-height: 1.62;
    margin: 0;
}

/* Placeholder for old .pp-hero selector (avoids errors if referenced elsewhere) */
.pp-hero {
    padding: clamp(1.5rem, 3vw, 2.5rem) clamp(1.2rem, 3vw, 2.2rem);
    background:
        radial-gradient(ellipse 60% 50% at 90% 10%, rgba(201,168,124,0.14), transparent 55%),
        linear-gradient(148deg, #1C110A 0%, #2E1B10 55%, #150D07 100%);
    border-radius: 12px;
    border: 1px solid rgba(201,168,124,0.14);
    margin-bottom: 1.5rem;
    animation: fadeInUp 0.55s ease-out both;
}
.pp-hero-copy { margin-bottom: 1.8rem; }
.pp-hero-copy h1 {
    color: #FFF8EE !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.8rem, 6vw, 5.5rem) !important;
    line-height: 0.92 !important;
    font-weight: 700 !important;
    margin: 0.3rem 0 0.75rem !important;
    letter-spacing: -0.01em !important;
}
.pp-hero-copy p {
    color: rgba(255,248,238,0.58);
    font-size: 0.9rem;
    line-height: 1.65;
    max-width: 680px;
    margin: 0;
}
.pp-hero-stats {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    border-top: 1px solid rgba(255,255,255,0.08);
    padding-top: 1.2rem;
}
.pp-hero-stat {
    padding: 0 1.2rem;
    border-right: 1px solid rgba(255,255,255,0.08);
}
.pp-hero-stat:first-child { padding-left: 0; }
.pp-hero-stat:last-child  { border-right: none; }
.pp-hero-stat strong {
    display: block;
    color: #FFF8EE;
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(1.4rem, 2.5vw, 2.2rem);
    line-height: 1;
    font-weight: 700;
}
.pp-hero-stat span {
    display: block;
    color: rgba(201,168,124,0.7);
    font-size: 0.62rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 700;
    margin-top: 0.3rem;
}

.pp-two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.2rem;
    margin-bottom: 1.5rem;
}
.pp-section {
    padding: 1.35rem;
    border: 1px solid rgba(126,83,46,0.14);
    border-radius: 10px;
    background: rgba(255,252,246,0.88);
}
.pp-section h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.8rem, 3vw, 2.8rem) !important;
    line-height: 0.92 !important;
    font-weight: 700 !important;
    margin: 0.2rem 0 1rem !important;
}

.pp-taste-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.6rem;
}
.pp-taste-pill {
    padding: 0.65rem 0.85rem;
    border-radius: 6px;
    background: rgba(255,250,242,0.9);
    border: 1px solid rgba(126,83,46,0.10);
}
.pp-taste-pill span {
    display: block;
    color: rgba(24,14,8,0.42);
    font-size: 0.58rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    font-weight: 800;
}
.pp-taste-pill strong {
    display: block;
    color: var(--espresso);
    font-size: 0.96rem;
    font-weight: 600;
    margin-top: 0.15rem;
    text-transform: capitalize;
}

.pp-exploration-bar {
    height: 6px;
    background: rgba(126,83,46,0.12);
    border-radius: 999px;
    margin: 0.5rem 0 1rem;
    overflow: hidden;
}
.pp-exploration-bar span {
    display: block;
    height: 100%;
    background: linear-gradient(90deg, var(--gold), var(--accent));
    border-radius: 999px;
    transition: width 0.8s cubic-bezier(0.22,1,0.36,1);
}
.pp-exploration-chips {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}
.pp-chip {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.55rem 0;
    border-bottom: 1px solid rgba(126,83,46,0.08);
}
.pp-chip:last-child { border-bottom: none; }
.pp-chip span {
    color: rgba(24,14,8,0.45);
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.5px;
}
.pp-chip strong {
    color: var(--espresso);
    font-size: 0.9rem;
    text-transform: capitalize;
}

.pp-brewed-head {
    margin-bottom: 0.9rem;
}
.pp-brewed-head h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.8rem, 3vw, 2.8rem) !important;
    line-height: 0.92 !important;
    font-weight: 700 !important;
    margin: 0.2rem 0 0 !important;
}
.pp-drink-card {
    padding: 1rem;
    border: 1px solid rgba(126,83,46,0.12);
    border-radius: 8px;
    background: rgba(255,252,246,0.88);
    text-align: center;
    transition: transform 0.22s ease, box-shadow 0.22s ease;
}
.pp-drink-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(90,55,27,0.10);
}
.pp-drink-card strong {
    display: block;
    color: var(--espresso);
    font-size: 0.88rem;
    font-weight: 700;
    margin-top: 0.5rem;
}
.pp-drink-card p {
    color: rgba(24,14,8,0.48);
    font-size: 0.74rem;
    margin: 0.15rem 0 0;
}

.pp-notes {
    margin-top: 1.5rem;
    padding: 1.35rem;
    border: 1px solid rgba(126,83,46,0.13);
    border-radius: 10px;
    background: rgba(255,252,246,0.88);
}
.pp-notes h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(1.8rem, 3vw, 2.8rem) !important;
    line-height: 0.92 !important;
    font-weight: 700 !important;
    margin: 0.2rem 0 1rem !important;
}
.pp-note-list { display: flex; flex-direction: column; }
.pp-note-row {
    padding: 0.8rem 0 0.8rem 1.1rem;
    border-bottom: 1px solid rgba(126,83,46,0.08);
    position: relative;
    animation: fadeInUp 0.45s ease-out both;
}
.pp-note-row:last-child { border-bottom: none; }
.pp-note-row::before {
    content: '';
    position: absolute;
    left: 0; top: 50%;
    transform: translateY(-50%);
    width: 3px; height: 55%;
    background: var(--gold);
    border-radius: 2px;
}
.pp-note-row p {
    color: rgba(24,14,8,0.68);
    font-size: 0.88rem;
    line-height: 1.62;
    margin: 0;
}

/* ══════════════════════════════════════════════════════════════════════════
   HOME — CARD GRID LAYOUT  (pure CSS grid, no Streamlit columns)
══════════════════════════════════════════════════════════════════════════ */
.home-grid {
    display: grid;
    grid-template-columns: 1.15fr 2fr;
    gap: 10px;
}
.home-grid-right {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.home-grid-top {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
}
.hc-insights { height: 510px; }
.hc-stats,
.hc-tip      { height: 310px; }
.hc-fact     { height: 190px; }

/* ══════════════════════════════════════════════════════════════════════════
   HOME — CHIC MOSAIC CARD GRID
══════════════════════════════════════════════════════════════════════════ */
/* Flex layout: content sits at the bottom naturally — no position:absolute needed */
.home-card {
    position: relative;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    text-decoration: none;
    cursor: default;
    border: 1px solid rgba(201,168,124,0.14);
    border-radius: 16px;
    transition:
        transform      0.75s cubic-bezier(0.34, 1.1, 0.64, 1),
        box-shadow     0.75s ease,
        border-color   0.45s ease;
    animation: cardSlideUp 1s cubic-bezier(0.22, 1, 0.36, 1) both;
}
a.home-card {
    cursor: pointer !important;
    text-decoration: none !important;
    color: #FFFFFF !important;
}

/* Staggered entrance */
.hc-insights { animation-delay: 0.06s; }
.hc-stats    { animation-delay: 0.14s; }
.hc-tip      { animation-delay: 0.22s; }
.hc-fact     { animation-delay: 0.30s; }

/* "Lit from within" radial backgrounds */
.hc-insights { background: radial-gradient(ellipse 80% 60% at 20% 25%, #3D1C0A 0%, #0F0604 70%); }
.hc-stats    { background: radial-gradient(ellipse 80% 60% at 80% 20%, #3A1A08 0%, #0C0503 70%); }
.hc-tip      { background: radial-gradient(ellipse 80% 60% at 20% 80%, #361808 0%, #0C0503 70%); }
.hc-fact     { background: radial-gradient(ellipse 80% 60% at 75% 50%, #3A1A08 0%, #0D0503 70%); }

/* Hover: lift + warm glow */
.home-card:hover {
    transform: translateY(-8px) scale(1.010);
    box-shadow: 0 32px 72px rgba(0,0,0,0.5), 0 0 0 1px rgba(201,168,124,0.30);
    border-color: rgba(201,168,124,0.35);
}
.home-card.hc-static-tip,
.home-card.hc-static-fact {
    cursor: default !important;
}
.home-card.hc-static-tip:hover,
.home-card.hc-static-fact:hover {
    transform: none;
    box-shadow: none;
    border-color: rgba(201,168,124,0.14);
}

/* Gold hairline at top */
.home-card::before {
    content: '';
    position: absolute;
    top: 0; left: 8%; right: 8%; height: 1px;
    background: linear-gradient(90deg, transparent, rgba(201,168,124,0.60) 50%, transparent);
    z-index: 3; pointer-events: none;
}

/* Gradient scrim behind text (absolutely positioned, not a flex child) */
.home-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.18) 45%, transparent 72%);
    pointer-events: none;
    border-radius: inherit;
    z-index: 1;
}

/* Content block — in normal flex flow, sits at bottom via justify-content: flex-end */
.hc-inner {
    padding: 1.6rem 1.8rem;
    position: relative;
    z-index: 2;
    flex-shrink: 0;
}

/* Label: gold leading rule */
.hc-label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'Satoshi', sans-serif;
    font-size: 0.52rem;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: var(--accent) !important;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.hc-label::before {
    content: '';
    display: inline-block;
    width: 16px; height: 1px;
    background: var(--accent);
    flex-shrink: 0;
}

/* Title: elegant thin serif */
.hc-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.6rem !important;
    font-weight: 300 !important;
    color: #FFFFFF !important;
    line-height: 1.08 !important;
    margin: 0 0 0.4rem !important;
    letter-spacing: 0.4px !important;
}

/* Large sans-serif stat number */
.hc-stat-num {
    display: block;
    font-family: 'Satoshi', sans-serif !important;
    font-size: 3.8rem !important;
    font-weight: 800 !important;
    color: #FFFFFF !important;
    line-height: 1 !important;
    letter-spacing: -2px !important;
    margin-bottom: 0.2rem;
}
.hc-stat-unit {
    display: block;
    font-family: 'Satoshi', sans-serif;
    font-size: 0.65rem;
    font-weight: 500;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(255,255,255,0.38) !important;
    margin-bottom: 0.6rem;
}

.hc-sub {
    font-family: 'Satoshi', sans-serif;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.40) !important;
    margin: 0;
    line-height: 1.55;
    letter-spacing: 0.2px;
}

/* Arrow: hollow → filled gold on hover */
.hc-arrow {
    position: absolute;
    top: 1.3rem; right: 1.3rem;
    width: 32px; height: 32px;
    border-radius: 50%;
    border: 1px solid rgba(201,168,124,0.28);
    background: transparent;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.78rem;
    color: rgba(201,168,124,0.50);
    z-index: 4;
    transition: background 0.25s ease, border-color 0.25s ease, color 0.25s ease,
                transform 0.3s cubic-bezier(0.34,1.2,0.64,1);
}
a.home-card:hover .hc-arrow {
    background: var(--accent);
    border-color: var(--accent);
    color: #0A0A0A;
    transform: translate(2px, -2px) rotate(45deg);
}

/* Per-card title tweaks */
.hc-insights .hc-title { font-size: 3.2rem !important; }
.hc-fact .hc-title {
    font-size: 1.1rem !important;
    font-weight: 400 !important;
    line-height: 1.55 !important;
    letter-spacing: 0.1px !important;
}
.hc-fact .hc-sub {
    max-width: 520px;
    margin-top: 0.45rem;
}

/* ══════════════════════════════════════════════════════════════════════════
   HOME — ROWA-STYLE CTA BAND
══════════════════════════════════════════════════════════════════════════ */
.home-cta-tagline {
    font-family: 'Satoshi', sans-serif !important;
    font-size: 1.65rem !important;
    font-weight: 700 !important;
    line-height: 1.28 !important;
    color: var(--text) !important;
    margin: 2.75rem 0 0 !important;
    letter-spacing: -0.2px !important;
    transition: color 0.6s ease, transform 0.6s ease, opacity 0.6s ease;
}
.home-cta-desc {
    font-family: 'Satoshi', 'Satoshi Placeholder', sans-serif !important;
    font-size: 1.65rem !important;
    font-weight: 700 !important;
    line-height: 1.28 !important;
    letter-spacing: -0.2px !important;
    color: var(--text) !important;
    margin: 2.75rem 0 0 !important;
    text-align: right !important;
    transition: color 0.6s ease, transform 0.6s ease, opacity 0.6s ease;
}

/* ── Page fade overlay — covers viewport on pill click ── */
#pill-expand-circle {
    position: fixed;
    left: 50%;
    top: 50%;
    width: 160vmax;
    height: 160vmax;
    margin-left: -80vmax;
    margin-top: -80vmax;
    border-radius: 50%;
    background:
        radial-gradient(circle at center, rgba(201,168,124,0.18) 0%, rgba(10,10,10,0.96) 42%, #0A0A0A 72%);
    opacity: 0;
    pointer-events: none;
    z-index: 9999;
    transform: scale(0.02);
    transition:
        opacity 0.18s ease,
        transform 0.72s cubic-bezier(0.18, 0.92, 0.22, 1);
}
#pill-expand-circle.zooming {
    opacity: 1;
    transform: scale(1);
    pointer-events: all;
}

/* ── Rowa expanding pill — large circle at rest, unfolds on hover ── */
.rowa-pill-outer {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 2rem;
}

/* Resting: wide pill showing text, icon hidden */
.rowa-pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    text-decoration: none !important;
    background: #0A0A0A;
    border-radius: 9999px !important;
    width: 310px;
    height: 76px;
    overflow: hidden;
    white-space: nowrap;
    cursor: pointer;
    padding: 0 2rem;
    box-shadow: 0 6px 32px rgba(0,0,0,0.32);
    /* Force GPU compositing so border-radius clips overflow correctly */
    transform: translateZ(0);
    -webkit-mask-image: -webkit-radial-gradient(white, black);
    transition:
        width      0.55s cubic-bezier(0.34, 1.1, 0.64, 1),
        padding    0.45s cubic-bezier(0.34, 1.1, 0.64, 1),
        box-shadow 0.28s ease;
}

/* Hover: icon slides in from left */
.rowa-pill:hover {
    width: 390px;
    padding: 0 2rem 0 0;
    box-shadow: 0 12px 48px rgba(0,0,0,0.40);
    border-radius: 9999px !important;
}

/* Icon — collapsed at rest, slides in on hover */
.rowa-pill-icon {
    width: 0;
    height: 50px;
    border-radius: 50%;
    flex-shrink: 0;
    overflow: hidden;
    margin: 0;
    background-color: #3A1E0D;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    transition:
        width  0.8s cubic-bezier(0.34, 1.1, 0.64, 1),
        margin 0.8s cubic-bezier(0.34, 1.1, 0.64, 1);
}

.rowa-pill:hover .rowa-pill-icon {
    width: 50px;
    margin: 11px 12px 11px 11px;
}

/* Text — always visible */
.rowa-pill-text {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.45rem;
    font-weight: 600;
    font-style: italic;
    letter-spacing: 1.5px;
    color: #FFFFFF;
    white-space: nowrap;
    text-decoration: none !important;
}

/* ══════════════════════════════════════════════════════════════════════════
   MODE SELECTION PAGE
══════════════════════════════════════════════════════════════════════════ */
.mode-select-page {
    width: calc(100% + 6rem);
    margin-left: -3rem;
    min-height: 90vh;
    background: radial-gradient(circle at top, rgba(201,168,124,0.08), transparent 28%), #0A0502;
    display: flex; flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2.5rem 0 4rem;
    animation: recommendZoomIn 0.65s cubic-bezier(0.22, 1, 0.36, 1) both;
}
.mode-select-hdr {
    text-align: center;
    padding: 1rem 2rem 2rem;
    max-width: 980px;
}
.mode-select-eyebrow {
    font-size: 0.6rem; letter-spacing: 5px; text-transform: uppercase;
    color: var(--accent); display: block; margin-bottom: 1rem;
    font-family: 'Satoshi', sans-serif;
}
.mode-select-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.4rem, 5vw, 4.2rem) !important;
    font-weight: 300 !important; color: #FFFFFF !important;
    letter-spacing: 4px; margin: 0 0 0.8rem !important;
    text-transform: uppercase;
}
.mode-select-sub {
    font-size: 0.72rem; letter-spacing: 2.5px; text-transform: uppercase;
    color: rgba(255,255,255,0.35); font-family: 'Satoshi', sans-serif; margin: 0;
}

/* Two-card grid */
.mode-cards-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.25rem;
    flex: 1;
    width: min(1100px, calc(100% - 2rem));
    max-width: 1100px;
    margin: 0 auto;
    align-items: stretch;
}
.mode-card {
    position: relative;
    min-height: 480px;
    border-radius: 28px !important;
    overflow: hidden;
    text-decoration: none !important;
    cursor: pointer;
    background-size: cover; background-position: center;
    display: flex; flex-direction: column; justify-content: flex-end;
    animation: mcEnter 0.75s cubic-bezier(0.22, 1, 0.36, 1) both;
    box-shadow: 0 26px 72px rgba(0,0,0,0.32);
}
.mode-card:first-child { animation-delay: 0.08s; }
.mode-card:last-child  { animation-delay: 0.20s; }

.mc-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(
        180deg,
        rgba(6,3,1,0.30) 0%,
        rgba(6,3,1,0.55) 40%,
        rgba(6,3,1,0.88) 75%,
        rgba(6,3,1,0.97) 100%
    );
    transition: background 0.5s ease;
}
.mc-overlay--home {
    background: linear-gradient(
        180deg,
        rgba(4,2,1,0.30) 0%,
        rgba(4,2,1,0.55) 40%,
        rgba(4,2,1,0.90) 75%,
        rgba(4,2,1,0.98) 100%
    );
}
.mode-card:hover .mc-overlay { background: rgba(4,2,1,0.55) !important; }
.mode-card:focus-visible,
.mode-card:active {
    outline: none;
    transform: translateY(-4px) scale(1.01);
    box-shadow: 0 34px 84px rgba(0,0,0,0.45), 0 0 0 1px rgba(201,168,124,0.22);
}

.mc-inner {
    position: relative; z-index: 2;
    padding: 2.5rem 3rem;
    display: flex; flex-direction: column; gap: 1rem;
    transform: translateY(8px);
    transition: transform 0.5s cubic-bezier(0.22, 1, 0.36, 1);
}
.mode-card:hover .mc-inner { transform: translateY(0); }

.mc-icon-wrap {
    width: 60px; height: 60px; border-radius: 50%;
    background: rgba(201,168,124,0.10);
    border: 1.5px solid rgba(201,168,124,0.28);
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 0.5rem;
    transition: background 0.4s ease, box-shadow 0.4s ease, transform 0.5s ease;
}
.mode-card:hover .mc-icon-wrap {
    background: rgba(201,168,124,0.18);
    box-shadow: 0 0 24px rgba(201,168,124,0.25);
    transform: scale(1.08);
}
.mc-icon {
    width: 28px; height: 28px; object-fit: contain;
    filter: brightness(0) invert(1);
    opacity: 0.65;
    transition: opacity 0.35s ease, filter 0.35s ease;
}
.mc-icon--home {
    filter: invert(1);
    mix-blend-mode: screen;
}
.mode-card:hover .mc-icon {
    opacity: 1;
    filter: brightness(0) invert(1) sepia(0.4) saturate(2.5) hue-rotate(330deg);
}
.mode-card:hover .mc-icon--home {
    filter: invert(1) sepia(0.6) saturate(2) hue-rotate(330deg);
    mix-blend-mode: screen;
}
.mc-title {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2.6rem !important; font-weight: 300 !important;
    color: #FFFFFF !important; letter-spacing: 1.5px;
    margin: 0 !important; line-height: 1.05 !important;
}
.mc-desc {
    font-size: 0.8rem; color: rgba(255,255,255,0.45);
    font-family: 'Satoshi', sans-serif; line-height: 1.65;
    margin: 0; letter-spacing: 0.2px;
    transition: color 0.35s ease;
}
.mode-card:hover .mc-desc { color: rgba(255,255,255,0.70); }
.mc-body { display: flex; flex-direction: column; gap: 0.75rem; }
.mc-tags {
    display: flex; flex-wrap: wrap; gap: 0.35rem;
}
.mc-tags span {
    font-size: 0.58rem; letter-spacing: 2px; text-transform: uppercase;
    padding: 0.22rem 0.65rem;
    border: 1px solid rgba(201,168,124,0.22);
    color: rgba(201,168,124,0.65);
    border-radius: 20px; font-family: 'Satoshi', sans-serif;
    transition: all 0.25s ease;
}
.mode-card:hover .mc-tags span {
    border-color: rgba(201,168,124,0.45);
    color: rgba(201,168,124,0.90);
}
.mc-cta {
    display: flex; align-items: center; gap: 0.6rem;
    font-size: 0.68rem; letter-spacing: 3px; text-transform: uppercase;
    color: var(--accent); font-family: 'Satoshi', sans-serif; font-weight: 600;
    padding-top: 0.75rem;
    border-top: 1px solid rgba(201,168,124,0.18);
    transition: gap 0.3s ease;
    position: relative;
}
.mode-card:hover .mc-cta { gap: 1rem; }
.mc-cta::after {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 999px;
    background: radial-gradient(circle, rgba(201,168,124,0.16), transparent 65%);
    opacity: 0;
    transform: scale(0.85);
    transition: opacity 0.25s ease, transform 0.25s ease;
}
.mode-card:hover .mc-cta::after {
    opacity: 1;
    transform: scale(1);
}
.mc-arrow {
    display: inline-block;
    transition: transform 0.35s cubic-bezier(0.34,1.2,0.64,1);
}
.mode-card:hover .mc-arrow { transform: translateX(5px); }

/* Vertical gold divider between cards */
.mode-cards-grid::after {
    content: '';
    position: absolute;
    top: 5%; bottom: 5%;
    left: 50%; width: 1px;
    background: linear-gradient(to bottom, transparent, rgba(201,168,124,0.28) 30%, rgba(201,168,124,0.28) 70%, transparent);
    pointer-events: none;
}
.mode-cards-grid { position: relative; }

/* ══════════════════════════════════════════════════════════════════════════
   FORM HEADER (back button + mode badge)
══════════════════════════════════════════════════════════════════════════ */
.form-header {
    width: calc(100% + 6rem);
    margin-left: -3rem;
    height: 132px;
    position: relative; overflow: hidden;
    background-size: cover; background-position: center 35%;
    margin-bottom: 0.75rem;
    animation: fhFade 0.6s cubic-bezier(0.22,1,0.36,1) both;
}
.fh-overlay {
    position: absolute; inset: 0;
    background: linear-gradient(90deg, rgba(6,3,1,0.96) 0%, rgba(6,3,1,0.75) 55%, rgba(6,3,1,0.45) 100%);
}
.fh-content {
    position: relative; z-index: 2;
    height: 100%;
    display: flex; align-items: center; justify-content: space-between;
    padding: 0 3.5rem;
}
.fh-back {
    font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase;
    color: rgba(255,255,255,0.50); font-family: 'Satoshi', sans-serif;
    text-decoration: none !important; font-weight: 500;
    transition: color 0.25s ease, letter-spacing 0.25s ease;
}
.fh-back:hover { color: var(--accent); letter-spacing: 4px; }
.fh-badge {
    display: flex; align-items: center; gap: 0.85rem;
}
.fh-icon-wrap {
    width: 38px; height: 38px; border-radius: 50%;
    background: rgba(201,168,124,0.12);
    border: 1px solid rgba(201,168,124,0.32);
    display: flex; align-items: center; justify-content: center;
}
.fh-icon {
    width: 18px; height: 18px; object-fit: contain;
    filter: brightness(0) invert(1) sepia(0.4) saturate(2.5) hue-rotate(330deg);
}
.fh-icon--home {
    filter: invert(1) sepia(0.6) saturate(2) hue-rotate(330deg);
    mix-blend-mode: screen;
}
.fh-mode-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.25rem; font-weight: 300;
    color: #FFFFFF; letter-spacing: 2px;
}

/* ══════════════════════════════════════════════════════════════════════════
   RESULT LAYOUT
══════════════════════════════════════════════════════════════════════════ */
.res-layout {
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 0;
    width: calc(100% + 6rem);
    margin-left: -3rem;
    min-height: 480px;
    background: linear-gradient(160deg, #0C0703 0%, #160A04 50%, #0C0703 100%);
    border-top: 1px solid rgba(201,168,124,0.12);
    margin-top: 1.5rem;
    animation: resSlideRight 0.75s cubic-bezier(0.22,1,0.36,1) both;
}
.res-left {
    padding: 3.5rem 3rem 3.5rem 3.5rem;
    display: flex; flex-direction: column; gap: 1.1rem;
    border-right: 1px solid rgba(201,168,124,0.08);
    animation: resSlideLeft 0.6s cubic-bezier(0.22,1,0.36,1) 0.05s both;
}
.res-right {
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    padding: 3rem 2rem;
    gap: 2rem;
    animation: resSlideRight 0.6s cubic-bezier(0.22,1,0.36,1) 0.15s both;
}

/* ── Result card animated cup ──────────────────────────────────────────── */
.res-cup-art {
    display: flex;
    flex-direction: column;
    align-items: center;
    animation: cupFloat 4.2s ease-in-out infinite;
    transform: scale(1.55);
    transform-origin: center top;
    margin-top: 0.5rem;
}
/* Reuse .bca-* steam + cup from barista — scale handled by .res-cup-art */

/* Iced glass variant */
.rca-glass-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
}
.rca-glass {
    width: 72px;
    height: 100px;
    background: linear-gradient(170deg, rgba(180,220,255,0.18), rgba(160,200,240,0.08));
    border: 1.5px solid rgba(180,220,255,0.38);
    border-top-width: 2px;
    border-radius: 4px 4px 14px 14px;
    position: relative;
    overflow: hidden;
}
.rca-liquid--iced {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 55%;
    background: linear-gradient(to top, rgba(100,180,240,0.42), rgba(140,200,255,0.14));
    animation: breathe 3.8s ease-in-out infinite;
}
.rca-ice {
    position: absolute;
    background: rgba(220,240,255,0.55);
    border: 1px solid rgba(180,220,255,0.6);
    border-radius: 3px;
}
.rca-ice1 { width: 20px; height: 18px; top: 28px; left: 10px; transform: rotate(-12deg); }
.rca-ice2 { width: 16px; height: 14px; top: 22px; right: 12px; transform: rotate(8deg); }
.rca-shine {
    position: absolute;
    top: 6px; left: 8px;
    width: 6px; height: 28px;
    background: linear-gradient(to bottom, rgba(255,255,255,0.35), transparent);
    border-radius: 3px;
}
.rca-straw {
    position: absolute;
    right: 18px; top: -14px;
    width: 4px; height: 48px;
    background: linear-gradient(to bottom, rgba(201,168,124,0.9), rgba(168,115,64,0.7));
    border-radius: 2px;
    transform: rotate(6deg);
    transform-origin: bottom center;
}
.rca-glass-base {
    width: 82px; height: 8px;
    background: linear-gradient(90deg, transparent, rgba(180,220,255,0.18), transparent);
    border-radius: 50%;
    border: 1px solid rgba(180,220,255,0.22);
    margin-top: 2px;
}
.res-mode-lbl {
    font-size: 0.58rem; letter-spacing: 5px; text-transform: uppercase;
    color: var(--accent); font-family: 'Satoshi', sans-serif;
}
.res-name {
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.2rem, 3.5vw, 3.4rem) !important;
    font-weight: 300 !important; color: #FFFFFF !important;
    letter-spacing: 1px; line-height: 1.08;
    margin: 0 !important;
    animation: revealMask 0.9s cubic-bezier(0.77,0,0.175,1) 0.2s both;
}
.res-badges { display: flex; gap: 0.5rem; flex-wrap: wrap; }
.res-badge {
    border: 1px solid rgba(201,168,124,0.22);
    padding: 0.35rem 0.9rem; font-size: 0.68rem;
    color: rgba(255,255,255,0.50); background: rgba(201,168,124,0.06);
    font-weight: 500; border-radius: 20px;
    font-family: 'Satoshi', sans-serif; letter-spacing: 0.4px;
}
.res-desc {
    font-size: 0.88rem; color: rgba(255,255,255,0.45);
    font-family: 'Satoshi', sans-serif; line-height: 1.75;
    margin: 0;
}
.res-detail-label {
    font-size: 0.55rem; letter-spacing: 4px; text-transform: uppercase;
    color: var(--accent); font-family: 'Satoshi', sans-serif; font-weight: 700;
    margin-top: 0.5rem;
}
.res-steps {
    list-style: none; margin: 0.5rem 0 0; padding: 0;
    display: flex; flex-direction: column; gap: 0.5rem;
}
.res-step {
    display: flex; align-items: flex-start; gap: 0.75rem;
    font-size: 0.85rem; color: rgba(255,255,255,0.72);
    font-family: 'Satoshi', sans-serif; line-height: 1.6;
    animation: staggerSlide 0.4s cubic-bezier(0.22,1,0.36,1) var(--d, 0.1s) both;
}
.res-step-n {
    width: 20px; height: 20px; border-radius: 50%; flex-shrink: 0;
    background: rgba(201,168,124,0.14); border: 1px solid rgba(201,168,124,0.28);
    display: flex; align-items: center; justify-content: center;
    font-size: 0.6rem; color: var(--accent); font-weight: 700;
    font-family: 'Satoshi', sans-serif; margin-top: 2px;
}
.home-brew-steps {
    gap: 0.55rem;
    max-width: 860px;
}
.home-brew-steps .res-step {
    padding: 0.72rem 0.85rem;
    border: 1px solid rgba(201,168,124,0.14);
    border-radius: 12px;
    background:
        linear-gradient(135deg, rgba(255,248,238,0.055), rgba(201,168,124,0.035));
    color: rgba(255,248,238,0.74);
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.04);
}
.home-brew-steps .res-step-n {
    width: 26px;
    height: 26px;
    background: rgba(201,168,124,0.20);
    color: #F1D49B;
    font-size: 0.68rem;
}
.home-brew-note {
    margin-top: 0.85rem;
    padding: 0.72rem 0.9rem;
    border-left: 2px solid var(--accent);
    border-radius: 10px;
    background: rgba(201,168,124,0.08);
    color: rgba(255,248,238,0.56);
    font-family: 'Satoshi', sans-serif;
    font-size: 0.78rem;
    line-height: 1.55;
}
.res-tip {
    font-size: 0.84rem; color: rgba(255,255,255,0.42);
    font-family: 'Satoshi', sans-serif; line-height: 1.7;
    margin: 0.5rem 0 0; border-left: 2px solid var(--accent);
    padding-left: 1rem;
}
.res-warning {
    font-size: 0.75rem; color: rgba(201,168,124,0.55);
    font-family: 'Satoshi', sans-serif; letter-spacing: 0.3px;
    padding: 0.6rem 1rem;
    background: rgba(201,168,124,0.05);
    border-radius: 8px; margin-top: 0.25rem;
}

/* Expand / transition polish for recommendation entry */
.fh-content,
.res-left,
.res-right {
    will-change: transform, opacity;
}
.fh-back,
.fh-mode-name {
    animation: fadeInUp 0.45s ease-out both;
}
.fh-badge {
    animation: fadeInUp 0.5s ease-out 0.08s both;
}

.cafe-shell .fh-overlay {
    background: linear-gradient(90deg, rgba(6,3,1,0.98) 0%, rgba(30,18,10,0.86) 55%, rgba(6,3,1,0.58) 100%);
}
.cafe-subtitle {
    margin: 0.35rem 0 1rem;
    color: rgba(255,255,255,0.38);
    font-size: 0.68rem;
    letter-spacing: 2.6px;
    text-transform: uppercase;
    font-family: 'Satoshi', sans-serif;
}

/* Staged preference form reveals */
[data-testid="column"]:has(#rec-quiz-marker),
[data-testid="column"]:has(#rec-quiz-marker-2) {
    animation: dropIn 0.65s cubic-bezier(0.34,1.2,0.64,1) both;
}
[data-testid="column"]:has(#rec-quiz-marker) { animation-delay: 0.08s; }
[data-testid="column"]:has(#rec-quiz-marker-2) { animation-delay: 0.16s; }
[data-testid="column"]:has(#rec-quiz-marker) .rec-col-title,
[data-testid="column"]:has(#rec-quiz-marker-2) .rec-col-title,
[data-testid="column"]:has(#rec-quiz-marker) .rec-col-subtitle,
[data-testid="column"]:has(#rec-quiz-marker-2) .rec-col-subtitle,
[data-testid="column"]:has(#rec-quiz-marker) .rec-chip-label,
[data-testid="column"]:has(#rec-quiz-marker-2) .rec-chip-label {
    animation: fadeInUp 0.55s ease-out both;
}
[data-testid="column"]:has(#rec-quiz-marker) .rec-col-title { animation-delay: 0.14s; }
[data-testid="column"]:has(#rec-quiz-marker-2) .rec-col-title { animation-delay: 0.18s; }
[data-testid="column"]:has(#rec-quiz-marker) .rec-col-subtitle { animation-delay: 0.18s; }
[data-testid="column"]:has(#rec-quiz-marker-2) .rec-col-subtitle { animation-delay: 0.22s; }
[data-testid="column"]:has(#rec-quiz-marker) .stRadio,
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio,
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"],
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"],
[data-testid="column"]:has(#rec-quiz-marker) .stSlider,
[data-testid="column"]:has(#rec-quiz-marker-2) .stSlider {
    animation: fadeInUp 0.55s ease-out both;
}
[data-testid="column"]:has(#rec-quiz-marker) .stRadio { animation-delay: 0.2s; }
[data-testid="column"]:has(#rec-quiz-marker-2) .stRadio { animation-delay: 0.24s; }
[data-testid="column"]:has(#rec-quiz-marker) [data-testid="stPills"] { animation-delay: 0.22s; }
[data-testid="column"]:has(#rec-quiz-marker-2) [data-testid="stPills"] { animation-delay: 0.26s; }
[data-testid="column"]:has(#rec-quiz-marker) .stSlider,
[data-testid="column"]:has(#rec-quiz-marker-2) .stSlider { animation-delay: 0.28s; }

/* CTA microinteraction */
[data-testid="stHorizontalBlock"] .stButton > button,
.stButton > button {
    position: relative;
    overflow: hidden;
}
.stButton > button::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle, rgba(255,255,255,0.25), transparent 60%);
    opacity: 0;
    transform: scale(0.85);
    transition: opacity 0.2s ease, transform 0.2s ease;
    pointer-events: none;
}
.stButton > button:hover::after,
.stButton > button:active::after {
    opacity: 1;
    transform: scale(1);
}
.stButton > button:active {
    box-shadow: 0 0 0 0 rgba(201,168,124,0.0), 0 0 0 6px rgba(201,168,124,0.18) !important;
}

[data-testid="column"]:has(#rec-result-actions) + [data-testid="column"] .stButton > button,
[data-testid="column"]:has(#rec-result-actions) + [data-testid="column"] + [data-testid="column"] .stButton > button,
[data-testid="column"]:has(#rec-result-actions) + [data-testid="column"] + [data-testid="column"] + [data-testid="column"] .stButton > button {
    border-radius: 999px !important;
    min-height: 3.2rem !important;
    background: var(--espresso) !important;
    color: #FFF8EE !important;
    border: 1px solid rgba(24,14,8,0.84) !important;
    box-shadow: 0 12px 26px rgba(90,55,27,0.12) !important;
}
[data-testid="column"]:has(#rec-result-actions) + [data-testid="column"] .stButton > button:hover,
[data-testid="column"]:has(#rec-result-actions) + [data-testid="column"] + [data-testid="column"] .stButton > button:hover,
[data-testid="column"]:has(#rec-result-actions) + [data-testid="column"] + [data-testid="column"] + [data-testid="column"] .stButton > button:hover {
    transform: translateY(-2px) !important;
    background: #2A1A10 !important;
    color: #FFF8EE !important;
}
.rec-result-action-row {
    width: calc(100% + 6rem);
    margin-left: -3rem;
    padding: 1.75rem 3.5rem 0.35rem;
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
}
.rec-result-action-row a {
    min-height: 3.4rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 999px;
    background: var(--espresso);
    color: #FFF8EE !important;
    text-decoration: none !important;
    border: 1px solid rgba(24,14,8,0.84);
    box-shadow: 0 12px 26px rgba(90,55,27,0.12);
    font-size: 0.76rem;
    letter-spacing: 2.4px;
    text-transform: uppercase;
    font-weight: 900;
    transition: transform 0.22s ease, background 0.22s ease, box-shadow 0.22s ease;
}
.rec-result-action-row a:hover {
    transform: translateY(-2px);
    background: #2A1A10;
    box-shadow: 0 18px 34px rgba(90,55,27,0.16);
}

@media (max-width: 900px) {
    .mode-cards-grid {
        grid-template-columns: 1fr;
        width: min(760px, calc(100% - 1.5rem));
    }
    .mode-select-page,
    .mode-select-hdr,
    .mode-card {
        width: 100% !important;
    }
    .res-layout {
        grid-template-columns: 1fr;
    }
    .rec-result-action-row {
        width: 100%;
        margin-left: 0;
        padding: 1rem 0 0.25rem;
        grid-template-columns: 1fr;
    }
    .barista-hero {
        width: calc(100% + 2rem);
        margin-left: -1rem;
        padding: 2.6rem 1.4rem 2.2rem;
        align-items: flex-start;
    }
    .barista-hero-right {
        display: none;
    }
    .barista-hero h1 {
        font-size: 3rem !important;
    }
    .barista-chat-heading {
        display: block;
    }
    .barista-chat-heading strong {
        display: block;
        margin-top: 0.45rem;
        text-align: left;
    }
    .barista-profile-panel {
        border-left: 0;
        border-top: 1px solid rgba(24,14,8,0.14);
        padding: 1.2rem 0 0;
    }
    .barista-result-panel {
        grid-template-columns: 1fr;
    }
    .barista-score {
        width: auto;
        height: auto;
        border-radius: 999px;
        justify-self: start;
        padding: 0.45rem 0.9rem;
    }
    .login-page {
        width: calc(100% + 2rem);
        margin-left: -1rem;
        min-height: 100vh;
        padding: 1.8rem 1.4rem 4rem;
        background-image:
            linear-gradient(170deg, rgba(6,3,1,0.74) 0%, rgba(12,6,2,0.38) 48%, rgba(6,3,1,0.80) 100%),
            var(--login-bg, linear-gradient(180deg,#2A1208 0%,#0F0804 100%));
        background-size: cover;
        background-position: center;
    }
    [data-testid="column"]:has(#login-form-marker) {
        margin-top: -82vh;
        width: calc(100vw - 2.2rem) !important;
        padding: 1.45rem 1.1rem;
    }
    .login-form-heading h2 {
        font-size: 2.2rem !important;
    }
}

/* ══════════════════════════════════════════════════════════════════════════
   CUP VISUALIZATION
══════════════════════════════════════════════════════════════════════════ */
.cup-viz { display: flex; flex-direction: column; align-items: center; gap: 0; }

/* ── Shared layer system ─────────────────────────────────────────────── */
.cup-mug-layers,
.cup-glass-layers {
    display: flex;
    flex-direction: column-reverse;
    position: absolute;
    bottom: 0; left: 0; right: 0; top: 0;
    z-index: 1;
}
.cup-layer {
    flex: var(--lf) 1 0;
    flex-grow: var(--lf);
    flex-shrink: 1;
    flex-basis: 0;
    background: var(--lbg);
    transform-origin: bottom center;
    animation: pourIn 0.55s cubic-bezier(0.34,1.1,0.64,1) var(--ld) both;
    display: flex; align-items: center; justify-content: center;
    overflow: hidden;
}
.res-right .cup-layer,
.composition-wrap .cup-layer {
    background: var(--lbg) !important;
    min-height: 14px;
    filter: saturate(1.8) brightness(1.18);
    opacity: 1 !important;
    box-shadow:
        inset 0 2px 0 rgba(255,255,255,0.20),
        inset 0 -2px 0 rgba(0,0,0,0.20);
}
.res-right .cup-layer[style*="2A0E04"],
.res-right .cup-layer[style*="180604"],
.composition-wrap .cup-layer[style*="2A0E04"],
.composition-wrap .cup-layer[style*="180604"] {
    background: linear-gradient(180deg, #A8572F 0%, #6F2C17 100%) !important;
}
.res-right .cup-layer[style*="C8A882"],
.composition-wrap .cup-layer[style*="C8A882"] {
    background: linear-gradient(180deg, #F3D5A2 0%, #D09A5E 100%) !important;
}
.res-right .cup-layer[style*="EDD8B8"],
.composition-wrap .cup-layer[style*="EDD8B8"] {
    background: linear-gradient(180deg, #FFF6D8 0%, #E6C989 100%) !important;
}
.res-right .cup-layer[style*="D4A96A"],
.composition-wrap .cup-layer[style*="D4A96A"] {
    background: linear-gradient(180deg, #F0BE5F 0%, #C77A25 100%) !important;
}
.res-right .cup-layer[style*="C8E8F8"],
.composition-wrap .cup-layer[style*="C8E8F8"] {
    background: linear-gradient(180deg, #DDF8FF 0%, #78C1E4 100%) !important;
}
.res-right .cup-layer[style*="C0966A"],
.composition-wrap .cup-layer[style*="C0966A"] {
    background: linear-gradient(180deg, #D8B282 0%, #8D5730 100%) !important;
}
.res-right .cup-layer[style*="6B3F2B"],
.composition-wrap .cup-layer[style*="6B3F2B"] {
    background: linear-gradient(180deg, #9C6547 0%, #5E2D1E 100%) !important;
}
.res-right .cup-layer[style*="5A2A10"],
.composition-wrap .cup-layer[style*="5A2A10"] {
    background: linear-gradient(180deg, #8E5133 0%, #4B2110 100%) !important;
}
.cup-lbl {
    font-size: 0.5rem; letter-spacing: 1.5px; text-transform: uppercase;
    color: rgba(255,255,255,0.78); font-family: 'Satoshi', sans-serif;
    font-weight: 900;
    text-shadow: 0 1px 3px rgba(0,0,0,0.50);
    white-space: nowrap; pointer-events: none;
}

/* ── Hot mug ─────────────────────────────────────────────────────────── */
.cup-mug { position: relative; }
.cup-steam {
    display: flex; gap: 10px; height: 42px;
    align-items: flex-end; justify-content: center;
    margin-bottom: -2px;
    position: relative;
    z-index: 5;
}
.cup-steam span {
    width: 6px; border-radius: 999px;
    background: linear-gradient(to top, rgba(255,250,240,0.98), rgba(255,250,240,0.46), rgba(255,250,240,0));
    animation: steamRiseNew 2.25s ease-out var(--sd) infinite;
    transform-origin: bottom;
    filter: blur(0.35px) drop-shadow(0 0 12px rgba(255,248,238,0.66));
}
.cup-steam span:nth-child(1) { height: 38px; }
.cup-steam span:nth-child(2) { height: 54px; }
.cup-steam span:nth-child(3) { height: 34px; }
.cup-mug-wrap {
    position: relative;
    width: 164px;
}
.cup-mug-body {
    width: 150px;
    height: 158px;
    margin: 0 auto;
    border: 3px solid rgba(255,245,228,0.54);
    border-radius: 18px 18px 46px 46px / 20px 20px 34px 34px;
    overflow: hidden;
    position: relative;
    background:
        linear-gradient(105deg, rgba(255,255,255,0.20) 0%, rgba(255,255,255,0.05) 16%, transparent 32%),
        linear-gradient(255deg, rgba(255,255,255,0.10) 0%, transparent 30%),
        rgba(255,248,236,0.10);
    backdrop-filter: blur(2px);
    clip-path: polygon(6% 0%, 94% 0%, 84% 100%, 16% 100%);
    box-shadow:
        inset 0 0 26px rgba(0,0,0,0.34),
        inset 12px 0 24px rgba(255,255,255,0.10),
        inset -12px 0 20px rgba(255,255,255,0.035),
        0 14px 32px rgba(0,0,0,0.24);
}
.cup-mug-body::before {
    content: '';
    position: absolute;
    top: -5px;
    left: 6px;
    right: 6px;
    height: 18px;
    border: 2px solid rgba(255,245,228,0.34);
    border-radius: 50%;
    background: radial-gradient(ellipse at center, rgba(255,255,255,0.08), rgba(255,255,255,0.01) 65%);
    z-index: 4;
    pointer-events: none;
}
.cup-mug-body::after {
    content: '';
    position: absolute;
    inset: 7px 13px 10px 13px;
    border-radius: 16px 16px 34px 34px / 16px 16px 28px 28px;
    border: 1px solid rgba(255,255,255,0.12);
    background:
        linear-gradient(115deg, rgba(255,255,255,0.18), transparent 22%),
        radial-gradient(circle at 72% 20%, rgba(255,255,255,0.14), transparent 24%);
    mix-blend-mode: screen;
    z-index: 3;
    pointer-events: none;
}
.cup-mug-shine {
    position: absolute; top: 10%; left: 17%; width: 13%; height: 76%;
    background: linear-gradient(to bottom, rgba(255,255,255,0.13), rgba(255,255,255,0.03) 48%, transparent 78%);
    border-radius: 999px;
    pointer-events: none; z-index: 3;
}
.cup-mug-handle {
    position: absolute;
    right: -7px; top: 37px;
    width: 34px; height: 58px;
    border: 1.5px solid rgba(255,245,228,0.30);
    border-left: none;
    border-radius: 0 24px 24px 0;
    background: transparent;
}
.cup-mug-saucer {
    position: relative;
    width: 214px; height: 28px; margin-top: -2px;
    background:
        radial-gradient(ellipse at 50% 38%, rgba(255,250,238,0.28) 0%, rgba(238,213,184,0.18) 32%, rgba(201,168,124,0.07) 55%, transparent 74%);
    border: 1px solid rgba(255,245,228,0.24);
    border-radius: 50%;
    box-shadow:
        inset 0 2px 8px rgba(255,255,255,0.10),
        0 10px 22px rgba(0,0,0,0.22);
}
.cup-mug-saucer::after {
    content: '';
    position: absolute;
    left: 34px; right: 34px; top: 8px; bottom: 8px;
    border-radius: 50%;
    border: 1px solid rgba(255,245,228,0.18);
    background: radial-gradient(ellipse at center, rgba(0,0,0,0.16), transparent 62%);
}

/* ── Iced glass ──────────────────────────────────────────────────────── */
.cup-glass { position: relative; }
.cup-glass-body {
    width: 122px; height: 190px;
    background:
        linear-gradient(105deg, rgba(255,255,255,0.26) 0%, rgba(255,255,255,0.06) 15%, transparent 34%),
        linear-gradient(255deg, rgba(255,255,255,0.14) 0%, transparent 32%),
        rgba(200,230,248,0.10);
    border: 2.5px solid rgba(230,250,255,0.48);
    border-radius: 18px 18px 34px 34px / 12px 12px 30px 30px;
    overflow: hidden; position: relative;
    clip-path: polygon(3% 0%, 97% 0%, 86% 100%, 14% 100%);
    backdrop-filter: blur(2px);
    box-shadow:
        inset 0 0 24px rgba(200,230,248,0.12),
        inset 11px 0 22px rgba(255,255,255,0.13),
        inset -11px 0 18px rgba(255,255,255,0.04),
        0 20px 40px rgba(0,0,0,0.24);
}
.cup-glass-body::before {
    content: '';
    position: absolute;
    top: -7px;
    left: 4px;
    right: 4px;
    height: 16px;
    border: 2px solid rgba(230,250,255,0.34);
    border-radius: 50%;
    z-index: 4;
    pointer-events: none;
}
.cup-glass-body::after {
    content: '';
    position: absolute;
    inset: 9px 11px 12px 11px;
    border-radius: 14px 14px 28px 28px / 10px 10px 24px 24px;
    border: 1px solid rgba(255,255,255,0.16);
    background:
        linear-gradient(115deg, rgba(255,255,255,0.20), transparent 24%),
        radial-gradient(circle at 76% 18%, rgba(255,255,255,0.18), transparent 24%);
    mix-blend-mode: screen;
    z-index: 3;
    pointer-events: none;
}
.cup-glass-shine {
    position: absolute; top: 8%; left: 15%; width: 12%; height: 78%;
    background: linear-gradient(to bottom, rgba(255,255,255,0.20), rgba(255,255,255,0.05) 45%, transparent 75%);
    border-radius: 999px;
    pointer-events: none; z-index: 3;
}
.cup-glass-straw {
    position: absolute;
    right: 27px; top: -36px;
    width: 5px; height: 152px;
    background: linear-gradient(135deg, rgba(201,168,124,0.7), rgba(201,168,124,0.4));
    border-radius: 3px;
    transform: rotate(6deg);
}
.cup-glass-base {
    width: 154px; height: 12px; margin-top: 5px;
    background: radial-gradient(ellipse at center, rgba(220,245,255,0.18) 0%, transparent 70%);
    border-radius: 50%; filter: blur(1px);
}

/* Result cup: keep the old proportional, color-blocked drink look. */
.res-right .cup-viz {
    animation:
        resultCupWake 0.85s cubic-bezier(0.2, 0.9, 0.24, 1.15) 0.08s both,
        resultCupFloat 4.8s ease-in-out 1.05s infinite;
    transform-origin: center bottom;
    will-change: transform;
}
.res-right .cup-mug-layers,
.res-right .cup-glass-layers,
.personality-result-cup .cup-mug-layers,
.personality-result-cup .cup-glass-layers {
    inset: 0;
    z-index: 2;
    opacity: 1;
}
.res-right .cup-mug-body,
.personality-result-cup .cup-mug-body {
    border-color: rgba(255,245,228,0.78);
    box-shadow:
        inset 0 0 12px rgba(255,250,230,0.12),
        inset 9px 0 16px rgba(255,255,255,0.12),
        inset -7px 0 14px rgba(0,0,0,0.10),
        0 14px 32px rgba(0,0,0,0.24);
    background:
        linear-gradient(105deg, rgba(255,255,255,0.24) 0%, rgba(255,255,255,0.07) 16%, transparent 30%),
        rgba(255,248,236,0.12);
}
.res-right .cup-mug-body.cup-fill-body,
.personality-result-cup .cup-mug-body.cup-fill-body {
    background:
        linear-gradient(100deg, transparent 0%, rgba(255,255,255,0.18) 42%, transparent 58%),
        linear-gradient(105deg, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.035) 16%, transparent 31%),
        linear-gradient(260deg, rgba(255,255,255,0.07) 0%, transparent 28%),
        var(--drink-fill);
    background-size: 220% 100%, 100% 100%, 100% 100%, 100% 100%;
    animation: resultLiquidGlow 3.8s ease-in-out 1.05s infinite;
}
.res-right .cup-glass-body,
.personality-result-cup .cup-glass-body {
    border-color: rgba(230,250,255,0.70);
    box-shadow:
        inset 0 0 12px rgba(255,250,230,0.10),
        inset 9px 0 16px rgba(255,255,255,0.13),
        inset -7px 0 14px rgba(0,0,0,0.10),
        0 18px 38px rgba(0,0,0,0.24);
    background:
        linear-gradient(105deg, rgba(255,255,255,0.30) 0%, rgba(255,255,255,0.08) 15%, transparent 32%),
        rgba(220,244,255,0.10);
}
.res-right .cup-glass-body.cup-fill-body,
.personality-result-cup .cup-glass-body.cup-fill-body {
    background:
        linear-gradient(100deg, transparent 0%, rgba(255,255,255,0.18) 42%, transparent 58%),
        linear-gradient(105deg, rgba(255,255,255,0.18) 0%, rgba(255,255,255,0.04) 14%, transparent 32%),
        linear-gradient(255deg, rgba(255,255,255,0.08) 0%, transparent 30%),
        var(--drink-fill);
    background-size: 220% 100%, 100% 100%, 100% 100%, 100% 100%;
    animation: resultLiquidGlow 4.2s ease-in-out 1.05s infinite;
}
.res-right .cup-fill-body .cup-mug-layers,
.res-right .cup-fill-body .cup-glass-layers,
.personality-result-cup .cup-fill-body .cup-mug-layers,
.personality-result-cup .cup-fill-body .cup-glass-layers {
    background: transparent;
}
.res-right .cup-fill-body .cup-mug-layers,
.res-right .cup-fill-body .cup-glass-layers {
    display: none;
}
.cup-composition-fill {
    position: absolute;
    inset: 0;
    z-index: 1;
    opacity: 1;
    pointer-events: none;
    transform-origin: bottom center;
    animation: pourIn 0.68s cubic-bezier(0.34,1.1,0.64,1) 0.08s both;
}
.res-right .cup-composition-fill,
.personality-result-cup .cup-composition-fill {
    filter: saturate(1.04) brightness(1.06);
    box-shadow:
        inset 0 2px 0 rgba(255,255,255,0.18),
        inset 0 -2px 0 rgba(0,0,0,0.18);
}
.cup-composition-labels {
    position: absolute;
    inset: 0;
    z-index: 5;
    pointer-events: none;
}
.cup-composition-label {
    position: absolute;
    left: 6%;
    right: 6%;
    transform: translateY(50%);
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 14px;
    padding: 0.1rem 0;
    border-top: 1px solid rgba(255,255,255,0.22);
    border-bottom: 1px solid rgba(0,0,0,0.15);
    color: rgba(255,255,255,0.94);
    font-family: 'Satoshi', sans-serif;
    font-size: 0.62rem;
    font-weight: 900;
    letter-spacing: 1.7px;
    line-height: 1;
    text-transform: uppercase;
    text-shadow: 0 1px 5px rgba(0,0,0,0.62);
    white-space: nowrap;
}
.cup-composition-label:first-child {
    border-bottom-color: rgba(255,255,255,0.16);
}
.res-right .cup-fill-body .cup-layer,
.personality-result-cup .cup-fill-body .cup-layer {
    background: transparent !important;
    filter: none;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.34),
        inset 0 -1px 0 rgba(0,0,0,0.22);
}
.res-right .cup-mug-body::after,
.res-right .cup-glass-body::after,
.personality-result-cup .cup-mug-body::after,
.personality-result-cup .cup-glass-body::after {
    opacity: 0.24;
    mix-blend-mode: normal;
    z-index: 4;
}
.res-right .cup-mug-shine,
.res-right .cup-glass-shine,
.personality-result-cup .cup-mug-shine,
.personality-result-cup .cup-glass-shine {
    z-index: 5;
    opacity: 0.68;
}
.res-right .cup-lbl,
.personality-result-cup .cup-lbl {
    color: rgba(255,255,255,0.92);
    font-size: 0.58rem;
    letter-spacing: 1.7px;
    text-shadow: 0 1px 5px rgba(0,0,0,0.72);
}
.res-right .cup-mug-handle {
    right: -38px;
    top: 52px;
    width: 56px;
    height: 78px;
    border: 2px solid rgba(255,245,228,0.28);
    border-left: 0;
    border-radius: 0 44px 44px 0;
    background: transparent;
    z-index: 0;
}
.res-right .cup-mug-handle::after { display: none; }
.res-right .cup-steam {
    height: 84px;
    width: 112px;
    margin-bottom: -24px;
    position: relative;
    overflow: visible;
}
.res-right .cup-steam span {
    position: absolute;
    bottom: 2px;
    width: 3px;
    border-radius: 2px;
    background: linear-gradient(to top, rgba(201,168,124,0.75), transparent);
    animation: steamRiseNew 2.8s ease-in-out var(--sd) infinite;
    transform-origin: bottom center;
    filter: blur(0.4px) drop-shadow(0 0 10px rgba(201,168,124,0.42));
    will-change: transform, opacity;
}
.res-right .cup-steam span:nth-child(1) { left: 36px; height: 42px; --sd: 0s;    }
.res-right .cup-steam span:nth-child(2) { left: 54px; height: 58px; --sd: 0.55s; }
.res-right .cup-steam span:nth-child(3) { left: 72px; height: 38px; --sd: 1.1s;  }
.res-right .cup-mug-saucer,
.res-right .cup-glass-base {
    animation: resultSaucerGlow 4.8s ease-in-out 1.05s infinite;
    transform-origin: center;
}

/* ── Score ring (compact) ────────────────────────────────────────────── */
.score-ring-wrap { display: flex; align-items: center; justify-content: center; width: 112px; height: 112px; }
.score-ring { width: 112px; height: 112px; animation: fadeIn 0.5s ease-out 0.5s both; }
.score-arc  { animation: arcDraw 1.4s cubic-bezier(0.4, 0, 0.2, 1) 0.5s both; }

/* ── Scroll-triggered reveals for Home components ─────────────────────── */
/* NOTE: .home-card excluded — view() timeline breaks column layout by keeping
   cards at opacity:0 until scroll-entry triggers, which fires at wrong time
   for the left-column card. Cards use their inline time-based animation instead. */
@supports (animation-timeline: view()) {
    .home-cta-tagline,
    .home-cta-desc,
    #rowa-cta-pill,
    .ticker-wrap {
        animation-delay: 0s !important;
        animation-fill-mode: both !important;
        animation-timeline: view() !important;
    }

    .home-cta-tagline {
        animation-name: fadeInUp !important;
        animation-duration: 0.8s !important;
        animation-range: entry 8% cover 28% !important;
    }

    #rowa-cta-pill {
        animation-name: fadeInUp !important;
        animation-duration: 0.85s !important;
        animation-range: entry 10% cover 30% !important;
    }

    .home-cta-desc {
        animation-name: fadeInUp !important;
        animation-duration: 0.9s !important;
        animation-range: entry 12% cover 32% !important;
    }

    .ticker-wrap {
        animation-name: fadeInUp !important;
        animation-duration: 0.85s !important;
        animation-range: entry 10% cover 28% !important;
    }
}

/* ── Profile dashboard + home preview ───────────────────────────────── */
.home-dashboard-preview {
    margin: 2rem 0 0;
    padding: 1.35rem 1.45rem;
    display: grid;
    grid-template-columns: minmax(260px, 1fr) minmax(360px, 0.9fr) auto;
    gap: 1.2rem;
    align-items: center;
    border-top: 1px solid rgba(24,14,8,0.12);
    border-bottom: 1px solid rgba(24,14,8,0.12);
    background: rgba(255,255,255,0.26);
    animation: fadeInUp 0.8s ease-out both;
}
.hdp-kicker {
    display: block;
    color: var(--gold);
    font-size: 0.58rem;
    letter-spacing: 3.4px;
    text-transform: uppercase;
    font-weight: 900;
    margin-bottom: 0.45rem;
}
.hdp-copy h2,
.profile-dashboard-grid h2,
.profile-habit-panel h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 2rem !important;
    line-height: 1.05 !important;
    font-weight: 500 !important;
    margin: 0 0 0.4rem !important;
}
.hdp-copy p {
    margin: 0;
    color: rgba(24,14,8,0.62);
    line-height: 1.65;
    font-size: 0.9rem;
}
.hdp-metrics {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.55rem;
}
.hdp-metrics div,
.profile-dashboard-strip div,
.profile-pill-card {
    border: 1px solid rgba(126,83,46,0.15);
    background: rgba(255,253,248,0.62);
    border-radius: 8px;
    padding: 0.8rem 0.9rem;
}
.hdp-metrics span,
.profile-dashboard-strip span,
.profile-pill-card span,
.profile-rank-row span,
.profile-note-row span {
    display: block;
    color: rgba(24,14,8,0.48);
    font-size: 0.54rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 800;
}
.hdp-metrics strong,
.profile-dashboard-strip strong,
.profile-pill-card strong {
    display: block;
    margin-top: 0.18rem;
    color: var(--espresso);
    font-size: 1rem;
    font-weight: 900;
}
.hdp-link {
    color: #FFF8EE !important;
    background: var(--espresso);
    border-radius: 999px;
    padding: 0.72rem 1rem;
    text-decoration: none !important;
    text-align: center;
    font-size: 0.66rem;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    font-weight: 900;
    white-space: nowrap;
    transition: transform 0.25s ease, filter 0.25s ease;
}
.hdp-link:hover {
    transform: translateY(-2px);
    filter: brightness(1.08);
}
.profile-page-head {
    padding: 2.6rem 0 1.4rem;
    max-width: 920px;
}
.profile-page-head h1,
.profile-dashboard-hero h1 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.8rem, 6vw, 5rem) !important;
    line-height: 0.95 !important;
    font-weight: 500 !important;
    margin: 0 0 0.75rem !important;
}
.profile-page-head p,
.profile-dashboard-hero p {
    color: rgba(24,14,8,0.62);
    line-height: 1.7;
    margin: 0;
    max-width: 720px;
}
.profile-dashboard-hero {
    margin: 1.5rem 0 1rem;
    padding: 1.6rem 0;
    border-top: 1px solid rgba(24,14,8,0.12);
    border-bottom: 1px solid rgba(24,14,8,0.12);
}
.profile-dashboard-strip {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.7rem;
    margin: 1rem 0 1.6rem;
}
.profile-dashboard-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 1.2rem;
    margin-bottom: 1.3rem;
}
.profile-dashboard-grid > section,
.profile-habit-panel {
    padding: 1.25rem 0;
    border-top: 1px solid rgba(24,14,8,0.12);
}
.profile-pill-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.65rem;
}
.profile-rank-list,
.profile-note-list {
    display: grid;
    gap: 0.55rem;
}
.profile-rank-row {
    display: grid;
    grid-template-columns: 34px 1fr auto;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(24,14,8,0.1);
}
.profile-rank-row strong {
    color: var(--espresso);
}
.profile-rank-row em {
    color: var(--gold);
    font-style: normal;
    font-weight: 900;
}
.profile-note-row {
    padding: 0.9rem 0;
    border-bottom: 1px solid rgba(24,14,8,0.1);
}
.profile-note-row p,
.profile-empty-note {
    color: rgba(24,14,8,0.66);
    line-height: 1.65;
    margin: 0.25rem 0 0;
}
.coffee-personality-hero {
    margin: 1rem 0 0;
    padding: 1.35rem 1.45rem 1rem;
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 1rem;
    align-items: start;
    background: linear-gradient(135deg, rgba(245,230,205,0.96), rgba(218,188,145,0.72));
    border: 1px solid rgba(126,83,46,0.16);
    border-radius: 8px 8px 0 0;
    box-shadow: 0 20px 54px rgba(90,55,27,0.12);
}
.coffee-personality-hero h1 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(3rem, 5vw, 5.4rem) !important;
    line-height: 0.9 !important;
    font-weight: 700 !important;
    margin: 0 0 0.7rem !important;
}
.coffee-personality-hero p {
    color: rgba(24,14,8,0.72);
    line-height: 1.6;
    margin: 0;
}
.coffee-personality-hero aside {
    min-width: 180px;
    padding: 0.82rem 1rem;
    border-radius: 0 0 8px 8px;
    background: #6B4423;
    color: #FFF8EE;
    text-align: left;
}
.coffee-personality-hero aside span {
    display: block;
    color: rgba(255,248,238,0.68);
    font-size: 0.54rem;
    letter-spacing: 2.2px;
    font-weight: 900;
}
.coffee-personality-hero aside strong {
    display: block;
    margin-top: 0.18rem;
    font-size: 0.95rem;
}
.coffee-personality-summary {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0.65rem;
    padding: 0.9rem 1rem 1rem;
    margin-bottom: 1rem;
    background: linear-gradient(135deg, rgba(245,230,205,0.96), rgba(218,188,145,0.72));
    border: 1px solid rgba(126,83,46,0.16);
    border-top: 0;
    border-radius: 0 0 8px 8px;
}
.coffee-personality-summary div,
.coffee-personality-panel {
    background: rgba(255,250,242,0.86);
    border: 1px solid rgba(126,83,46,0.13);
    border-radius: 8px;
    box-shadow: 0 12px 30px rgba(90,55,27,0.07);
}
.coffee-personality-summary div {
    padding: 0.9rem 0.95rem;
}
.coffee-personality-summary span {
    display: block;
    color: rgba(24,14,8,0.54);
    font-size: 0.56rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    font-weight: 900;
}
.coffee-personality-summary strong {
    display: block;
    color: var(--espresso);
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.55rem;
    line-height: 1;
    margin: 0.45rem 0 0.25rem;
}
.coffee-personality-summary p {
    color: rgba(24,14,8,0.66);
    margin: 0;
    line-height: 1.45;
    font-size: 0.8rem;
}
.coffee-personality-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin: 1rem 0;
}
.coffee-personality-panel {
    padding: 1.1rem;
}
.coffee-personality-panel h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2rem, 3vw, 3rem) !important;
    line-height: 0.98 !important;
    font-weight: 700 !important;
    margin: 0 0 0.9rem !important;
}
.exploration-bar {
    height: 16px;
    background: rgba(218,188,145,0.42);
    border-radius: 999px;
    overflow: hidden;
    margin: 0.25rem 0 1rem;
}
.exploration-bar span {
    display: block;
    height: 100%;
    min-width: 8%;
    border-radius: inherit;
    background: linear-gradient(90deg, #6B4423, #C9A87C);
    animation: fillBar 1s ease-out both;
}
.exploration-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.6rem;
}
.personality-chip-row {
    display: flex;
    gap: 0.45rem;
    margin: -0.35rem 0 0.8rem;
}
.personality-chip-row span {
    background: var(--espresso);
    color: #FFF8EE;
    border-radius: 999px;
    padding: 0.4rem 0.7rem;
    font-size: 0.72rem;
    font-weight: 800;
}
.personality-drink-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 0.7rem;
}
.personality-drink-grid.compact {
    grid-template-columns: repeat(5, minmax(0, 1fr));
}
.personality-drink-card {
    background:
        radial-gradient(circle at 50% 0%, rgba(210,166,107,0.16), transparent 42%),
        linear-gradient(160deg, #1A120C 0%, #27170F 54%, #100A07 100%);
    border: 1px solid rgba(238,213,184,0.16);
    border-radius: 8px;
    padding: 0.72rem 0.72rem 0.9rem;
    min-height: 290px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    overflow: hidden;
    box-shadow:
        inset 0 1px 0 rgba(255,248,238,0.08),
        0 14px 32px rgba(48,28,14,0.18);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
}
.personality-drink-card:hover {
    transform: translateY(-3px);
    border-color: rgba(238,213,184,0.30);
    box-shadow:
        inset 0 1px 0 rgba(255,248,238,0.10),
        0 22px 42px rgba(48,28,14,0.26);
}
.personality-drink-card strong {
    color: #FFF8EE;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: 1.35rem;
    line-height: 1;
    text-align: center;
    text-shadow: 0 1px 12px rgba(0,0,0,0.28);
}
.personality-drink-card p {
    color: rgba(255,248,238,0.58);
    font-size: 0.76rem;
    margin: 0.35rem 0 0;
    text-align: center;
}
.personality-result-cup {
    min-height: 210px;
    margin: -0.1rem -0.25rem 0.85rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 7px;
    background:
        radial-gradient(ellipse at 50% 72%, rgba(238,213,184,0.15), transparent 44%),
        radial-gradient(circle at 50% 14%, rgba(255,248,238,0.08), transparent 34%),
        linear-gradient(180deg, rgba(255,248,238,0.035), rgba(0,0,0,0.12));
    position: relative;
}
.personality-result-cup::after {
    content: '';
    position: absolute;
    inset: auto 12% 12px;
    height: 22px;
    border-radius: 50%;
    background: radial-gradient(ellipse at center, rgba(0,0,0,0.32), transparent 68%);
    filter: blur(2px);
    pointer-events: none;
}
.personality-result-cup .cup-viz {
    transform: scale(0.86);
    transform-origin: center bottom;
    position: relative;
    z-index: 1;
}
.personality-result-cup .composition-wrap {
    grid-template-columns: 1fr;
    justify-items: center;
    gap: 0.35rem;
    position: relative;
    z-index: 1;
}
.personality-result-cup .composition-legend {
    width: min(100%, 250px);
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.32rem;
}
.personality-result-cup .composition-legend-item {
    grid-template-columns: 9px minmax(0, 1fr) auto;
    gap: 0.36rem;
    padding: 0.34rem 0.42rem;
    border-radius: 7px;
    background: rgba(255,248,238,0.055);
}
.personality-result-cup .composition-legend-item span {
    width: 9px;
    height: 9px;
}
.personality-result-cup .composition-legend-item b,
.personality-result-cup .composition-legend-item em {
    font-size: 0.58rem;
    line-height: 1;
}
.personality-result-cup .composition-legend-item b {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.personality-result-cup .cup-glass-body,
.personality-result-cup .cup-mug-body {
    background:
        linear-gradient(105deg, rgba(255,255,255,0.24) 0%, rgba(255,255,255,0.06) 16%, transparent 34%),
        rgba(255,248,236,0.10);
}
.personality-result-cup .cup-layer {
    min-height: 18px;
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.16),
        inset 0 -1px 0 rgba(0,0,0,0.22);
    filter: saturate(1.45) brightness(1.2);
}
.personality-result-cup .cup-layer[style*="C8E8F8"] {
    background: linear-gradient(180deg, #DCF6FF 0%, #7FC3E5 100%) !important;
}
.personality-result-cup .cup-layer[style*="2A0E04"],
.personality-result-cup .cup-layer[style*="180604"] {
    background: linear-gradient(180deg, #7A3D22 0%, #1B0904 100%) !important;
}
.personality-result-cup .cup-layer[style*="C8A882"] {
    background: linear-gradient(180deg, #F2D6A5 0%, #B8834D 100%) !important;
}
.personality-result-cup .cup-layer[style*="EDD8B8"] {
    background: linear-gradient(180deg, #FFF2D3 0%, #D7B980 100%) !important;
}
.personality-result-cup .cup-lbl {
    color: rgba(255,255,255,0.82);
    font-weight: 900;
    text-shadow: 0 1px 3px rgba(0,0,0,0.50);
}
.personality-drink-grid.compact .personality-drink-card {
    min-height: 285px;
}
.personality-drink-grid.compact .personality-result-cup {
    min-height: 210px;
}
.personality-drink-grid.compact .personality-result-cup .cup-viz {
    transform: scale(0.66);
}
.personality-drink-grid.compact .personality-result-cup .composition-legend {
    grid-template-columns: 1fr;
    width: min(100%, 150px);
}
.personality-drink-grid.compact .personality-result-cup .composition-legend-item {
    padding: 0.28rem 0.34rem;
}
.profile-book-indicator {
    margin: 0.1rem 0 0.75rem;
    width: fit-content;
    color: rgba(24,14,8,0.58);
    border: 1px solid rgba(126,83,46,0.16);
    background: rgba(255,250,242,0.74);
    border-radius: 999px;
    padding: 0.56rem 1rem;
    font-size: 0.62rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 900;
}
.profile-page-head + div [data-testid="stButton"] button {
    min-height: 2.6rem !important;
    width: auto !important;
    padding: 0.62rem 1.05rem !important;
    border-radius: 999px !important;
    background: var(--espresso) !important;
    color: #FFF8EE !important;
    font-size: 0.62rem !important;
    letter-spacing: 1.7px !important;
    box-shadow: none !important;
}
.profile-book-shell {
    position: relative;
    margin: 0.4rem 0 2rem;
    min-height: 680px;
    perspective: 1800px;
}
.profile-book-spine {
    position: absolute;
    inset: 18px auto 18px 0;
    width: 34px;
    border-radius: 8px 0 0 8px;
    background:
        linear-gradient(90deg, rgba(57,34,18,0.55), rgba(126,83,46,0.20), rgba(255,248,238,0.08)),
        #5B351D;
    box-shadow: inset -10px 0 18px rgba(0,0,0,0.20);
    z-index: 2;
}
.profile-book-paper {
    min-height: 680px;
    margin-left: 26px;
    border-radius: 8px;
    background:
        linear-gradient(90deg, rgba(83,50,27,0.16) 0, transparent 42px),
        radial-gradient(circle at 15% 8%, rgba(201,168,124,0.18), transparent 34%),
        linear-gradient(145deg, #FFF8ED 0%, #F3E5CC 52%, #FFFDF8 100%);
    border: 1px solid rgba(126,83,46,0.18);
    box-shadow:
        0 28px 70px rgba(67,42,24,0.18),
        inset 0 1px 0 rgba(255,255,255,0.76),
        inset 44px 0 34px rgba(126,83,46,0.08);
    overflow: hidden;
    position: relative;
}
.profile-book-paper::after {
    content: '';
    position: absolute;
    right: 0;
    top: 18px;
    bottom: 18px;
    width: 20px;
    border-radius: 12px 0 0 12px;
    background: repeating-linear-gradient(
        to bottom,
        rgba(126,83,46,0.16) 0 1px,
        transparent 1px 7px
    );
    opacity: 0.5;
    pointer-events: none;
}
.profile-book-page {
    min-height: 680px;
    padding: clamp(1.5rem, 3vw, 3.1rem);
    position: relative;
    animation: bookPageTurn 0.55s cubic-bezier(0.22,1,0.36,1) both;
    transform-origin: left center;
}
.book-page-number {
    position: absolute;
    top: 1.15rem;
    right: 1.35rem;
    color: rgba(24,14,8,0.22);
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(3rem, 7vw, 6.5rem);
    line-height: 0.75;
    font-weight: 700;
    pointer-events: none;
}
.profile-book-page h1,
.profile-book-page h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 700 !important;
    letter-spacing: 0 !important;
}
.profile-book-page h1 {
    max-width: 780px;
    font-size: clamp(4rem, 8vw, 8rem) !important;
    line-height: 0.86 !important;
    margin: 0.2rem 0 1rem !important;
}
.profile-book-page h2 {
    max-width: 850px;
    font-size: clamp(3rem, 5vw, 5.2rem) !important;
    line-height: 0.9 !important;
    margin: 0.2rem 0 1rem !important;
}
.book-cover-copy p,
.book-page-intro {
    max-width: 720px;
    color: rgba(24,14,8,0.66);
    font-size: 1rem;
    line-height: 1.7;
    margin: 0 0 1.25rem;
}
.book-cover-stamp {
    position: absolute;
    right: clamp(1.4rem, 4vw, 3rem);
    top: clamp(1.4rem, 4vw, 3rem);
    width: min(230px, 28vw);
    min-height: 92px;
    display: grid;
    align-content: center;
    gap: 0.28rem;
    padding: 1rem 1.15rem;
    color: #FFF8EE;
    background:
        linear-gradient(145deg, rgba(91,53,29,0.94), rgba(45,27,16,0.96));
    border-radius: 8px;
    transform: rotate(1deg);
    box-shadow: 0 16px 34px rgba(67,42,24,0.24);
}
.book-cover-stamp span {
    color: rgba(255,248,238,0.62);
    font-size: 0.53rem;
    letter-spacing: 2.3px;
    font-weight: 900;
}
.book-cover-stamp strong {
    color: #FFF8EE;
    font-size: 1rem;
}
.book-summary {
    margin: clamp(2rem, 6vw, 5.5rem) 0 0;
    padding: 0;
    background: transparent;
    border: 0;
    box-shadow: none;
}
.book-summary div,
.profile-book-page .profile-pill-card {
    background: rgba(255,253,248,0.66);
    border-color: rgba(126,83,46,0.14);
    box-shadow: 0 10px 24px rgba(90,55,27,0.06);
}
.book-two-col {
    display: grid;
    grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr);
    gap: clamp(1.3rem, 3vw, 2.5rem);
    align-items: start;
}
.book-exploration {
    grid-template-columns: 1fr;
}
.book-brew-grid {
    align-items: stretch;
}
.personality-drink-grid.book-brew-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}
.personality-drink-grid.book-brew-grid.compact {
    grid-template-columns: repeat(2, minmax(0, 1fr));
}
.book-brew-grid .personality-drink-card {
    min-height: 390px;
}
.book-brew-grid .personality-result-cup {
    min-height: 285px;
}
.book-brew-grid .personality-result-cup .cup-viz {
    transform: scale(0.96);
}
.book-brew-grid.compact .personality-drink-card {
    min-height: 345px;
}
.book-brew-grid.compact .personality-result-cup {
    min-height: 250px;
}
.book-brew-grid.compact .personality-result-cup .cup-viz {
    transform: scale(0.84);
}
.book-note-list {
    margin-top: 1rem;
}
.profile-book-page .profile-note-row {
    background: rgba(255,253,248,0.48);
    border: 1px solid rgba(126,83,46,0.10);
    border-radius: 8px;
    padding: 0.78rem 0.9rem;
    margin-bottom: 0.55rem;
}
@keyframes bookPageTurn {
    0% {
        opacity: 0;
        transform: rotateY(-10deg) translateX(18px);
        filter: blur(3px);
    }
    100% {
        opacity: 1;
        transform: rotateY(0deg) translateX(0);
        filter: blur(0);
    }
}
.profile-flipbook {
    margin: 0.6rem 0 2rem;
}
.profile-flip-radio {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}
.profile-flip-stage {
    position: relative;
    display: grid;
    grid-template-columns: minmax(280px, 0.42fr) minmax(520px, 1fr);
    gap: 0;
    min-height: 735px;
    perspective: 2200px;
    filter: drop-shadow(0 30px 70px rgba(67,42,24,0.18));
}
.profile-book-left-page,
.profile-flip-stack {
    min-height: 735px;
    background:
        radial-gradient(circle at 18% 8%, rgba(201,168,124,0.18), transparent 34%),
        linear-gradient(145deg, #FFF8ED 0%, #F2E1C4 58%, #FFFDF8 100%);
    border: 1px solid rgba(126,83,46,0.18);
    box-shadow:
        inset 0 1px 0 rgba(255,255,255,0.76),
        inset 0 -1px 0 rgba(126,83,46,0.08);
}
.profile-book-left-page {
    position: relative;
    z-index: 1;
    padding: clamp(1.5rem, 3vw, 2.6rem);
    border-radius: 8px 0 0 8px;
    border-right: 0;
    overflow: hidden;
}
.profile-book-left-page::after {
    content: '';
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    width: 44px;
    background: linear-gradient(90deg, transparent, rgba(83,50,27,0.18));
    pointer-events: none;
}
.profile-book-left-page h2 {
    color: var(--espresso) !important;
    font-family: 'Cormorant Garamond', serif !important;
    font-size: clamp(2.8rem, 5vw, 4.6rem) !important;
    line-height: 0.9 !important;
    margin: 0.25rem 0 1rem !important;
}
.profile-book-left-page p {
    color: rgba(24,14,8,0.62);
    line-height: 1.7;
    margin: 0 0 2rem;
}
.profile-book-toc {
    display: grid;
    gap: 0.65rem;
    margin-top: clamp(1.6rem, 4vw, 4rem);
}
.profile-book-toc label {
    display: grid;
    grid-template-columns: 42px 1fr;
    align-items: center;
    gap: 0.75rem;
    padding: 0.78rem 0.85rem;
    border: 1px solid rgba(126,83,46,0.13);
    border-radius: 8px;
    background: rgba(255,253,248,0.48);
    color: var(--espresso);
    cursor: pointer;
    font-size: 0.86rem;
    font-weight: 800;
    transition: transform 0.22s ease, background 0.22s ease, border-color 0.22s ease;
}
.profile-book-toc label:hover {
    transform: translateX(4px);
    border-color: rgba(126,83,46,0.28);
    background: rgba(255,253,248,0.76);
}
.profile-book-toc label span {
    color: var(--gold);
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.45rem;
    line-height: 1;
    font-weight: 700;
}
.profile-book-toc-row {
    display: grid;
    grid-template-columns: 42px 1fr;
    align-items: center;
    gap: 0.75rem;
    padding: 0.78rem 0.85rem;
    border: 1px solid rgba(126,83,46,0.13);
    border-radius: 8px;
    background: rgba(255,253,248,0.48);
    color: var(--espresso);
    font-size: 0.86rem;
    font-weight: 800;
    text-decoration: none !important;
    transition: transform 0.22s ease, background 0.22s ease, border-color 0.22s ease;
}
.profile-book-toc-row:hover {
    transform: translateX(4px);
    border-color: rgba(126,83,46,0.28);
    background: rgba(255,253,248,0.76);
}
.profile-book-toc-row.active {
    background: var(--espresso);
    color: #FFF8EE !important;
    border-color: rgba(24,14,8,0.7);
}
.profile-book-toc-row span {
    color: var(--gold);
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.45rem;
    line-height: 1;
    font-weight: 700;
}
.profile-book-toc-row.active span {
    color: #E7C995;
}
.profile-flip-stack {
    position: relative;
    border-radius: 0 8px 8px 0;
    overflow: hidden;
    transform-style: preserve-3d;
    box-shadow:
        inset 42px 0 42px rgba(83,50,27,0.14),
        inset -12px 0 24px rgba(255,255,255,0.44);
}
.profile-flip-stack::before {
    content: '';
    position: absolute;
    inset: 0 auto 0 0;
    width: 58px;
    background: linear-gradient(90deg, rgba(83,50,27,0.22), transparent);
    z-index: 20;
    pointer-events: none;
}
.profile-flip-stack::after {
    content: '';
    position: absolute;
    right: 0;
    top: 16px;
    bottom: 16px;
    width: 20px;
    border-radius: 12px 0 0 12px;
    background: repeating-linear-gradient(
        to bottom,
        rgba(126,83,46,0.16) 0 1px,
        transparent 1px 7px
    );
    opacity: 0.48;
    z-index: 20;
    pointer-events: none;
}
.profile-flip-stack .flip-page {
    position: absolute;
    inset: 0;
    min-height: 735px;
    overflow: auto;
    backface-visibility: hidden;
    transform-origin: left center;
    transform-style: preserve-3d;
    opacity: 0;
    pointer-events: none;
    filter: saturate(0.92);
    transition:
        transform 0.9s cubic-bezier(0.22, 1, 0.36, 1),
        opacity 0.36s ease,
        filter 0.5s ease;
}
.profile-flip-stack .flip-page::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(83,50,27,0.10), transparent 12%),
        linear-gradient(270deg, rgba(255,255,255,0.38), transparent 24%);
    opacity: 0;
    transition: opacity 0.45s ease;
    pointer-events: none;
}
#profile-flip-1:checked ~ .profile-flip-stage .flip-page-1,
#profile-flip-2:checked ~ .profile-flip-stage .flip-page-2,
#profile-flip-3:checked ~ .profile-flip-stage .flip-page-3,
#profile-flip-4:checked ~ .profile-flip-stage .flip-page-4 {
    opacity: 1;
    pointer-events: auto;
    transform: rotateY(0deg) translateX(0);
    filter: saturate(1);
    z-index: 10;
}
#profile-flip-1:checked ~ .profile-flip-stage .flip-page-2,
#profile-flip-1:checked ~ .profile-flip-stage .flip-page-3,
#profile-flip-1:checked ~ .profile-flip-stage .flip-page-4,
#profile-flip-2:checked ~ .profile-flip-stage .flip-page-3,
#profile-flip-2:checked ~ .profile-flip-stage .flip-page-4,
#profile-flip-3:checked ~ .profile-flip-stage .flip-page-4 {
    opacity: 0.24;
    transform: rotateY(7deg) translateX(26px) scale(0.985);
    z-index: 2;
}
#profile-flip-2:checked ~ .profile-flip-stage .flip-page-1,
#profile-flip-3:checked ~ .profile-flip-stage .flip-page-1,
#profile-flip-3:checked ~ .profile-flip-stage .flip-page-2,
#profile-flip-4:checked ~ .profile-flip-stage .flip-page-1,
#profile-flip-4:checked ~ .profile-flip-stage .flip-page-2,
#profile-flip-4:checked ~ .profile-flip-stage .flip-page-3 {
    opacity: 0;
    transform: rotateY(-115deg) translateX(-18px);
    z-index: 1;
}
#profile-flip-1:checked ~ .profile-flip-stage .flip-page-1::before,
#profile-flip-2:checked ~ .profile-flip-stage .flip-page-2::before,
#profile-flip-3:checked ~ .profile-flip-stage .flip-page-3::before,
#profile-flip-4:checked ~ .profile-flip-stage .flip-page-4::before {
    opacity: 1;
}
.profile-book-tabs {
    display: flex;
    justify-content: center;
    gap: 0.55rem;
    margin: 1rem 0 0;
}
.profile-book-tabs label {
    color: rgba(24,14,8,0.64);
    border: 1px solid rgba(126,83,46,0.16);
    background: rgba(255,250,242,0.76);
    border-radius: 999px;
    padding: 0.62rem 0.92rem;
    cursor: pointer;
    font-size: 0.62rem;
    letter-spacing: 1.7px;
    text-transform: uppercase;
    font-weight: 900;
    transition: transform 0.22s ease, background 0.22s ease, color 0.22s ease;
}
.profile-book-tabs label:hover {
    transform: translateY(-2px);
    background: var(--espresso);
    color: #FFF8EE;
}
.profile-book-tab {
    color: rgba(24,14,8,0.64);
    border: 1px solid rgba(126,83,46,0.16);
    background: rgba(255,250,242,0.76);
    border-radius: 999px;
    padding: 0.62rem 0.92rem;
    font-size: 0.62rem;
    letter-spacing: 1.7px;
    text-transform: uppercase;
    font-weight: 900;
}
.profile-book-tab.active {
    background: var(--espresso);
    color: #FFF8EE;
    border-color: rgba(24,14,8,0.7);
}
.stable-page-stack {
    min-height: 735px;
    overflow: hidden;
}
.stable-page-stack .single-book-page {
    position: relative;
    inset: auto;
    min-height: 735px;
    opacity: 1;
    pointer-events: auto;
    filter: none;
    transform-origin: left center;
    animation: bookPageTurn 0.72s cubic-bezier(0.22,1,0.36,1) both;
}
.stable-page-stack .single-book-page::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(83,50,27,0.10), transparent 12%),
        linear-gradient(270deg, rgba(255,255,255,0.38), transparent 24%);
    pointer-events: none;
}
#profile-flip-1:checked ~ .profile-book-tabs label[for="profile-flip-1"],
#profile-flip-2:checked ~ .profile-book-tabs label[for="profile-flip-2"],
#profile-flip-3:checked ~ .profile-book-tabs label[for="profile-flip-3"],
#profile-flip-4:checked ~ .profile-book-tabs label[for="profile-flip-4"],
#profile-flip-1:checked ~ .profile-flip-stage label[for="profile-flip-1"],
#profile-flip-2:checked ~ .profile-flip-stage label[for="profile-flip-2"],
#profile-flip-3:checked ~ .profile-flip-stage label[for="profile-flip-3"],
#profile-flip-4:checked ~ .profile-flip-stage label[for="profile-flip-4"] {
    background: var(--espresso);
    color: #FFF8EE;
    border-color: rgba(24,14,8,0.7);
}
#profile-flip-1:checked ~ .profile-flip-stage label[for="profile-flip-1"] span,
#profile-flip-2:checked ~ .profile-flip-stage label[for="profile-flip-2"] span,
#profile-flip-3:checked ~ .profile-flip-stage label[for="profile-flip-3"] span,
#profile-flip-4:checked ~ .profile-flip-stage label[for="profile-flip-4"] span {
    color: #E7C995;
}

@media (max-width: 900px) {
    .home-dashboard-preview,
    .profile-dashboard-grid,
    .profile-dashboard-strip,
    .coffee-personality-hero,
    .coffee-personality-summary,
    .coffee-personality-grid {
        grid-template-columns: 1fr;
    }
    .hdp-metrics,
    .profile-pill-grid,
    .exploration-cards,
    .personality-drink-grid,
    .personality-drink-grid.compact {
        grid-template-columns: 1fr;
    }
    .personality-drink-card,
    .personality-drink-grid.compact .personality-drink-card {
        min-height: 280px;
    }
    .personality-drink-grid.compact .personality-result-cup {
        min-height: 210px;
    }
    .personality-drink-grid.compact .personality-result-cup .cup-viz {
        transform: scale(0.86);
    }
    .profile-book-shell,
    .profile-book-paper,
    .profile-book-page {
        min-height: auto;
    }
    .profile-book-paper {
        margin-left: 14px;
    }
    .profile-book-spine {
        width: 20px;
    }
    .book-two-col,
    .coffee-personality-summary,
    .personality-drink-grid.book-brew-grid,
    .personality-drink-grid.book-brew-grid.compact {
        grid-template-columns: 1fr;
    }
    .book-cover-stamp {
        position: relative;
        right: auto;
        top: auto;
        width: 100%;
        margin: 1.3rem 0 0;
    }
    .book-brew-grid .personality-drink-card,
    .book-brew-grid.compact .personality-drink-card {
        min-height: 350px;
    }
    .book-brew-grid .personality-result-cup,
    .book-brew-grid.compact .personality-result-cup {
        min-height: 255px;
    }
    .profile-flip-stage {
        grid-template-columns: 1fr;
        min-height: auto;
    }
    .profile-book-left-page {
        min-height: auto;
        border-radius: 8px 8px 0 0;
        border-right: 1px solid rgba(126,83,46,0.18);
        border-bottom: 0;
    }
    .profile-book-left-page::after {
        display: none;
    }
    .profile-flip-stack {
        min-height: 720px;
        border-radius: 0 0 8px 8px;
    }
    .profile-flip-stack .flip-page {
        min-height: 720px;
    }
    .profile-book-tabs {
        flex-wrap: wrap;
    }
}
</style>
"""
