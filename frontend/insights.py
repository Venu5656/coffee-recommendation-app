from __future__ import annotations

from html import escape
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import streamlit as st

from backend_client import CoffeeBackendClient

_DATA_PATH = (
    Path(__file__).parent.parent
    / "ADV_Python_Midterm_Team1_Nova"
    / "data_clean"
    / "master_hi_2010_2019.csv"
)

_CHART_BG  = "#FFF9F3"
_BAR_COLOR = "#6B4423"
_GOLD      = "#C9A87C"
_LINE      = "#A06535"
_MUTED     = "#5A3010"
_GRID      = "#E8D8C4"

_STATS = [
    ("10.1 kg", "Finland — highest per-capita"),
    ("85%",     "Variance explained by culture"),
    ("0.12",    "Work-hours correlation"),
    ("< 8%",    "Global shift, 2010–2019"),
]

_FINDINGS = [
    (
        "Culture beats pressure",
        "Culture and geography explain <strong>85%</strong> of cross-country variance in coffee consumption — making it a ritual before it is a productivity tool.",
        "85% variance",
    ),
    (
        "Finland sets the pace",
        "Finland leads global consumption at <strong>10.1 kg</strong> per person per year — nearly double the worldwide average. Scandinavia claims four of the top five spots.",
        "10.1 kg / yr",
    ),
    (
        "Work hours are a weak signal",
        "Work intensity has almost <strong>no correlation</strong> (r = 0.12) with coffee intake. The overworked-needs-coffee story is mostly a myth.",
        "r = 0.12",
    ),
    (
        "GDP explains little on its own",
        "Each <strong>$10,000 increase</strong> in GDP per capita raises consumption by only ~5%. Income alone cannot explain why some nations drink far more than others.",
        "~5% per $10k",
    ),
    (
        "The habit is remarkably stable",
        "Global coffee consumption varied less than <strong>8%</strong> between 2010 and 2019 — one of the steadier dietary trends in the dataset.",
        "< 8% variation",
    ),
    (
        "Cold brew changes acidity",
        "Cold brew can have up to <strong>65% less acidity</strong> than hot-brewed coffee — gentler on the stomach and noticeably smoother in taste.",
        "65% less acid",
    ),
]

_EVIDENCE = [
    ("Consumption leader", "Finland",         "10.1 kg per person / yr"),
    ("Weakest myth",       "Work hours",      "r = 0.12"),
    ("Strongest driver",   "Culture",         "85% of variance"),
    ("Trend stability",    "Global 2010–19",  "< 8% variation"),
    ("GDP lift",           "Per $10k income", "~5% more consumption"),
]


@st.cache_data
def _load_data() -> pd.DataFrame:
    try:
        df = pd.read_csv(_DATA_PATH)
        df = df.dropna(subset=["coffee_kg_pc", "gdp_pc", "hours_worked"])
        df["year"] = df["year"].astype(int)
        return df
    except Exception:
        return pd.DataFrame()


def _styled_fig(w: float, h: float):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_facecolor(_CHART_BG)
    ax.set_facecolor(_CHART_BG)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines["left"].set_color("#E0CAB0")
    ax.spines["bottom"].set_color("#E0CAB0")
    ax.tick_params(colors=_MUTED, labelsize=8)
    ax.xaxis.label.set_color(_MUTED)
    ax.yaxis.label.set_color(_MUTED)
    ax.grid(alpha=0.18, linestyle="--", color=_GRID)
    return fig, ax


