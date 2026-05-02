# Barista Bot Architecture Diagram

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Coffee Companion App                         │
│                     (Streamlit App)                             │
└─────────────────────────────────────────────────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    │                   │
          ┌─────────▼──────────┐  ┌────▼──────────────┐
          │    app.py          │  │  Navigation       │
          │  Page Router       │  │  (Sidebar)        │
          └─────────┬──────────┘  └────┬──────────────┘
                    │                   │
        ┌───────────┼───────────────────┼──────────┐
        │           │                   │          │
    ┌───▼───┐   ┌───▼──────┐      ┌─────▼───┐  ┌──▼────┐
    │ Home  │   │ Recommend│      │Barista  │  │History│
    │       │   │ (3 modes)│      │Bot ◄────┼──┤       │
    └───────┘   └───┬──────┘      │  NEW!   │  └──┬────┘
                    │             └─────────┘     │
                    │                             │
        ┌───────────┴──────────┐   ┌──────────────▼──────┐
        │   Insights Page      │   │  All recommendations │
        │                      │   │  saved here!         │
        └──────────────────────┘   └─────────────────────┘
```

## Barista Bot Component Architecture

```
┌──────────────────────────────────────────────────────────────┐
│             barista_bot_page.py (Streamlit UI)               │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Chat Interface                             │  │
│  │  User messages (dark) ◄─ User input ─► Bot reply    │  │
│  │  Bot messages (light)      (light)      (dark)      │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │   Live Profile Display                               │  │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │  │
│  │  │   Mood   │ │   Temp   │ │Location  │ │ Effort  │ │  │
│  │  │─────────│ │─────────│ │─────────│ │────────│ │  │
│  │  │ stressed │ │   hot    │ │  cafe   │ │medium  │ │  │
│  │  └──────────┘ └──────────┘ └──────────┘ └─────────┘ │  │
│  │  Concerns: too strong, caffeine sensitive            │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │      "Get My Perfect Brew" Button                    │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │      Recommendation Display                          │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │ Cappuccino (85% match)                         │ │  │
│  │  │ "Smooth & creamy, perfect for stress relief"   │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  │  ┌─────────────────────────────────────────────────┐ │  │
│  │  │       [Composition Visualization]              │ │  │
│  │  │  Shows: caffeine, sugar, foam, milk layers    │ │  │
│  │  │  (renders hot cup or cold glass)              │ │  │
│  │  └─────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────┘  │
│                           │                                  │
│                           ▼                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Save to History & Display "Why This?"              │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
                           │
                    ┌──────┴──────┐
                    │             │
            ┌───────▼──────┐  ┌───▼──────────┐
            │ barista_bot  │  │ HistoryTracker
            │    .py       │  │ (saves rec)
            └──────────────┘  └──────────────┘
```

## Data Flow: From Chat to Recommendation

```
                    User Input
                        │
                        ▼
          ┌─────────────────────────┐
          │  BaristaBot.           │
          │  process_user_input()  │
          └────────────┬────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
    ┌────────┐  ┌───────────┐  ┌──────────┐
    │Extract │  │ Extract   │  │ Extract  │
    │ Mood   │  │ Concerns  │  │Preferences
    │        │  │           │  │
    │Keywords│  │ Keywords  │  │ Keywords │
    │ Match  │  │ Match     │  │ Match    │
    └────┬───┘  └─────┬─────┘  └────┬─────┘
         │            │             │
         └────────────┼─────────────┘
                      │
                      ▼
          ┌──────────────────────┐
          │  BaristaContext      │
          │  ├─ mood             │
          │  ├─ concerns[]       │
          │  ├─ temperature_pref │
          │  ├─ effort_pref      │
          │  ├─ location         │
          │  └─ preferences{}    │
          └──────────┬───────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ BaristaBot.               │
        │ get_recommendation_payload│
        │()                          │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ Recommendation Payload     │
        │ {                          │
        │  "mood": "stressed",       │
        │  "taste_preference":       │
        │    "smooth",               │
        │  "caffeine_preference":    │
        │    "medium",               │
        │  "temperature": "hot",     │
        │  "location": "cafe",       │
        │  ...                       │
        │ }                          │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ backend_client.           │
        │ get_recommendation()       │
        │ (payload)                  │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │ Recommendation Result      │
        │ {                          │
        │  "recommended_drink":      │
        │    "Cappuccino",           │
        │  "match_score": 0.85,      │
        │  "explanation": "...",     │
        │  "warning": None           │
        │ }                          │
        └────────────┬───────────────┘
                     │
         ┌───────────┼───────────────┐
         │           │               │
         ▼           ▼               ▼
    ┌─────────┐ ┌──────────┐ ┌──────────────┐
    │ Display │ │Load Comp │ │ Save to      │
    │ Drink   │ │-osit-ion │ │ History      │
    │ Card    │ │ (hot cup)│ │              │
    │         │ │(cold    │ │ CoffeeRec    │
    │         │ │  glass) │ │ stored in    │
    │         │ │         │ │ .coffee_h    │
    │         │ │         │ │ istory.json  │
    └─────────┘ └──────────┘ └──────────────┘
