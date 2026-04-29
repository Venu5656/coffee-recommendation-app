# Coffee Recommendation System with Data-Driven Insight Integration

This project turns a prior midterm analysis of global coffee consumption into a practical application. It combines a rule-based recommendation engine, an AI chat workflow, local personalization, an exploration layer for variety, a beaker-style ingredient visualization, and a separate "Did You Know?" section that presents the earlier analysis findings without affecting recommendation logic.

## How this extends the midterm analysis

The earlier analysis found that coffee consumption is stable in high-income countries, weakly tied to GDP growth, inversely related to work intensity in several cases, and strongly shaped by cultural context. Those findings appear in the UI as readable insight cards so the project preserves the analytical narrative while keeping recommendation decisions independent.

## Core features

- Filter-based recommendation using mood, taste, time, temperature, and effort
- Shared coffee profile model across rule-based and chat-based recommendation flows
- Exploration mode that occasionally diversifies suggestions outside familiar user patterns
- AI chatbot endpoint that extracts preferences from free text and maps them to the same drink profiles
- Beaker-style composition graph for ingredient percentages
- Local history and feedback tracking with `localStorage`
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

## Beaker visualization

Each coffee profile includes ingredient composition percentages that total 100. The result page renders those percentages as a vertical beaker with stacked ingredient segments for coffee, milk, sugar, foam, water, and chocolate.

## Project structure

```text
client/   React + Vite frontend
server/   Express API and chatbot integration
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

3. Optional: add an OpenAI key to enable LLM-based extraction:

```env
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o-mini
PORT=8787
```

4. Start the frontend and backend together:

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

## Notes for the next UI integration step

The current home page is intentionally temporary. When your custom home page design is ready, the UI can be swapped in while keeping the shared data model, API routes, recommendation engine, and personalization logic intact.
