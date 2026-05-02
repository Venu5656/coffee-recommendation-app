# ☕ Coffee Companion - Barista Bot Feature

## Overview

The **Barista Bot** is a conversational interface that complements the existing recommendation system. Rather than filling out forms, users can chat naturally with the bot about their mood, concerns, and preferences—and the bot will guide them to their perfect brew.

## Architecture

### Core Components

#### `barista_bot.py`
The main conversational engine that:
- Maintains conversation history
- Extracts user intent (mood, concerns, preferences) from natural language
- Tracks context across multiple turns
- Converts conversation context into recommendation parameters

**Key Classes:**
- `BaristaContext`: Dataclass holding extracted user state
  - `mood` (stressed, tired, energetic, relaxed, focused)
  - `concerns` (too bitter, too strong, caffeine sensitive, etc.)
  - `temperature_pref` (hot/cold)
  - `effort_pref` (quick/medium/effort)
  - `location` (cafe/home)

- `BaristaBot`: Main conversational agent
  - `start_conversation()` - Initiates friendly greeting
  - `process_user_input(message)` - Processes and responds to user
  - `get_context()` - Returns extracted BaristaContext
  - `get_recommendation_payload()` - Converts context to recommendation parameters

#### `barista_bot_page.py`
Streamlit UI for the Barista Bot that:
- Displays a chat interface (dark messages = user, light = bot)
- Handles input/output flow
- Shows extracted coffee profile based on conversation
- Generates recommendation from bot's extracted context
- Displays visual recommendation with composition

**Key Functions:**
- `render_barista_bot_page()` - Main UI orchestrator
- `_get_barista_recommendation()` - Generates recommendation from bot context and saves to history

## How It Works

### User Flow
1. User navigates to **👨‍🍳 Barista Bot** page
2. Bot greets with a friendly message
3. User describes their mood/concerns naturally
4. Bot responds contextually and asks follow-up questions
5. Bot extracts structure info (mood, temp preference, location, etc.)
6. User clicks "🎯 Get My Perfect Brew"
7. Bot generates recommendation based on extracted context
8. Recommendation is displayed with composition visualization
9. Recommendation is saved to history

### Intent Extraction

The bot uses keyword matching to detect:

**Moods:**
- `stress|stressed|anxious` → "stressed"
- `tired|sleepy|exhausted` → "tired"
- `energy|energetic|pumped` → "energetic"
- `relax|chill|calm` → "relaxed"
- `focus|work|concentrate` → "focused"

**Concerns:**
- "too bitter" → skip bold/intense drinks
- "too strong" → suggest creamier options
- "too sweet" → reassure about natural drinks
- "caffeine sensitive" → suggest medium/low caffeine
- "stomach sensitive" → suggest gentler options
- "want something new" → suggest trending/adventurous drinks

**Temperature & Location:**
- "cold|ice" → cold preference
- "home|make" → home location
- "cafe|shop|order" → cafe location

### How It Differs from "Chat" Tab in Recommend

| Feature | Recommend (Chat Tab) | Barista Bot |
|---------|---------------------|------------|
| Purpose | Quick form-filling via NLP | Conversational guidance |
| Interface | Single text input → recommendation | Multi-turn chat |
| Context | Extract and immediately recommend | Build context over conversation |
| User Goal | Quickly specify preferences | Elaborate and refine preferences |
| Concern Handling | Detect in single message | Explore across multiple turns |

**Analogy:** Recommend's Chat tab is like quickly ordering ("I'll have a cappuccino"); Barista Bot is like actually talking to a barista ("I'm stressed and want something smooth but energizing...").

## Integration with Recommendation Engine

When user clicks "Get My Perfect Brew", the bot:
1. Calls `barista.get_recommendation_payload()` to convert context to:
   ```python
   {
       "mood": "stressed",
       "taste_preference": "bold",
       "time_of_day": "morning",
       "temperature_preference": "hot",
       "effort_level": "medium",
       "caffeine_preference": "high",
       "location": "cafe"
   }
   ```
2. Passes payload to `backend_client.get_recommendation(payload)`
3. Receives recommendation: `{"recommended_drink", "match_score", "explanation", "warning"}`
4. Saves to history via `HistoryTracker`
5. Displays with visual composition using `visualization.render_hot_cup()` or `render_cold_glass()`

## Session State Management

Uses Streamlit session state to preserve:
- `st.session_state.barista_bot` - BaristaBot instance
- `st.session_state.barista_bot_messages` - Full conversation history
- `st.session_state.barista_bot_started` - Flag to avoid re-running initialization

## Extensibility

### Future Enhancements
1. **Multi-language support** - Detect language and respond accordingly
2. **Richer context tracking** - Remember dietary restrictions, allergies
3. **Recommendation refinement** - "Not quite right? Tell me why..." → rerank
4. **Learning** - Improve suggestions based on user ratings over time
5. **Integration with history** - "Show me what I usually get" → context-aware suggestions

### Adding New Concerns
Edit `BaristaBot.CONCERN_RESPONSES` dict in `barista_bot.py`:
```python
CONCERN_RESPONSES = {
    "too bitter": "...",
    "your_new_concern": "Response text here",
}
```

Then add keyword matching in `process_user_input()`:
```python
concern_keywords = {
    # ... existing
    "keyword1|keyword2": "your_new_concern",
}
```

## Design Decisions

1. **Keyword-based Intent Extraction** vs. LLM
   - ✅ Pro: Fast, deterministic, no external API
   - ✅ Pro: Works offline with mock data
   - ⚠️ Con: Less sophisticated than NLP
   - Future: Can swap to OpenAI API for richer extraction

2. **Separate from "Chat" Tab**
   - ✅ Different UX intent: conversational vs. quick
   - ✅ Independent session state
   - ✅ Easier to A/B test / iterate separately

3. **JSON-based Session Storage**
   - ✅ Simple, no database needed
   - ✅ Human-readable for debugging
   - ⚠️ Not suitable for production scale

## Styling

Uses ROWA minimalist theme:
- User messages: Dark background (#0A0A0A) with white text
- Bot messages: Light background (#E0E0E0) with dark text
- Profile cards: Clean layout with clear spacing
- Button: Primary action style (black background)
- Overall: 0px border-radius, flat design

## Files Modified/Created

- ✅ **barista_bot.py** - Core conversation engine
- ✅ **barista_bot_page.py** - Streamlit UI
- ✅ **app.py** - Added navigation entry & routing
- 📝 **theme.py** - Used for styling (no changes needed)
- 📝 **history.py** - Used for saving recommendations (no changes needed)
- 📝 **visualization.py** - Used for composition display (no changes needed)