```

## Intent Extraction Logic

```
┌─────────────────────────────────────────────────┐
│   User Text: "I'm stressed and cold drinks"     │
└────────────────┬────────────────────────────────┘
                 │
      ┌──────────┼───────────┐
      │          │           │
      ▼          ▼           ▼
  ┌────────┐ ┌───────┐  ┌──────────┐
  │ Mood   │ │Temp   │  │Concerns
  │Extract │ │Extract│  │Extract
  └───┬────┘ └───┬───┘  └────┬─────┘
      │          │           │
 "stressed" "cold"  (none)
      │          │           │
      └──────────┼───────────┘
                 │
                 ▼
      ┌─────────────────────────┐
      │  Updated BaristaContext │
      │  ├─ mood: "stressed"    │
      │  ├─ concerns: []        │
      │  └─ temperature: "cold" │
      └─────────────────────────┘
```

## Files & Dependencies

```
┌──────────────────────────────────────────────────────┐
│                  app.py                             │
│            (Main navigation hub)                    │
└──────┬─────────────────────────────────┬────────────┘
       │                                 │
       ▼                                 ▼
  ┌──────────────┐            ┌─────────────────────┐
  │barista_bot   │            │barista_bot_page.py  │
  │_page.py      │◄──imports──┤(Streamlit UI)       │
  │(Streamlit UI)│            └────────┬────────────┘
  └──────┬───────┘                     │
         │                             │
         └─────────────┬───────────────┘
                       │
           ┌───────────┴────────────┐
           │                        │
           ▼                        ▼
    ┌────────────────┐    ┌──────────────────┐
    │barista_bot.py │    │backend_client.py │
    │(Conversation) │    │(Recommendations) │
    └────────────────┘    └──────────────────┘
           │                        │
           │              ┌─────────┼─────────┐
           │              │         │         │
           ▼              ▼         ▼         ▼
    ┌─────────────┐ ┌──────────┐  coffee  ┌──────────┐
    │ Intent      │ │ History  │ profiles │Dashboard/
    │Extraction   │ │ Tracker  │  .json  │Insights
    │(Keywords)   │ │(Saves)   │         │(Data)
    └─────────────┘ └──────────┘ └────────┴──────────┘
           │                        │
           └────────────┬───────────┘
                        │
                        ▼
              ┌──────────────────┐
              │ visualization.py │
              │(Renders cups/   │
              │ glasses)         │
              └──────────────────┘
```

## Session State Management

```
┌────────────────────────────────────────────┐
│     Streamlit Session State                │
├────────────────────────────────────────────┤
│                                            │
│  st.session_state.barista_bot              │
│  └─ BaristaBot instance                    │
│     ├─ conversation_history[]              │
│     └─ context (BaristaContext)            │
│                                            │
│  st.session_state.barista_bot_messages     │
│  └─ Chat history (for display)             │
│     ├─ [{"role": "barista", "content": }] │
│     ├─ [{"role": "user", "content": }]    │
│     └─ ...                                 │
│                                            │
│  st.session_state.barista_bot_started      │
│  └─ Boolean flag (init check)              │
│                                            │
└────────────────────────────────────────────┘
      Persists during app session
      (cleared on page refresh)
```

## Recommendation Flow Chart

```
                    START
                      │
                      ▼
        ┌─────────────────────────┐
        │ Barista Bot Greeting    │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ User Types Message      │
        │ "I'm stressed..."       │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Extract Intent          │
        │ (mood, concerns, prefs) │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Bot Responds &          │
        │ Updates Profile         │
        └────────────┬────────────┘
                     │
           ┌─────────┴─────────┐
           │                   │
           ▼                   ▼
    ┌──────────────┐   ┌────────────────┐
    │ Continue Chat│   │Get Perfect Brew│
    │              │   │   (Button)     │
    └──────────────┘   └────────┬───────┘
           │                    │
           └────────┬───────────┘
                    │
                    ▼
        ┌─────────────────────────┐
        │ Generate Payload from   │
        │ Extracted Context       │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Call Backend            │
        │ get_recommendation()    │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Display Recommendation  │
        │ + Composition Viz       │
        └────────────┬────────────┘
                     │
                     ▼
        ┌─────────────────────────┐
        │ Save to History         │
        │ (.coffee_history.json)  │
        └────────────┬────────────┘
                     │
                     ▼
                    END
```

## Keyword Matching Decision Tree

```
User Input
    │
    ├─→ Contains mood keywords?
    │   ├─→ YES: Extract mood
    │   └─→ NO: Keep current mood
    │
    ├─→ Contains concern keywords?
    │   ├─→ YES: Add to concerns[]
    │   └─→ NO: Keep current concerns
    │
    ├─→ Contains temperature keywords?
    │   ├─→ "cold/ice" → cold
    │   ├─→ "hot/warm" → hot
    │   └─→ NO MATCH: Keep current
    │
    ├─→ Contains location keywords?
    │   ├─→ "home/make" → home
    │   ├─→ "cafe/shop" → cafe
    │   └─→ NO MATCH: Keep current
    │
    └─→ Update BaristaContext
        Generate Contextual Response
```

This architecture ensures:
- **Separation of Concerns**: UI, logic, and recommendations separated
- **Reusability**: BaristaBot can be used independently
- **Extensibility**: Easy to add moods, concerns, or upgrade NLP
- **Session Persistence**: Chat history persists within session
- **Integration**: Works seamlessly with existing recommendation system

---

*Created: April 28, 2025*
*Status: ✅ Ready for Testing*
