# Coffee Recommendation System with Data-Driven Insight Integration

This project turns a prior midterm analysis of global coffee consumption into a practical application. It combines a rule-based recommendation engine, an AI chat workflow, PostgreSQL-backed user accounts and history, an exploration layer for variety, a beaker-style ingredient visualization, and a separate "Did You Know?" section that presents the earlier analysis findings without affecting recommendation logic.

## How this extends the midterm analysis

The earlier analysis found that coffee consumption is stable in high-income countries, weakly tied to GDP growth, inversely related to work intensity in several cases, and strongly shaped by cultural context. Those findings appear in the UI as readable insight cards so the project preserves the analytical narrative while keeping recommendation decisions independent.

## Core features

- Filter-based recommendation using mood, taste, time, temperature, and effort
- Shared coffee profile model across rule-based and chat-based recommendation flows
- Exploration mode that occasionally diversifies suggestions outside familiar user patterns
- AI chatbot endpoint that extracts preferences from free text and maps them to the same drink profiles
- PostgreSQL-backed account system with registration, login, and synced recommendation history
- Beaker-style composition graph for ingredient percentages
- Guest-mode local history plus authenticated database persistence for real users
- Separate "Did You Know?" page for prior analytical insights

## Recommendation logic

The backend scores each coffee profile against:

- mood match
- taste match
- time suitability
- temperature compatibility
- effort compatibility
- previous likes in local history

If the user explicitly asks to try something new, or if history shows repetitive patterns, the engine introduces controlled exploration. The system still favors familiar matches most of the time, but it can shift about 20-30% toward a nearby but less expected option.

## Chatbot flow

`POST /api/chat` accepts free-form user text and local interaction history.

- If `OPENAI_API_KEY` is present, the server calls the OpenAI API to extract structured preferences.
- If no API key is configured, the server falls back to keyword-based extraction.
- In both cases, the extracted preferences are passed into the same shared recommendation engine used by the filter flow.

This keeps the chatbot and rule-based recommendation outputs aligned.

## Authentication and persistence

The backend now supports:

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `GET /api/history`
- `POST /api/feedback`

Signed-in users store recommendations and feedback in PostgreSQL. Guests can still browse and test the app without an account, but their history remains browser-local only.

## Database choice

PostgreSQL is the right fit for this phase because it supports concurrent users, durable storage, hosted deployment, and straightforward backup workflows. It is a much stronger production path than relying only on browser storage or JSON files.

For convenience, the server can fall back to a local Unix-socket PostgreSQL connection when `DATABASE_URL` is not set. For normal local development and deployment, set `DATABASE_URL` explicitly.

## Backup strategy

User accounts and recommendation history should now be backed up at the database level.

Example backup:

```bash
mkdir -p backups
pg_dump "$DATABASE_URL" > backups/coffee_recommendation_app.sql
```

Example restore:

```bash
psql "$DATABASE_URL" < backups/coffee_recommendation_app.sql
```

## Beaker visualization

Each coffee profile includes ingredient composition percentages that total 100. The result page renders those percentages as a vertical beaker with stacked ingredient segments for coffee, milk, sugar, foam, water, and chocolate.

## Project structure

```text
client/   React + Vite frontend
server/   Express API, PostgreSQL access, and authentication
shared/   Shared coffee profiles, insights, and recommendation logic
```

## Setup

1. Install dependencies:

```bash
npm install
```

2. Create a `.env` file in the repository root:

```bash
cp .env.example .env
```

3. Configure the environment variables:

```env
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
PORT=8787
DATABASE_URL=postgresql://localhost:5432/coffee_recommendation_app
JWT_SECRET=replace_this_before_production
```

4. Make sure PostgreSQL is available locally, then start the frontend and backend together:

```bash
npm run dev
```

5. Build the frontend:

```bash
npm run build
```

6. Run the production server:

```bash
npm start
```

## Deploy the Streamlit app + API together

The polished Streamlit experience in `frontend/frontend.py` needs the Node API for live recommendations and barista chat. The included Docker deployment runs both in one web service:

- Streamlit listens on the platform-provided public `PORT`
- The Node API runs internally on `API_PORT=8787`
- `BACKEND_URL` points Streamlit to `http://127.0.0.1:8787/api`

Render can use the included `render.yaml` blueprint, or any Docker host can run:

```bash
docker build -t coffee-companion .
docker run -p 8501:8501 coffee-companion
```

For production accounts/history, add a hosted PostgreSQL database and set:

```env
DATABASE_URL=your_postgres_connection_string
JWT_SECRET=replace_this_before_production
```

On Railway, attach a PostgreSQL service and add its `DATABASE_URL` to the web service variables to enable persistent accounts and history. Without `DATABASE_URL`, the app still runs recommendations and barista chat, while auth/history use an in-memory fallback that resets on redeploy.

## Notes for the next UI integration step

The current home page is intentionally temporary. When your custom home page design is ready, the UI can be swapped in while keeping the shared data model, API routes, recommendation engine, and personalization logic intact.
