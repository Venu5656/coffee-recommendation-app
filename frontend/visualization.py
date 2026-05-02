from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import streamlit as st


COFFEE_PROFILES_PATH = Path(__file__).parent / "coffee_profiles.json"


def load_coffee_profiles() -> dict[str, Any]:
    """Load coffee profile compositions from JSON."""
    try:
        with open(COFFEE_PROFILES_PATH) as f:
            data = json.load(f)
        return data.get("coffee_profiles", {})
    except Exception:
        return {}


def render_hot_cup(caffeine_mg: int, sugar_g: float, foam_percent: float, milk_percent: float, coffee_percent: float) -> None:
    """Render a hot coffee cup with composition layers."""
    fig, ax = plt.subplots(figsize=(4, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")

    # Cup outline
    from matplotlib.patches import Rectangle, Polygon

    cup = Rectangle((2, 1), 6, 7, fill=False, edgecolor="black", linewidth=2)
    ax.add_patch(cup)

    # Handle
    handle = plt.Circle((8.2, 4.5), 0.5, fill=False, edgecolor="black", linewidth=2)
    ax.add_patch(handle)

    # Layers (bottom to top)
    layer_y = 1

    # Coffee layer
    coffee_height = (coffee_percent / 100) * 6
    coffee_rect = Rectangle((2, layer_y), 6, coffee_height, facecolor="#6F4E37", edgecolor="none")
    ax.add_patch(coffee_rect)
    layer_y += coffee_height

    # Milk layer
    milk_height = (milk_percent / 100) * 6
    if milk_height > 0:
        milk_rect = Rectangle((2, layer_y), 6, milk_height, facecolor="#D4A574", edgecolor="none")
        ax.add_patch(milk_rect)
        layer_y += milk_height

    # Foam layer
    foam_height = (foam_percent / 100) * 6
    if foam_height > 0:
        foam_rect = Rectangle((2, layer_y), 6, foam_height, facecolor="#E8D5C4", edgecolor="none", alpha=0.7)
        ax.add_patch(foam_rect)

    # Labels
    ax.text(9.5, 10, "Hot", fontsize=10, fontweight="bold")
    ax.text(5, 0.3, "Hot Cup", ha="center", fontsize=12, fontweight="bold")

    # Legend
    ax.text(0.5, 11, f"Caffeine: {caffeine_mg}mg", fontsize=9, fontweight="bold")
    ax.text(0.5, 10.5, f"Sugar: {sugar_g}g", fontsize=9)
    ax.text(0.5, 10, f"Foam: {foam_percent}%", fontsize=9)

    st.pyplot(fig, use_container_width=False)
    plt.close(fig)


def render_cold_glass(caffeine_mg: int, sugar_g: float, foam_percent: float, milk_percent: float, coffee_percent: float, ice_percent: float = 30) -> None:
    """Render a cold coffee glass with ice and layers."""
    fig, ax = plt.subplots(figsize=(4, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis("off")

    from matplotlib.patches import Rectangle, Polygon

    # Glass outline
    glass_points = [[2, 1], [2.5, 0.5], [7.5, 0.5], [8, 1], [8, 8], [2, 8]]
    glass = Polygon(glass_points, fill=False, edgecolor="lightblue", linewidth=3)
    ax.add_patch(glass)

    # Ice at bottom
    ice_height = (ice_percent / 100) * 6.5
    ice_rect = Rectangle((2, 1), 6, ice_height, facecolor="#B3D9FF", edgecolor="none", alpha=0.6)
    ax.add_patch(ice_rect)

    layer_y = 1 + ice_height

    # Coffee layer
    coffee_height = (coffee_percent / 100) * 4.5
    if coffee_height > 0:
        coffee_rect = Rectangle((2, layer_y), 6, coffee_height, facecolor="#6F4E37", edgecolor="none")
        ax.add_patch(coffee_rect)
        layer_y += coffee_height

    # Milk layer
    milk_height = (milk_percent / 100) * 4.5
    if milk_height > 0:
        milk_rect = Rectangle((2, layer_y), 6, milk_height, facecolor="#D4A574", edgecolor="none")
        ax.add_patch(milk_rect)

    # Labels
    ax.text(9.5, 10, "Cold", fontsize=10, fontweight="bold")
    ax.text(5, 0, "Cold Glass", ha="center", fontsize=12, fontweight="bold")

    # Legend
    ax.text(0.5, 11, f"Caffeine: {caffeine_mg}mg", fontsize=9, fontweight="bold")
    ax.text(0.5, 10.5, f"Sugar: {sugar_g}g", fontsize=9)
    ax.text(0.5, 10, f"Ice: {ice_percent}%", fontsize=9)

    st.pyplot(fig, use_container_width=False)
    plt.close(fig)
