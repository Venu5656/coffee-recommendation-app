# Barista Bot Feature Summary

## What Was Added

### 1. **barista_bot.py** — Core Conversation Engine
- `BaristaContext` dataclass: Tracks mood, concerns, preferences, temperature, effort level, location
- `BaristaBot` class with:
  - Natural language intent extraction (keyword-based)
  - Multi-turn conversation management
  - Context tracking across exchanges
  - Conversion to recommendation payload
  - Predefined response templates for common moods/concerns

**Key Methods:**
```python
barista = BaristaBot()
greeting = barista.start_conversation()  # Get greeting
response = barista.process_user_input("I'm stressed")  # Get response
context = barista.get_context()  # Extract mood/concerns/prefs
payload = barista.get_recommendation_payload()  # Convert to rec params
```

---

### 2. **barista_bot_page.py** — Streamlit UI Interface
- Chat interface with dark/light message styling
- Real-time conversation display
- Live profile extraction (mood, temperature, location, effort, concerns)
- Integration with recommendation engine & history tracker
- Visual composition display

**User Workflow:**
1. Bot greets user
2. User types natural message
3. Bot extracts intent and responds conversationally
4. Profile updates in real-time
5. User clicks "Get My Perfect Brew"
6. Recommendation appears with composition visualization
7. Saved to history

---

### 3. **app.py** — Navigation Integration
- Added import: `from barista_bot_page import render_barista_bot_page`
- Added navigation option: `"👨‍🍳 Barista Bot"`
- Added page routing:
```python
elif page == "👨‍🍳 Barista Bot":
    render_barista_bot_page()
```

---

## How It Differs from Existing Chat

| Aspect | Recommend → Chat | Barista Bot |
|--------|-----------------|------------|
| User Experience | Single input → immediate recommendation | Multi-turn conversation |
| Purpose | Quick form filling via NLP | Elaborate on mood/concerns |
| Context Building | One-shot extraction | Cumulative across turns |
| Concern Exploration | Detect in single message | Discuss in detail |
| Analogy | "I'll have a cappuccino" | Chat with actual barista |

---

## Key Features

### ✅ Mood Detection
- Recognizes: stressed, tired, energetic, relaxed, focused
- Maps to recommendation preferences (taste, caffeine, time)

### ✅ Concern Tracking
- Detects: too bitter, too strong, too sweet, caffeine sensitive, stomach issues
- Responds with specific guidance
- Influences recommendation filtering

### ✅ Preference Extraction
- Temperature: hot/cold
- Location: cafe/home
- Effort level: quick/medium/involved
- Time of day: morning/afternoon/evening

### ✅ Real-Time Profile
Shows user's extracted profile with:
- Detected mood
- Temperature preference
- Location choice
- Effort level
- Any mentioned concerns

### ✅ Seamless Integration
- Saves recommendations to same history as form/chat
- Uses same backend client & visualization system
- Matches ROWA minimalist design
- Session-based conversation persistence

---

## Conversation Flow Example

**Bot:** "☕ Hey there! I'm your barista bot. What brings you in today?"

**User:** "I'm really stressed from work"

**Bot:** "I hear you're stressed. Would you prefer a bold energizer or something smooth to calm down?"
- [Profile updates: Mood = "stressed"]

**User:** "Something smooth but not too sweet"

**Bot:** "Got it—you want smooth and balanced? Great—most of our coffees are naturally not too sweet."
"Will you be at a café or making it at home?"
- [Profile updates: Concerns = ["too sweet"]]

**User:** "At a cafe"

**Bot:** "Perfect! I've got your profile ready."
- [Profile shows: Mood=Stressed, Temp=Hot, Location=Cafe, Concerns=Too Sweet]

**User clicks: "Get My Perfect Brew"** → Recommendation = Cappuccino (smooth, balanced, cafe-friendly)

---

## Session State Management

The app uses Streamlit session state to maintain conversation:
```python
st.session_state.barista_bot  # BaristaBot instance
st.session_state.barista_bot_messages  # Full conversation history
st.session_state.barista_bot_started  # Init flag
```

Persists across app reruns within same session.

---

## Design Alignment

Styled with **ROWA Minimalist Aesthetic:**
- User messages: Black background (#0A0A0A) with white text
- Bot messages: Light gray (#E0E0E0) with dark text
- 0px border-radius (flat design)
- Poppins typography
- Consistent spacing & alignment

---

## Next Steps (Optional)

1. **Enhanced NLP** — Swap keyword matching for OpenAI API intent extraction
2. **Recommendation Refinement** — Let user say "Not quite right" and rerank
3. **Learning** — Store feedback and improve suggestions over time
4. **History Integration** — "What do I usually order?" for context-aware suggestions
5. **Allergy/Diet Tracking** — Remember dietary restrictions across sessions

---

## Files Created/Modified

| File | Status | Changes |
|------|--------|---------|
| `barista_bot.py` | ✅ Created | Core conversation engine |
| `barista_bot_page.py` | ✅ Created | Streamlit UI interface |
| `app.py` | ✅ Modified | Added import & navigation |
| `theme.py` | - | No changes (used for styling) |
| `history.py` | - | No changes (used for saving) |
| `visualization.py` | - | No changes (used for display) |
| `BARISTA_BOT.md` | ✅ Created | Detailed documentation |

---

## Testing Checklist

- ✅ All imports work (barista_bot, barista_bot_page, app)
- ✅ No syntax errors in any files
- ✅ Navigation includes Barista Bot option
- ✅ Page routing correctly handles Barista Bot selection
- 🔄 Ready for Streamlit UI testing

**To test UI:**
```bash
cd /Users/anshureddy/Desktop/ADV_P/coffee-recommendation-app
streamlit run app.py
```

Then:
1. Click "👨‍🍳 Barista Bot" in sidebar
2. Chat with bot naturally
3. Watch profile extract in real-time
4. Click "Get My Perfect Brew" for recommendation
5. Verify composition visualization displays
6. Check that recommendation was saved to history
