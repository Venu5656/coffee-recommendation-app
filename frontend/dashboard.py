from __future__ import annotations

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

_CHART_COLOR = "#6B4423"
_SCATTER_COLOR = "#C9A87C"
_LINE_COLOR = "#1F77B4"


@st.cache_data
def _load_data() -> pd.DataFrame:
    try:
        df = pd.read_csv(_DATA_PATH)
        df = df.dropna(subset=["coffee_kg_pc", "gdp_pc", "hours_worked"])
        df["year"] = df["year"].astype(int)
        return df
    except Exception:
        return pd.DataFrame()


def render_dashboard_page(_client: CoffeeBackendClient) -> None:
    st.markdown("### Coffee Data Dashboard")
    st.markdown("---")

    df_full = _load_data()

    if df_full.empty:
        st.warning("Dataset not found. Expected: ADV_Python_Midterm_Team1_Nova/data_clean/master_hi_2010_2019.csv")
        return

    # ── Filters ───────────────────────────────────────────────────────────────
    countries = sorted(df_full["country"].unique().tolist())
    f1, f2 = st.columns([1, 2])
    with f1:
        selected_country = st.selectbox("Country", ["All"] + countries, key="dash_country")
    with f2:
        year_range = st.slider(
            "Year",
            min_value=int(df_full["year"].min()),
            max_value=int(df_full["year"].max()),
            value=(int(df_full["year"].min()), int(df_full["year"].max())),
            key="dash_years",
        )

    df = df_full[
        (df_full["year"] >= year_range[0]) & (df_full["year"] <= year_range[1])
    ]
    if selected_country != "All":
        df_country = df[df["country"] == selected_country]
    else:
        df_country = df

    st.markdown("---")

    # ── Chart 1: Coffee Consumption by Country (horizontal bar) ───────────────
    st.markdown("#### Coffee Consumption by Country")
    top_n = 12
    country_avg = (
        df.groupby("country")["coffee_kg_pc"]
        .mean()
        .sort_values(ascending=False)
        .head(top_n)
        .sort_values(ascending=True)
    )
    fig1, ax1 = plt.subplots(figsize=(9, max(3, len(country_avg) * 0.45)))
    bars = ax1.barh(country_avg.index, country_avg.values, color=_CHART_COLOR, height=0.6)
    ax1.set_xlabel("Avg Consumption (kg / person / year)", fontsize=9)
    ax1.xaxis.set_major_formatter(mticker.FormatStrFormatter("%.1f"))
    ax1.tick_params(labelsize=8)
    ax1.grid(axis="x", alpha=0.25, linestyle="--")
    ax1.spines[["top", "right"]].set_visible(False)
    for bar in bars:
        w = bar.get_width()
        ax1.text(w + 0.05, bar.get_y() + bar.get_height() / 2,
                 f"{w:.1f}", va="center", fontsize=7, color="#555")
    plt.tight_layout()
    st.pyplot(fig1, use_container_width=True)
    plt.close(fig1)

    st.markdown("---")

    # ── Chart 2: Consumption Over Time (line) ────────────────────────────────
    st.markdown("#### Coffee Consumption Over Time")
    if selected_country != "All":
        line_df = (
            df_country.groupby("year")["coffee_kg_pc"].mean().reset_index().sort_values("year")
        )
        line_label = selected_country
    else:
        line_df = (
            df.groupby("year")["coffee_kg_pc"].mean().reset_index().sort_values("year")
        )
        line_label = "Global average (high-income)"

    fig2, ax2 = plt.subplots(figsize=(9, 3.5))
    ax2.plot(line_df["year"], line_df["coffee_kg_pc"],
             marker="o", color=_LINE_COLOR, linewidth=2, markersize=5)
    ax2.fill_between(line_df["year"], line_df["coffee_kg_pc"], alpha=0.15, color=_LINE_COLOR)
    ax2.set_xlabel("Year", fontsize=9)
    ax2.set_ylabel("kg / person / year", fontsize=9)
    ax2.set_title(line_label, fontsize=9, color="#555")
    ax2.tick_params(labelsize=8)
    ax2.grid(alpha=0.25, linestyle="--")
    ax2.spines[["top", "right"]].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig2, use_container_width=True)
    plt.close(fig2)

    st.markdown("---")

    # ── Charts 3 & 4: Scatter plots ───────────────────────────────────────────
    sc1, sc2 = st.columns(2)

    with sc1:
        st.markdown("#### GDP vs Coffee Consumption")
        scatter_df = df.groupby("country")[["gdp_pc", "coffee_kg_pc"]].mean().reset_index()
        fig3, ax3 = plt.subplots(figsize=(5, 3.8))
        ax3.scatter(scatter_df["gdp_pc"], scatter_df["coffee_kg_pc"],
                    color=_SCATTER_COLOR, alpha=0.75, edgecolors="#8B6914", linewidth=0.5, s=50)
        ax3.set_xlabel("GDP per capita (USD)", fontsize=8)
        ax3.set_ylabel("Coffee (kg/person/yr)", fontsize=8)
        ax3.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x/1000:.0f}k"))
        ax3.tick_params(labelsize=7)
        ax3.grid(alpha=0.25, linestyle="--")
        ax3.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig3, use_container_width=True)
        plt.close(fig3)

    with sc2:
        st.markdown("#### Work Hours vs Coffee Consumption")
        work_df = df.groupby("country")[["hours_worked", "coffee_kg_pc"]].mean().reset_index()
        fig4, ax4 = plt.subplots(figsize=(5, 3.8))
        ax4.scatter(work_df["hours_worked"], work_df["coffee_kg_pc"],
                    color=_CHART_COLOR, alpha=0.75, edgecolors="#3B1A0A", linewidth=0.5, s=50)
        ax4.set_xlabel("Avg Hours Worked / Year", fontsize=8)
        ax4.set_ylabel("Coffee (kg/person/yr)", fontsize=8)
        ax4.tick_params(labelsize=7)
        ax4.grid(alpha=0.25, linestyle="--")
        ax4.spines[["top", "right"]].set_visible(False)
        plt.tight_layout()
        st.pyplot(fig4, use_container_width=True)
        plt.close(fig4)