def _render_charts(df_full: pd.DataFrame) -> None:
    # ── Year filter ───────────────────────────────────────────────────────────
    year_range = st.slider(
        "Year range",
        min_value=int(df_full["year"].min()),
        max_value=int(df_full["year"].max()),
        value=(int(df_full["year"].min()), int(df_full["year"].max())),
        key="ins_years",
    )

    df = df_full[
        (df_full["year"] >= year_range[0]) & (df_full["year"] <= year_range[1])
    ]
    df_country = df

    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

    # ── Row 1: Bar + Line ─────────────────────────────────────────────────────
    c1, c2 = st.columns(2, gap="medium")

    with c1:
        st.markdown(
            '<span class="ip-chart-kicker">Top countries</span>'
            '<p class="ip-chart-title">Consumption by Country</p>',
            unsafe_allow_html=True,
        )
        top_n = 12
        country_avg = (
            df.groupby("country")["coffee_kg_pc"]
            .mean()
            .sort_values(ascending=False)
            .head(top_n)
            .sort_values(ascending=True)
        )
        fig1, ax1 = _styled_fig(6, max(3.4, len(country_avg) * 0.46))
        bars = ax1.barh(country_avg.index, country_avg.values, color=_BAR_COLOR,
                        height=0.56, zorder=2)
        ax1.set_xlabel("kg / person / year", fontsize=8)
        ax1.xaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f"))
        for bar in bars:
            w = bar.get_width()
            ax1.text(w + 0.06, bar.get_y() + bar.get_height() / 2,
                     f"{w:.1f}", va="center", fontsize=7, color=_MUTED)
        plt.tight_layout()
        st.pyplot(fig1, use_container_width=True)
        plt.close(fig1)

    with c2:
        st.markdown(
            '<span class="ip-chart-kicker">Trend over time</span>'
            '<p class="ip-chart-title">Consumption Over Time — Global Average</p>',
            unsafe_allow_html=True,
        )
        line_df = (
            df_country.groupby("year")["coffee_kg_pc"]
            .mean().reset_index().sort_values("year")
        )
        fig2, ax2 = _styled_fig(6, 4.0)
        ax2.plot(line_df["year"], line_df["coffee_kg_pc"],
                 marker="o", color=_LINE, linewidth=2.4, markersize=5, zorder=2)
        ax2.fill_between(line_df["year"], line_df["coffee_kg_pc"],
                         alpha=0.10, color=_LINE)
        ax2.set_xlabel("Year", fontsize=8)
        ax2.set_ylabel("kg / person / year", fontsize=8)
        ax2.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
        plt.tight_layout()
        st.pyplot(fig2, use_container_width=True)
        plt.close(fig2)

    st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)

    # ── Row 2: Scatter plots ──────────────────────────────────────────────────
    c3, c4 = st.columns(2, gap="medium")

    with c3:
        st.markdown(
            '<span class="ip-chart-kicker">Wealth vs habit</span>'
            '<p class="ip-chart-title">GDP vs Coffee Consumption</p>',
            unsafe_allow_html=True,
        )
        scatter_df = df.groupby("country")[["gdp_pc", "coffee_kg_pc"]].mean().reset_index()
        fig3, ax3 = _styled_fig(5.5, 3.9)
        ax3.scatter(scatter_df["gdp_pc"], scatter_df["coffee_kg_pc"],
                    color=_GOLD, alpha=0.82, edgecolors=_BAR_COLOR,
                    linewidth=0.6, s=58, zorder=2)
        ax3.set_xlabel("GDP per capita (USD)", fontsize=8)
        ax3.set_ylabel("Coffee (kg/person/yr)", fontsize=8)
        ax3.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}k"))
        plt.tight_layout()
        st.pyplot(fig3, use_container_width=True)
        plt.close(fig3)

    with c4:
        st.markdown(
            '<span class="ip-chart-kicker">Effort vs ritual</span>'
            '<p class="ip-chart-title">Work Hours vs Coffee Consumption</p>',
            unsafe_allow_html=True,
        )
        work_df = df.groupby("country")[["hours_worked", "coffee_kg_pc"]].mean().reset_index()
        fig4, ax4 = _styled_fig(5.5, 3.9)
        ax4.scatter(work_df["hours_worked"], work_df["coffee_kg_pc"],
                    color=_BAR_COLOR, alpha=0.82, edgecolors="#3B1A0A",
                    linewidth=0.6, s=58, zorder=2)
        ax4.set_xlabel("Avg Hours Worked / Year", fontsize=8)
        ax4.set_ylabel("Coffee (kg/person/yr)", fontsize=8)
        plt.tight_layout()
        st.pyplot(fig4, use_container_width=True)
        plt.close(fig4)


def render_insights_page(client: CoffeeBackendClient) -> None:

    # ── 1. Hero ───────────────────────────────────────────────────────────────
    hero_stats = "".join(
        f'<div class="ip-hero-stat"><strong>{num}</strong><span>{escape(label)}</span></div>'
        for num, label in _STATS
    )
    st.markdown(
        f"""
        <div class="ip-hero">
          <span class="hdp-kicker">Coffee Intelligence</span>
          <h1>What the world reveals<br>through coffee</h1>
          <p class="ip-hero-sub">Research findings from consumption data across high-income countries, 2010–2019.</p>
          <div class="ip-hero-stats">{hero_stats}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── 2. Data Explorer ──────────────────────────────────────────────────────
    st.markdown(
        """
        <div class="ip-explorer-head">
          <span class="hdp-kicker">Data Explorer</span>
          <h2>Browse the numbers yourself</h2>
          <p>Filter by country and year range to drill into the dataset behind each finding.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    df_full = _load_data()
    if df_full.empty:
        st.warning("Dataset not found — charts unavailable.")
    else:
        _render_charts(df_full)

    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    # ── 3. Key Findings grid ──────────────────────────────────────────────────
    finding_cards = "".join(
        f"""<div class="ip-finding-card" style="--d:{0.04 + i * 0.06:.2f}s">
          <span class="ip-fn-num">{i + 1:02d}</span>
          <h3>{escape(title)}</h3>
          <p>{body}</p>
          <span class="ip-fn-badge">{escape(metric)}</span>
        </div>"""
        for i, (title, body, metric) in enumerate(_FINDINGS)
    )
    st.markdown(
        f"""
        <div class="ip-findings-head">
          <span class="hdp-kicker">Key Findings</span>
          <h2>Six patterns from the data</h2>
        </div>
        <div class="ip-findings-grid">{finding_cards}</div>
        """,
        unsafe_allow_html=True,
    )

    # ── 4. Evidence strip ─────────────────────────────────────────────────────
    ev_items = "".join(
        f"""<div class="ip-ev-item">
          <span>{escape(label)}</span>
          <strong>{escape(value)}</strong>
          <em>{escape(note)}</em>
        </div>"""
        for label, value, note in _EVIDENCE
    )
    st.markdown(
        f'<div class="ip-evidence-strip">{ev_items}</div>',
        unsafe_allow_html=True,
    )

    # ── 5. Model notes ────────────────────────────────────────────────────────
    backend_items = client.get_insights()
    if backend_items:
        model_items = "".join(
            f'<li class="ip-model-item" style="--d:{0.05 + i * 0.07:.2f}s">{escape(item)}</li>'
            for i, item in enumerate(backend_items)
        )
        st.markdown(
            f"""
            <div class="ip-model-card">
              <span class="hdp-kicker">Model Notes</span>
              <h2>What the recommender is watching</h2>
              <ul class="ip-model-list">{model_items}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
