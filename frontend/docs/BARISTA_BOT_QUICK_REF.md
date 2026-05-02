# Barista Bot Quick Reference

## 🚀 Quick Start

The Barista Bot is now live! Navigate to **👨‍🍳 Barista Bot** in the sidebar to access it.

### User Interaction Flow
```
Chat naturally → Bot extracts intent → Profile updates → Get recommendation → Save to history
```

## 🎯 What Users Can Do

### Express Their Mood
- "I'm stressed from work"
- "Feeling tired, need a pick-me-up"
- "Just want to relax with something smooth"
- "I need to focus for a meeting"

### Share Concerns
- "I can't do strong coffee"
- "Too much caffeine keeps me up"
- "My stomach is sensitive"
- "I want something new"
- "Too sweet gives me a headache"

### Specify Preferences
- "Cold drink at home"
- "Something quick at the cafe"
- "Something I can prep at home"
- "Just grab and go"

### Get Perfect Recommendation
Click **"🎯 Get My Perfect Brew"** to receive a drink matched to their conversation.

## 🏗️ Architecture at a Glance

### barista_bot.py
```
BaristaBot
├── start_conversation()     → Friendly greeting
├── process_user_input()     → Extract intent & respond
├── get_context()            → Return BaristaContext
└── get_recommendation_payload()  → Convert to recommendation params
```

### barista_bot_page.py
```
render_barista_bot_page()
├── Initialize BaristaBot
├── Display chat interface
├── Handle user input
├── Show extracted profile
├── Generate recommendation
└── Save to history
```

### Integration Points
- Uses `BaristaContext` to track user state
- Calls `backend_client.get_recommendation()` for drink suggestions
- Saves to `HistoryTracker` for session persistence
- Displays with `visualization.render_hot_cup/cold_glass()`

## 🔍 Intent Extraction Examples

### Mood Recognition
```
User: "I'm stressed"
Bot detects: mood = "stressed"
Suggests: bold, high-caffeine coffee for energy
```

### Concern Detection
```
User: "My stomach has been sensitive"
Bot detects: concern = "stomach sensitive"
Suggests: gentler, less acidic options
```

### Preference Extraction
```
User: "Cold drink at the cafe"
Bot detects: 
  - temperature_pref = "cold"
  - location = "cafe"
Adjusts: recommends iced drinks available at cafe
```

## 🎨 UI Features

### Chat Bubbles
- **Dark (user)**: Black background, white text
- **Light (bot)**: Light gray background, dark text

### Live Profile Display
Shows extracted preferences:
- Mood
- Temperature
- Location
- Effort Level
- Concerns (if any)

### Recommendation Display
- Drink name & match score
- Explanation from bot
- Visual composition (hot cup or cold glass)
- Why the bot recommended this

## 🔗 How It Connects to Existing System

1. **Recommend Page** → Form + Chat + Discover modes
2. **Barista Bot Page** → NEW: Conversational guidance mode
3. **My History** → Saves recommendations from all modes (including Barista Bot)
4. **Insights** → Analyzes patterns from all recommendations
5. **Backend Client** → Same recommendation engine

All modes feed into the same history & insights system.

## 🧠 Intent Extraction Keywords

### Moods
| User Says | Detected As |
|-----------|------------|
| stressed, anxious, worry | stressed |
| tired, sleepy, exhausted | tired |
| energy, pumped, hyped | energetic |
| relax, chill, calm | relaxed |
| focus, work, concentrate | focused |

### Concerns
| User Says | Detected As |
|-----------|------------|
| too bitter, bitter | too bitter |
| too strong, strong | too strong |
| too sweet, sugar | too sweet |
| caffeine, won't sleep | caffeine sensitive |
| stomach, sensitive, upset | stomach sensitive |
| new, adventurous, try | want something new |

### Temperature
| User Says | Detected As |
|-----------|------------|
| cold, ice, iced | cold |
| hot, warm, steaming | hot |

### Location
| User Says | Detected As |
|-----------|------------|
| home, make, brew | home |
| cafe, shop, order, buy | cafe |

## 📊 Session State

Uses Streamlit session to track:
- `barista_bot` - BaristaBot instance
- `barista_bot_messages` - Full chat history
- `barista_bot_started` - Initialization flag

Persists across app interactions within a session.

## 🔄 Recommendation Flow

```
User Chat → process_user_input() 
    ↓
Extract Intent (mood, concerns, preferences)
    ↓
get_recommendation_payload()
    ↓
backend_client.get_recommendation(payload)
    ↓
Display recommendation + composition
    ↓
Save to history via HistoryTracker
```

## 🎯 Key Differences from "Chat" Mode

| Aspect | Chat Tab | Barista Bot |
|--------|----------|------------|
| Purpose | Quick NLP form fill | Extended conversation |
| Turns | Single input | Multi-turn |
| Context | Extract once | Build gradually |
| Concerns | Quick detect | In-depth discussion |
| UX | Input → Result | Chat conversation |

## 🚀 Future Enhancement Ideas

1. **AI Upgrade** - Use OpenAI API for richer NLP
2. **Refinement** - "That's not quite right..." → rerank
3. **Learning** - Remember user feedback over time
4. **Memory** - "Show me my usual order"
5. **Allergies** - Track dietary restrictions
6. **Recipes** - Suggest home brewing techniques
7. **Multi-language** - Support Spanish, French, etc.

## 📝 Code Examples

### Starting a Barista Conversation
```python
from barista_bot import BaristaBot

bot = BaristaBot()
greeting = bot.start_conversation()
# "☕ Hey there! I'm your barista bot. What brings you in today?"
```

### Processing User Input
```python
response = bot.process_user_input("I'm stressed from work")
# "I hear you're stressed. Would you prefer a bold energizer 
#  or something smooth to calm down?"

context = bot.get_context()
# BaristaContext(mood='stressed', concerns=[], ...)
```

### Getting Recommendation Payload
```python
payload = bot.get_recommendation_payload()
# {
#     'mood': 'stressed',
#     'taste_preference': 'bold',
#     'caffeine_preference': 'high',
#     'temperature_preference': 'hot',
#     'location': 'cafe',
#     ...
# }
```

## 🎓 Design Philosophy

**Conversational, not Transactional**
- User feels heard (not just form-filled)
- Bot provides guidance (not just recommendations)
- Concerns matter (not just preferences)

**Minimal but Contextual**
- No unnecessary clicks
- Information extracted in conversation
- Profile builds naturally

**Complementary, not Replacement**
- Barista Bot = in-depth exploration
- Chat Tab = quick form-filling
- Form Tab = structured selection
- Users choose their journey

---

## ✅ Status
- ✅ Core engine complete
- ✅ UI integrated
- ✅ Navigation working
- ✅ Ready for testing
- ✅ Extensible for future enhancements

**Next:** Run `streamlit run app.py` and test the Barista Bot! 👨‍🍳☕
