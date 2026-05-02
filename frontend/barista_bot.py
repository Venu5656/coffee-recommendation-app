from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class BaristaContext:
    """Context from barista conversation."""
    mood: str = "relaxed"
    concerns: list[str] = None
    preferences: dict[str, str] = None
    temperature_pref: str = "hot"
    effort_pref: str = "moderate"
    location: str = "cafe"
    notes: str = ""
    
    def __post_init__(self):
        if self.concerns is None:
            self.concerns = []
        if self.preferences is None:
            self.preferences = {}


class BaristaBot:
    """Conversational barista bot for personalized coffee guidance."""
    
    GREETINGS = [
        "Hey there. I am your barista bot. What brings you in today?",
        "Welcome! Let's find your perfect brew. How are you feeling?",
        "Hi! Tell me about your mood or what you're looking for in a coffee.",
    ]
    
    MOOD_QUESTIONS = {
        "stressed": "I hear you're stressed. Would you prefer a bold energizer or something smooth to calm down?",
        "energetic": "Great energy! Looking for something bold to keep that momentum?",
        "tired": "Feeling tired? Let me suggest something to perk you up.",
        "relaxed": "Nice! Want something smooth and comforting?",
        "focused": "In work mode? I can suggest something to help you concentrate.",
    }
    
    CONCERN_RESPONSES = {
        "too bitter": "Got it—you want smooth and balanced? I'd skip the bold espressos.",
        "too strong": "Something lighter then! How about a creamy latte or cappuccino?",
        "too sweet": "You prefer less sugar? Great—most of our coffees are naturally not too sweet.",
        "caffeine sensitive": "Gotcha. Let me suggest something with medium or low caffeine.",
        "stomach sensitive": "I understand. We can suggest gentler options that are easier on the stomach.",
        "want something new": "Adventurous! Let's try something trending you haven't had before.",
    }
    
    FOLLOW_UP_QUESTIONS = [
        "Any concerns or preferences I should know about? (like bitter taste, caffeine sensitivity, etc.)",
        "Will you be at a café or making it at home?",
        "How much effort do you want to put in? (quick grab vs. home prep)",
        "Any specific flavor you're craving today?",
    ]

    def __init__(self):
        self.conversation_history: list[dict[str, str]] = []
        self.context = BaristaContext()

    def start_conversation(self) -> str:
        """Start the barista conversation."""
        import random
        greeting = random.choice(self.GREETINGS)
        self.conversation_history.append({"role": "barista", "content": greeting})
        return greeting

    def process_user_input(self, user_message: str) -> str:
        """Process user message and return barista response."""
        self.conversation_history.append({"role": "user", "content": user_message})
        
        user_lower = user_message.lower()
        
        # Extract mood from message
        mood_keywords = {
            "stress|stressed|anxious|worry": "stressed",
            "tired|sleepy|exhausted|worn": "tired",
            "energy|energetic|pumped|hyped": "energetic",
            "relax|chill|calm|peace": "relaxed",
            "focus|work|concentrate|produc": "focused",
        }
        
        for keywords, mood in mood_keywords.items():
            if any(keyword in user_lower for keyword in keywords.split("|")):
                self.context.mood = mood
                break
        
        # Extract concerns
        concern_keywords = {
            "bitter|too bitter": "too bitter",
            "strong|too strong": "too strong",
            "sweet|sugar": "too sweet",
            "caffeine": "caffeine sensitive",
            "stomach|sensitive": "stomach sensitive",
            "new|try|different": "want something new",
        }
        
        for keywords, concern in concern_keywords.items():
            if any(keyword in user_lower for keyword in keywords.split("|")):
                if concern not in self.context.concerns:
                    self.context.concerns.append(concern)
        
        # Extract temperature preference
        if "cold" in user_lower or "ice" in user_lower:
            self.context.temperature_pref = "iced"
        elif "hot" in user_lower:
            self.context.temperature_pref = "hot"

        # Extract effort preference
        if any(word in user_lower for word in ("quick", "fast", "grab", "easy", "simple")):
            self.context.effort_pref = "minimal"
        elif any(word in user_lower for word in ("home prep", "brew", "make", "hands", "craft")):
            self.context.effort_pref = "hands-on"
        
        # Extract location
        if "home" in user_lower or "make" in user_lower:
            self.context.location = "home"
        elif "cafe" in user_lower or "shop" in user_lower or "order" in user_lower:
            self.context.location = "cafe"
        
        # Generate response based on detected mood
        response = self._generate_response(user_message)
        self.conversation_history.append({"role": "barista", "content": response})
        
        return response

    def _generate_response(self, user_message: str) -> str:
        """Generate contextual barista response."""
        mood = self.context.mood
        concerns = self.context.concerns
        
        # If we detected concerns, respond to those first
        if concerns:
            concern = concerns[-1]  # Last mentioned concern
            if concern in self.CONCERN_RESPONSES:
                return self.CONCERN_RESPONSES[concern] + " " + self._ask_followup()
        
        # If we detected mood, respond to that
        if mood in self.MOOD_QUESTIONS:
            return self.MOOD_QUESTIONS[mood] + " " + self._ask_followup()
        
        # Default response
        return "Tell me more! What matters most to you in a good coffee? (taste, strength, preparation time, etc.)" + " " + self._ask_followup()

    def _ask_followup(self) -> str:
        """Ask a relevant follow-up question."""
        import random
        # Don't repeat questions already answered
        unanswered = [q for q in self.FOLLOW_UP_QUESTIONS]
        if self.context.location != "cafe":
            unanswered = [q for q in unanswered if "café" not in q]
        
        if unanswered:
            return "\n\n" + random.choice(unanswered)
        return ""

    def get_context(self) -> BaristaContext:
        """Get the current barista context."""
        return self.context

    def get_recommendation_payload(self) -> dict[str, str]:
        """Convert barista context to recommendation payload."""
        # Map mood to taste/caffeine preference
        mood_to_taste = {
            "stressed": "bold",
            "tired": "bold",
            "energetic": "bold",
            "relaxed": "smooth",
            "focused": "balanced",
        }
        
        mood_to_caffeine = {
            "stressed": "high",
            "tired": "high",
            "energetic": "high",
            "relaxed": "medium",
            "focused": "medium",
        }
        
        mood_to_time = {
            "stressed": "morning",
            "tired": "morning",
            "energetic": "afternoon",
            "relaxed": "afternoon",
            "focused": "morning",
        }
        
        return {
            "mood": self.context.mood,
            "taste_preference": mood_to_taste.get(self.context.mood, "balanced"),
            "time_of_day": mood_to_time.get(self.context.mood, "afternoon"),
            "temperature_preference": self.context.temperature_pref,
            "effort_level": self.context.effort_pref,
            "caffeine_preference": mood_to_caffeine.get(self.context.mood, "medium"),
            "location": self.context.location,
        }

    def get_conversation_summary(self) -> str:
        """Get a summary of the conversation."""
        summary = f"""
        **Your Coffee Profile (from our chat):**
        - Mood: {self.context.mood.title()}
        - Temperature: {self.context.temperature_pref.title()}
        - Location: {self.context.location.title()}
        - Effort Level: {self.context.effort_pref.title()}
        """
        
        if self.context.concerns:
            summary += f"\n- Concerns: {', '.join(self.context.concerns)}"
        
        return summary
