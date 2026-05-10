# Coffee Recommendation System with Data-Driven Insight Integration

This project turns a midterm analysis of global coffee consumption into a user-facing product. It combines a coffee recommendation engine, a conversational barista assistant, personalized history, a dashboard, coffee-composition visuals, and a separate insight section that presents the original analysis without influencing recommendation logic.

## Project overview

The app has two main layers:

- `frontend/`: the primary Streamlit UI your team is using now
- `server/`: the Node.js + Express API that powers recommendations, chat, auth, and persistence

Shared recommendation data and logic live in `shared/` so the backend stays consistent across recommendation flows.

## What the app does

- Recommends coffee from structured user preferences
- Supports a conversational barista assistant
- Encourages discovery with exploration-mode behavior
- Visualizes drink composition
- Tracks user history and preferences
- Shows coffee history, traditions, and consumption insights separately from recommendations

## How this extends the midterm analysis

The earlier analysis found that:

- coffee consumption is relatively stable in high-income countries
- GDP growth has limited direct explanatory power
- work intensity can relate inversely to consumption in some contexts
- culture and region matter more than simple economic indicators

Those insights appear in the app as their own educational and visual section. They are intentionally separated from recommendation logic, so the app preserves the original analytical findings without using them to decide what drink a person should receive.

## Current app architecture

### 1. Streamlit frontend

The current main UI is in `frontend/`.

Key files:

- `frontend/frontend.py`: app entrypoint and page routing
- `frontend/recommendation_engine.py`: form-based recommendation page
- `frontend/barista_bot_page.py`: barista chat UI
- `frontend/dashboard.py`: user dashboard
- `frontend/history.py`: history and session tracking UI
- `frontend/insights.py`: “Did You Know?” and data-insight views
- `frontend/visualization.py`: drink rendering and composition visuals
- `frontend/backend_client.py`: adapter between Streamlit and the API
- `frontend/theme.py`: custom UI styling
- `frontend/coffee_profiles.json`: frontend drink metadata used by the Streamlit UI

### 2. Backend API

The backend is in `server/`.

Key files:

- `server/src/index.js`: Express server startup
- `server/src/routes/api.js`: API routes
- `server/src/db.js`: PostgreSQL connection and schema bootstrap
- `server/src/services/authService.js`: registration/login/token logic
- `server/src/services/historyService.js`: persistent user event history
- `server/src/services/chatService.js`: local barista assistant behavior
- `server/src/middleware/auth.js`: auth middleware

### 3. Shared domain logic

Reusable coffee logic lives in `shared/`.

Key files:

- `shared/coffeeProfiles.js`: coffee profile catalog
- `shared/recommendation.js`: recommendation scoring and reasoning
- `shared/personalization.js`: adaptive preference modeling
- `shared/dashboard.js`: derived dashboard data
- `shared/insights.js`: data-insight content
- `shared/baristaKnowledge.js`: barista knowledge topics and off-menu drinks

### 4. Legacy React frontend

There is also a `client/` folder containing an earlier React/Vite frontend. It is still in the repo, but the current teammate-built UI is the Streamlit app in `frontend/`.

## Core product features

### Filter-based recommendation

The recommendation engine scores drinks using user-facing signals such as:

- mood
- taste
- time of day
- temperature
- effort
- caffeine preference
- sweetness preference
- texture preference
- drink style

The output includes:

- drink name
- description
- caffeine level
- effort
- alternatives
- reasoning text

### Conversational barista assistant

The current chatbot is a local domain assistant, not a general-purpose LLM.

It can:

- recommend drinks from free-form text
- keep recommendations aligned with the same backend engine used by the structured recommender
- guide users on how to make drinks at home
- answer coffee history and tradition questions
- explain brewing methods, bean types, roast levels, and coffee terms
- suggest off-menu drinks like Vietnamese Iced Coffee or Espresso Tonic

### Exploration and discovery

The system supports controlled novelty so recommendations do not stay trapped in the same comfort zone. When the input or user pattern indicates exploration, the engine can shift toward nearby but less expected drinks.

### Personalization

The app stores user events and feedback to improve recommendations over time. Personalized behavior is based on:

- saved recommendations
- likes/dislikes
- repeated patterns
- learned preference tendencies

### Dashboard

The dashboard is designed to summarize a user’s coffee behavior with elements like:

