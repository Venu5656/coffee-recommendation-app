# Coffee Companion - Smart Coffee Recommendation App

A beautiful, interactive Streamlit app for personalized coffee recommendations with session tracking, mood analysis, and data insights.

## ✨ Features

### 🏠 Home Page
- Hero landing section
- "How It Works" step-by-step guide
- Quick stats on your session
- Direct navigation to all features

### ☕ Recommendation Engine (3 Modes)
- **📋 Quick Form** — Traditional preference selection (mood, taste, temperature, location, effort)
- **💬 Chat Mode** — Natural language input with NLP parsing ("I'm stressed and need energy" → auto-fills form)
- **🎲 Trending Discovery** — Discover new drinks based on trending selections

### 🥤 Composition Visualization
- **Hot Cup Rendering** — Shows caffeine, sugar, foam, and milk layers
- **Cold Glass Rendering** — Shows ice, coffee, and milk composition
- Nutritional breakdown with mg/percentage displays
- Fun facts about each drink

### 📜 My History
- Session-based recommendation tracking
- Recent orders table with timestamps
- Top drinks frequency chart
- Mood pattern analysis
- Location preference stats

### 📊 Did You Know? (Insights)
- **4 Global Stat Cards:** Global avg consumption, cultural variance, work correlation, GDP effect
- **Per-Capita Chart** — Coffee consumption by country (2010-2019)
- **Stability Trend** — 10-year consumption stability visualization
- **Your Personal Trends:**
  - Top drinks (you've tried this session)
  - Mood distribution pie chart
  - Cafe vs Home preference
  - Fun facts personalized to your history

## 🎨 UI Polish
- **Coffee-themed color palette** (browns, oranges, blues)
- **Custom CSS styling** for cards, buttons, inputs
- **Responsive layout** with 2-3 column grids
- **Icons & emojis** throughout
- **Gradient backgrounds** and smooth transitions

## 📁 Project Structure

```
coffee-recommendation-app/
├── app.py                      # Main navigation hub
├── recommendation_engine.py    # Recommendation UI (3 modes)
├── insights.py                 # Did You Know? + trends
├── history.py                  # Session tracking
├── visualization.py            # Cup/glass composition rendering
├── backend_client.py           # Mock + API adapter
├── theme.py                    # CSS styling
├── coffee_profiles.json        # Drink profiles + composition data
└── README.md
```

## 🚀 Quick Start

```bash
cd /Users/anshureddy/Desktop/ADV_P/coffee-recommendation-app
/Users/anshureddy/Desktop/ADV_P/.venv/bin/python -m streamlit run app.py
```

Visit: `http://localhost:8501`

## 📱 Pages Overview

| Page | Features |
|------|----------|
| **🏠 Home** | Welcome hero + quick stats + CTA buttons |
| **☕ Recommend** | 3 recommendation modes + composition viz |
| **📜 My History** | Session tracking + trend analysis |
| **📊 Insights** | Midterm data + personal trends |

## 🔌 Backend Integration Ready

All data flows through `backend_client.py` with mock implementations ready to swap:

```python
# Current: Mock mode
# Future: Set to Live API mode and connect to teammate's backend
client = CoffeeBackendClient(use_mock=True, base_url="http://backend-api:8000")
```

**Backend Contract:**
- `POST /recommend` — Coffee recommendation
- `POST /dashboard` — Dashboard data
- `POST /insights` — Insight cards
- `POST /chat-parse` — NLP mood parsing (optional)

## 🎯 Current Status: UI PROTOTYPE ✅

- [x] Home page with hero + CTA
- [x] Recommendation form + chat + trending modes
- [x] Composition visualization (hot cup + cold glass)
- [x] Session history tracking
- [x] Midterm insights dashboard
- [x] Custom theme & styling
- [x] Backend client abstraction (mock mode)
- [ ] Backend integration (next step)

## 🌟 Ready for Next Phase

Once your teammate provides the backend endpoints, simply:
1. Switch "Mock Data" → "Live API" in sidebar
2. Paste backend URL
3. All UI stays the same, data comes from real API!

---

**Built for coffee lovers with ☕**
