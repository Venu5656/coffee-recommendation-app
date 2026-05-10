from __future__ import annotations

import os
from dataclasses import dataclass, field
from typing import Any

import pandas as pd

try:
    import requests as _requests
except Exception:  # pragma: no cover
    _requests = None  # type: ignore[assignment]

_DEFAULT_URL = os.getenv("BACKEND_URL", "http://localhost:8787/api")

# Max possible raw score from recommendation.js ATTRIBUTE_WEIGHTS (sum = 21)
_MAX_SCORE = 21


def _sweetness_label(value: int) -> str:
    if value < 34:
        return "not-sweet"
    if value < 67:
        return "lightly-sweet"
    return "sweet"


def _map_preferences(payload: dict[str, Any]) -> dict[str, Any]:
    mood_raw = str(payload.get("mood", "")).lower()
    mood = {
        "stressed": "tired",
        "focused": "energetic",
        "cozy": "relaxed",
        "comfort": "relaxed",
        "productive": "energetic",
    }.get(mood_raw, mood_raw)

    effort_raw = str(payload.get("effort_level", "")).lower()
    effort = {
        "quick": "quick",
        "minimal": "quick",
        "low": "quick",
        "medium": "elaborate",
        "moderate": "elaborate",
        "hands-on": "elaborate",
        "elaborate": "elaborate",
    }.get(effort_raw, "quick")

    taste_raw = str(payload.get("taste_preference", "")).lower()
    taste = {
        "bold": "bitter",
        "intense": "bitter",
        "balanced": "smooth",
        "creamy": "smooth",
        "mild": "smooth",
        "smooth": "smooth",
        "sweet": "sweet",
        "chocolatey": "sweet",
    }.get(taste_raw, taste_raw)

    time_raw = str(payload.get("time_of_day", "")).lower()
    time = {"evening": "night"}.get(time_raw, time_raw)

    temperature_raw = str(payload.get("temperature_preference", "hot")).lower()
    temperature = {"cold": "iced", "ice": "iced"}.get(temperature_raw, temperature_raw)

    return {
        "mood":                mood,
        "taste":               taste,
        "time":                time,
        "temperature":         temperature,
        "effort":              effort,
        "caffeinePreference":  payload.get("caffeine_preference", "medium"),
        "sweetnessPreference": payload.get(
            "sweetness_preference",
            _sweetness_label(int(payload.get("sweetness_level", 50))),
        ),
        "texturePreference":   payload.get("texture_preference", ""),
        "drinkStyle":          payload.get("drink_style", ""),
        "trySomethingNew":     bool(payload.get("try_something_new", False)),
    }