- passport-style identity summary
- taste profile
- time-based drink behavior
- mood-based drink recall
- exploration score
- top drinks
- habit insights

### Data insight section

The “Did You Know?” section and related insight views present:

- midterm findings
- global coffee patterns
- country-level trends
- coffee traditions and history

These are kept separate from recommendation outputs.

## Recommendation model

The recommendation system is rule-based with weighted scoring and personalization.

It uses:

- explicit preference matching
- mismatch penalties when a drink conflicts with direct user intent
- adaptive user-history weighting
- exploration handling
- reasoning generation

Important design rule:

- explicit current user intent should outrank passive history bias

That prevents the system from overfitting to old habits when the user asks clearly for something different.

## Chatbot design

The current chatbot does not rely on the OpenAI API.

Instead, it uses:

- intent classification
- keyword and phrase-based preference extraction
- coffee-domain knowledge retrieval
- conversation-state-aware refinement
- the same backend recommendation model used by the form flow

This makes it more consistent with the product, even though it is narrower than a true general LLM.

## Authentication and database behavior

The backend supports:

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `GET /api/history`
- `GET /api/dashboard`
- `POST /api/feedback`

Accounts and persistent user history are intended to use PostgreSQL.

Important current behavior:

- if PostgreSQL is not configured, the app still runs in guest mode
- recommendation and chat features still work
- real account creation/login should be treated as unavailable until the database is configured

In other words:

- guest usage works without a database
- persistent multi-user accounts require PostgreSQL

## PostgreSQL setup

The backend reads either:

- `DATABASE_URL`

or individual variables:

- `PGHOST`
- `PGPORT`
- `PGUSER`
- `PGPASSWORD`
- `PGDATABASE`

Optional:

- `PGSSLMODE=require`
- `JWT_SECRET=your_long_random_secret`

Example:

```env
PORT=8787
DATABASE_URL=postgresql://USER:PASSWORD@HOST:5432/DBNAME
JWT_SECRET=replace_this_before_production
PGSSLMODE=require
```

When the backend starts with a valid database, it auto-creates:

- `users`
- `user_events`

## Local development

### 1. Install Node dependencies

```bash
npm install
```

### 2. Create the backend environment file

```bash
cp .env.example .env
```

Then update `.env` with your real values.

### 3. Create the Python virtual environment for the Streamlit UI

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r frontend/requirements.txt
```

### 4. Start the backend

```bash
npm run dev --workspace server
```

### 5. Start the Streamlit frontend

```bash
.venv/bin/python -m streamlit run frontend/frontend.py --server.port 8501 --server.address 127.0.0.1
```

### 6. Open the app

- Streamlit frontend: `http://127.0.0.1:8501`
- Backend health: `http://127.0.0.1:8787/api/health`

## Production notes

For production, you should provide:

- a real PostgreSQL database
- a real `JWT_SECRET`
- environment variables through your host platform

Hosted PostgreSQL providers that fit this project well:

- Railway
- Neon
- Supabase
- Render PostgreSQL

## Repository structure

```text
frontend/
  frontend.py
  backend_client.py
  recommendation_engine.py
  barista_bot_page.py
  dashboard.py
  history.py
  insights.py
  visualization.py
  theme.py
  coffee_profiles.json
  data/cleaned_dataset.csv

server/
  src/
    index.js
    db.js
    routes/api.js
    middleware/auth.js
    services/
      authService.js
      chatService.js
      historyService.js

shared/
  coffeeProfiles.js
  recommendation.js
  personalization.js
  dashboard.js
  insights.js
  baristaKnowledge.js

client/
  src/
    ...
```

## Current status

Implemented:

- Streamlit frontend UI
- Node/Express backend
- coffee profile catalog
- rule-based recommendation engine
- inline reasoning
- local barista assistant
- off-menu drink support
- home brewing guidance
- dashboard and history flows
- data insight section
- PostgreSQL schema bootstrap

Still dependent on environment setup:

- real persistent accounts require a valid PostgreSQL connection
- production deployment requires real environment variables

## Summary

This repo now contains a complete coffee-product stack:

- a polished primary frontend in Streamlit
- an API-driven backend in Node
- shared recommendation and personalization logic
- educational coffee knowledge and insights
- a path to real multi-user persistence through PostgreSQL

The main thing to understand operationally is simple:

- the app can run without PostgreSQL in guest mode
- but real accounts and true profile persistence require a configured database
