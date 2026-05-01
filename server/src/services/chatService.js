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
  },
  caffeinePreference: {
    low: ["low caffeine", "gentle", "light", "not too strong", "mild"],
    medium: ["balanced", "moderate", "normal"],
    high: ["strong", "extra caffeine", "high caffeine", "powerful", "wake me up"]
  },
  sweetnessPreference: {
    "not-sweet": ["not sweet", "unsweetened", "plain", "no sugar"],
    "lightly-sweet": ["slightly sweet", "lightly sweet", "subtle sweetness"],
    sweet: ["sweet", "dessert", "sugary", "vanilla", "caramel", "chocolate"]
  },
  texturePreference: {
    light: ["light", "clean", "thin", "crisp"],
    creamy: ["creamy", "comforting", "smooth", "velvety", "milky"],
    foamy: ["foamy", "airy", "dry foam"]
  },
  drinkStyle: {
    straight: ["straight", "black coffee", "no milk", "pure coffee"],
    milky: ["milky", "latte", "with milk", "soft"],
    refreshing: ["refreshing", "cold", "iced", "summer"],
    indulgent: ["indulgent", "treat", "dessert", "fancy", "fun"]
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
    caffeinePreference: inferValue(message, "caffeinePreference") || "medium",
    sweetnessPreference: inferValue(message, "sweetnessPreference") || "lightly-sweet",
    texturePreference: inferValue(message, "texturePreference") || "creamy",
    drinkStyle: inferValue(message, "drinkStyle") || "milky",
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
          "Extract coffee recommendation preferences. Return strict JSON with mood, taste, time, temperature, effort, caffeinePreference, sweetnessPreference, texturePreference, drinkStyle, trySomethingNew. Allowed values: mood=tired|relaxed|energetic, taste=bitter|smooth|sweet, time=morning|afternoon|night, temperature=hot|iced, effort=quick|elaborate, caffeinePreference=low|medium|high, sweetnessPreference=not-sweet|lightly-sweet|sweet, texturePreference=light|creamy|foamy, drinkStyle=straight|milky|refreshing|indulgent, trySomethingNew=true|false."
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