@dataclass
class CoffeeBackendClient:
    base_url: str = field(default_factory=lambda: _DEFAULT_URL)
    use_mock: bool = False
    timeout_seconds: int = 8
    _token: str = field(default="", repr=False, compare=False)
    last_error: str = field(default="", init=False, repr=False, compare=False)

    def server_status(self) -> dict[str, Any]:
        data = self._get_json("/health")
        return data if isinstance(data, dict) else {}

    # ── Public API ─────────────────────────────────────────────────────────

    def health_check(self) -> bool:
        data = self.server_status()
        return isinstance(data, dict) and data.get("ok") is True

    def login(self, email: str, password: str) -> dict[str, Any] | None:
        data = self._post_json("/auth/login", {"email": email, "password": password})
        if data and "token" in data:
            self._token = data["token"]
        return data

    def register(self, name: str, email: str, password: str) -> dict[str, Any] | None:
        data = self._post_json("/auth/register", {"name": name, "email": email, "password": password})
        if data and "token" in data:
            self._token = data["token"]
        return data

    def logout(self) -> None:
        self._token = ""

    def get_recommendation(self, payload: dict[str, Any]) -> dict[str, Any]:
        if self.use_mock:
            if self.health_check():
                self.use_mock = False
            else:
                return self._mock_recommendation(payload)

        preferences = _map_preferences(payload)
        data = self._post_json("/recommend", {"preferences": preferences})
        if data and "drink" in data:
            drink = data["drink"]
            raw = data.get("score", 0)
            pct = round(min(100, max(0, raw / _MAX_SCORE * 100)))
            return {
                "recommended_drink": drink.get("name", "Unknown"),
                "match_score":       pct,
                "caffeine_level":    drink.get("caffeineLevel", ""),
                "preparation_effort": drink.get("effort", ""),
                "description":       drink.get("description", ""),
                "composition":       drink.get("composition", {}),
                "explanation":       data.get("reasoning", ""),
                "alternatives":      [d.get("name") for d in data.get("alternatives", [])],
                "_from_backend":     True,
            }
        return self._mock_recommendation(
            payload, note="Backend unavailable — showing mock response."
        )

    def chat(
        self,
        message: str,
        history: list[dict[str, Any]] | None = None,
        messages: list[dict[str, str]] | None = None,
    ) -> dict[str, Any] | None:
        """Ask the backend barista assistant for the same response used by the web app."""
        if self.use_mock:
            if self.health_check():
                self.use_mock = False
            else:
                self.last_error = "Backend mock mode is enabled."
                return None
        return self._post_json(
            "/chat",
            {
                "message": message,
                "history": history or [],
                "messages": messages or [],
            },
        )

    def get_insights(self) -> list[str]:
        if self.use_mock:
            return self._mock_insights()

        data = self._get_json("/insights")
        if isinstance(data, dict) and isinstance(data.get("insights"), list):
            out = []
            for item in data["insights"]:
                if isinstance(item, dict):
                    title = item.get("title", "")
                    body  = item.get("body", "")
                    out.append(f"{title}: {body}" if title else body)
                else:
                    out.append(str(item))
            return out
        return self._mock_insights()

    def get_dashboard_data(self, country: str | None = None, year: int | None = None) -> pd.DataFrame:
        # Backend has no /dashboard endpoint — always use local mock data
        return self._mock_dashboard_df(country, year)

    # ── HTTP helpers ───────────────────────────────────────────────────────

    def _headers(self) -> dict[str, str]:
        h: dict[str, str] = {}
        if self._token:
            h["Authorization"] = f"Bearer {self._token}"
        return h

    def _post_json(self, endpoint: str, payload: dict[str, Any]) -> dict[str, Any] | None:
        self.last_error = ""
        if not self.base_url.strip() or _requests is None:
            self.last_error = "Backend client is not available."
            return None
        try:
            resp = _requests.post(
                f"{self.base_url.rstrip('/')}{endpoint}",
                json=payload,
                headers=self._headers(),
                timeout=self.timeout_seconds,
            )
            if not resp.ok:
                try:
                    data = resp.json()
                    if isinstance(data, dict):
                        self.last_error = str(data.get("error") or data.get("message") or resp.reason)
                    else:
                        self.last_error = resp.reason
                except Exception:
                    self.last_error = resp.text.strip() or resp.reason
                return None
            resp.raise_for_status()
            data = resp.json()
            return data if isinstance(data, dict) else None
        except Exception as exc:
            self.last_error = str(exc)
            return None

    def _get_json(self, endpoint: str) -> dict[str, Any] | None:
        self.last_error = ""
        if not self.base_url.strip() or _requests is None:
            self.last_error = "Backend client is not available."
            return None
        try:
            resp = _requests.get(
                f"{self.base_url.rstrip('/')}{endpoint}",
                headers=self._headers(),
                timeout=self.timeout_seconds,
            )
            if not resp.ok:
                try:
                    data = resp.json()
                    if isinstance(data, dict):
                        self.last_error = str(data.get("error") or data.get("message") or resp.reason)
                    else:
                        self.last_error = resp.reason
                except Exception:
                    self.last_error = resp.text.strip() or resp.reason
                return None
            resp.raise_for_status()
            data = resp.json()
            return data if isinstance(data, dict) else None
        except Exception as exc:
            self.last_error = str(exc)
            return None

    # ── Mock fallbacks ─────────────────────────────────────────────────────

    def _mock_recommendation(self, payload: dict[str, Any], note: str = "") -> dict[str, Any]:
        temperature = str(payload.get("temperature_preference", "hot")).lower()
        taste       = str(payload.get("taste_preference", "balanced")).lower()
        caffeine    = str(payload.get("caffeine_preference", "medium")).lower()

        if temperature in {"iced", "cold"}:
            drink = "Cold Brew" if caffeine == "high" else "Iced Latte"
        elif taste in {"bold", "intense"}:
            drink = "Espresso"
        elif taste in {"sweet", "chocolatey"}:
            drink = "Latte"
        else:
            drink = "Americano"

        _compositions = {
            "Cold Brew":   {"coffee": 85, "milk": 15},
            "Iced Latte":  {"coffee": 25, "milk": 65, "ice": 10},
            "Espresso":    {"coffee": 100},
            "Latte":       {"coffee": 20, "milk": 70, "foam": 10},
            "Americano":   {"coffee": 40, "water": 60},
        }

        return {
            "recommended_drink":  drink,
            "match_score":        86,
            "caffeine_level":     caffeine,
            "preparation_effort": str(payload.get("effort_level", "medium")),
            "explanation":        f"{drink} fits your current mood and taste preferences.",
            "warning":            note,
            "composition":        _compositions.get(drink, {"coffee": 60, "milk": 40}),
            "_from_backend":      False,
        }

    def _mock_dashboard_df(self, country: str | None, year: int | None) -> pd.DataFrame:
        rows = [
            {"country": "USA",     "year": 2018, "coffee_consumption": 4.3, "gdp_per_capita": 63000},
            {"country": "USA",     "year": 2019, "coffee_consumption": 4.4, "gdp_per_capita": 65000},
            {"country": "Germany", "year": 2018, "coffee_consumption": 5.1, "gdp_per_capita": 47000},
            {"country": "Germany", "year": 2019, "coffee_consumption": 5.2, "gdp_per_capita": 48000},
            {"country": "Japan",   "year": 2018, "coffee_consumption": 3.6, "gdp_per_capita": 40000},
            {"country": "Japan",   "year": 2019, "coffee_consumption": 3.8, "gdp_per_capita": 41000},
        ]
        df = pd.DataFrame(rows)
        if country:
            df = df[df["country"] == country]
        if year:
            df = df[df["year"] == year]
        return df

    def _mock_insights(self) -> list[str]:
        return [
            "Stable habits in high-income countries: Coffee consumption tends to remain steady in wealthier countries, suggesting mature routines rather than sudden spikes.",
            "Work intensity is not everything: Higher work intensity did not translate into higher coffee consumption. In several cases the relationship moved in the opposite direction.",
            "GDP growth is a weak signal: Economic growth alone had limited explanatory power — coffee demand is not simply a byproduct of short-term macroeconomic change.",
            "Culture shapes the cup: Regional norms, rituals, and taste preferences were stronger drivers than broad economic indicators, reinforcing coffee as a cultural behavior.",
        ]
