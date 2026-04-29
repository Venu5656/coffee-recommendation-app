import OpenAI from "openai";
import { recommendCoffee } from "@coffee/shared/recommendation";

const keywordMap = {
  mood: {
    tired: ["tired", "sleepy", "drained", "exhausted", "sluggish"],
    relaxed: ["relaxed", "calm", "cozy", "comforting", "gentle"],
    energetic: ["energetic", "focused", "motivated", "active", "productive"]
  },
  taste: {
    bitter: ["bitter", "strong", "bold", "intense"],
    smooth: ["smooth", "mellow", "comforting", "creamy", "balanced"],
    sweet: ["sweet", "dessert", "sugary", "vanilla", "chocolate"]
  },
  time: {
    morning: ["morning", "breakfast", "early"],
    afternoon: ["afternoon", "lunch", "midday"],
    night: ["night", "evening", "late"]
  },
  temperature: {
    hot: ["hot", "warm"],
    iced: ["iced", "cold", "chilled", "refreshing"]
  },
  effort: {
    quick: ["quick", "fast", "simple", "easy"],
    elaborate: ["elaborate", "treat", "special", "fancy"]
  }
};

function inferValue(text, group) {
  const normalized = text.toLowerCase();
  return Object.entries(keywordMap[group]).find(([, words]) => words.some((word) => normalized.includes(word)))?.[0] || null;
}

function heuristicExtraction(message) {
  return {
    mood: inferValue(message, "mood") || "relaxed",
    taste: inferValue(message, "taste") || "smooth",
    time: inferValue(message, "time") || "afternoon",
    temperature: inferValue(message, "temperature") || "hot",
    effort: inferValue(message, "effort") || "quick",
    trySomethingNew: /new|different|surprise|explore|adventurous/.test(message.toLowerCase())
  };
}

async function llmExtraction(message) {
  if (!process.env.OPENAI_API_KEY) {
    return null;
  }

  const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
  const response = await client.chat.completions.create({
    model: process.env.OPENAI_MODEL || "gpt-4o-mini",
    temperature: 0.2,
    response_format: { type: "json_object" },
    messages: [
      {
        role: "system",
        content:
          "Extract coffee recommendation preferences. Return strict JSON with mood, taste, time, temperature, effort, trySomethingNew. Allowed values: mood=tired|relaxed|energetic, taste=bitter|smooth|sweet, time=morning|afternoon|night, temperature=hot|iced, effort=quick|elaborate, trySomethingNew=true|false."
      },
      {
        role: "user",
        content: message
      }
    ]
  });

  const raw = response.choices[0]?.message?.content;
  if (!raw) {
    return null;
  }

  try {
    return JSON.parse(raw);
  } catch {
    return null;
  }
}

export async function getChatRecommendation(message, history = []) {
  const extracted = (await llmExtraction(message)) || heuristicExtraction(message);
  const result = recommendCoffee(extracted, history);

  const reply = `Based on what you said, I would recommend the ${result.drink.name}. ${result.reasoning} If you want, I can adjust it toward something sweeter, lower caffeine, or more adventurous.`;

  return {
    extractedPreferences: extracted,
    recommendation: result,
    reply,
    usedLlm: Boolean(process.env.OPENAI_API_KEY)
  };
}
