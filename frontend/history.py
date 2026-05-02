from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass, asdict, field
import json
from pathlib import Path


@dataclass
class CoffeeRecommendation:
    drink_name: str
    mood: str
    time_of_day: str
    temperature: str
    location: str
    match_score: int
    timestamp: str
    composition: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


class HistoryTracker:
    def __init__(self):
        self.history_file = Path(__file__).parent / ".coffee_history.json"
        self.recommendations: list[CoffeeRecommendation] = self._load_history()

    def _load_history(self) -> list[CoffeeRecommendation]:
        """Load recommendation history from file."""
        if self.history_file.exists():
            try:
                with open(self.history_file) as f:
                    data = json.load(f)
                return [CoffeeRecommendation(**item) for item in data]
            except Exception:
                return []
        return []

    def _save_history(self) -> None:
        """Save recommendation history to file."""
        try:
            with open(self.history_file, "w") as f:
                json.dump([r.to_dict() for r in self.recommendations], f, indent=2)
        except Exception:
            pass

    def add_recommendation(
        self,
        drink_name: str,
        mood: str,
        time_of_day: str,
        temperature: str,
        location: str,
        match_score: int,
        composition: dict | None = None,
    ) -> None:
        """Add a new recommendation to history."""
        rec = CoffeeRecommendation(
            drink_name=drink_name,
            mood=mood,
            time_of_day=time_of_day,
            temperature=temperature,
            location=location,
            match_score=match_score,
            timestamp=datetime.now().isoformat(),
            composition=composition or {},
        )
        self.recommendations.append(rec)
        self._save_history()

    def get_all(self) -> list[CoffeeRecommendation]:
        """Get all recommendations."""
        return self.recommendations

    def get_recent(self, n: int = 10) -> list[CoffeeRecommendation]:
        """Get last n recommendations."""
        return self.recommendations[-n:]

    def get_trending_drinks(self, n: int = 5) -> list[tuple[str, int]]:
        """Get top n most recommended drinks."""
        drink_counts: dict[str, int] = {}
        for rec in self.recommendations:
            drink_counts[rec.drink_name] = drink_counts.get(rec.drink_name, 0) + 1
        return sorted(drink_counts.items(), key=lambda x: x[1], reverse=True)[:n]

    def get_mood_patterns(self) -> dict[str, int]:
        """Get mood frequency patterns."""
        mood_counts: dict[str, int] = {}
        for rec in self.recommendations:
            mood_counts[rec.mood] = mood_counts.get(rec.mood, 0) + 1
        return mood_counts

    def get_location_preference(self) -> dict[str, int]:
        """Get cafe vs home preference."""
        location_counts: dict[str, int] = {}
        for rec in self.recommendations:
            location_counts[rec.location] = location_counts.get(rec.location, 0) + 1
        return location_counts

    def get_stats(self) -> dict[str, str | int]:
        """Get session statistics."""
        if not self.recommendations:
            return {
                "total_drinks": 0,
                "unique_drinks": 0,
                "avg_match_score": 0,
                "favorite_drink": "None yet",
                "favorite_mood": "Not tracked",
            }

        drinks = [r.drink_name for r in self.recommendations]
        unique_drinks = len(set(drinks))
        avg_score = sum(r.match_score for r in self.recommendations) // len(self.recommendations)
        favorite_drink = max(set(drinks), key=drinks.count)
        mood_patterns = self.get_mood_patterns()
        favorite_mood = max(mood_patterns, key=mood_patterns.get) if mood_patterns else "Varied"

        return {
            "total_drinks": len(self.recommendations),
            "unique_drinks": unique_drinks,
            "avg_match_score": avg_score,
            "favorite_drink": favorite_drink,
            "favorite_mood": favorite_mood,
        }
