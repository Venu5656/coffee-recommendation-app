import { recommendCoffee } from "@coffee/shared/recommendation";
import { coffeeProfiles } from "@coffee/shared/coffeeProfiles";
import { coffeeKnowledge, customCoffeeDrinks, knowledgeTopics } from "@coffee/shared/baristaKnowledge";

const keywordMap = {
  mood: {
    tired: ["tired", "sleepy", "drained", "exhausted", "sluggish"],
    relaxed: ["relaxed", "calm", "cozy", "comforting", "gentle"],
    energetic: ["energetic", "focused", "motivated", "active", "productive"]
  },
  taste: {
    bitter: ["bitter", "strong", "bold", "intense"],
    smooth: ["smooth", "mellow", "comforting", "creamy", "balanced"],
    sweet: ["sweet", "dessert", "sugary", "vanilla", "chocolate", "caramel"]
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
    low: ["low caffeine", "gentle", "light", "not too strong", "mild", "less caffeine"],
    medium: ["balanced", "moderate", "normal"],
    high: ["strong", "extra caffeine", "high caffeine", "powerful", "wake me up", "more caffeine"]
  },
  sweetnessPreference: {
    "not-sweet": ["not sweet", "unsweetened", "plain", "no sugar", "less sweet"],
    "lightly-sweet": ["slightly sweet", "lightly sweet", "subtle sweetness"],
    sweet: ["sweet", "dessert", "sugary", "vanilla", "caramel", "chocolate", "sweeter"]
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

const intentPatterns = {
  brewGuide: /(how do i make|how to make|make at home|recipe|brew this|steps|ingredients|home|make that)/i,
  knowledge: /(what is|history|origin|explain|term|method|what does|tell me about|why does|how does|teach me|learn|basics|beginner|new coffee drinker|tradition)/i,
  comparison: /(difference between|compare|vs\b|versus|better than)/i,
  offMenu: /(outside|off menu|not on the menu|custom|different drink|specialty|surprise me|something else|something new|new drink|try in)/i,
  followUp: /(something sweeter|less sweet|stronger|less caffeine|more caffeine|same thing but|make it iced|make it hot|similar to that|like that)/i
};

const profileAliases = [
  { phrases: ["iced latte"], profileId: "latte", title: "Iced Latte", temperature: "iced" },
  { phrases: ["cafe latte"], profileId: "latte", title: "Latte" },
  { phrases: ["black coffee"], profileId: "americano", title: "Americano" },
  { phrases: ["milk coffee"], profileId: "latte", title: "Latte" }
];

function tokenize(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9\s]/g, " ")
    .split(/\s+/)
    .filter(Boolean);
}

function phraseIncluded(normalizedMessage, phrase) {
  return normalizedMessage.includes(phrase.toLowerCase());
}

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

function strongestNameMatch(message, drinks) {
  const normalized = message.toLowerCase();
  const tokens = tokenize(message);
  const directMatches = drinks
    .filter((drink) => phraseIncluded(normalized, drink.name.toLowerCase()))
    .sort((left, right) => right.name.length - left.name.length);

  if (directMatches.length > 0) {
    return directMatches[0];
  }

  const tokenMatches = drinks
    .filter((drink) => {
      const nameTokens = tokenize(drink.name);
      return nameTokens.length > 0 && nameTokens.every((token) => tokens.includes(token));
    })
    .sort((left, right) => tokenize(right.name).length - tokenize(left.name).length);

  return tokenMatches[0] || null;
}

function getProfileById(profileId) {
  return coffeeProfiles.find((profile) => profile.id === profileId) || null;
}

function resolveProfileAlias(message) {
  const normalized = message.toLowerCase();
  const alias = profileAliases.find((item) => item.phrases.some((phrase) => phraseIncluded(normalized, phrase)));
  if (!alias) {
    return null;
  }

  const profile = getProfileById(alias.profileId);
  return profile ? { profile, title: alias.title || profile.name, temperature: alias.temperature || null } : null;
}

function findCustomDrink(message) {
  const normalized = message.toLowerCase();
  const directNameMatch = strongestNameMatch(message, customCoffeeDrinks);

  if (directNameMatch) {
    return directNameMatch;
  }

  const tokens = tokenize(message);
  return (
    customCoffeeDrinks.find((drink) => {
      const strongTagMatches = drink.tags.filter((tag) =>
        tag.includes(" ") ? phraseIncluded(normalized, tag) : tokens.includes(tag)
      );
      return strongTagMatches.length >= 2;
    }) || null
  );
}

function findProfileDrink(message) {
  const aliasMatch = resolveProfileAlias(message);
  if (aliasMatch) {
    return aliasMatch;
  }

  const normalized = message.toLowerCase();
  const directNameMatch = strongestNameMatch(message, coffeeProfiles);

  if (directNameMatch) {
    return { profile: directNameMatch, title: directNameMatch.name, temperature: null };
  }

  const tokens = tokenize(message);
  const matchedProfile = coffeeProfiles.find((drink) => {
    const nameTokens = tokenize(drink.name);
    const matchedNameTokens = nameTokens.filter((token) => tokens.includes(token));
    if (matchedNameTokens.length >= Math.min(2, nameTokens.length)) {
      return true;
    }

    const strongTagMatches = drink.tags.filter((tag) =>
      tag.includes(" ") ? phraseIncluded(normalized, tag) : tokens.includes(tag)
    );
    return strongTagMatches.length >= 2;
  });

  return matchedProfile ? { profile: matchedProfile, title: matchedProfile.name, temperature: null } : null;
}

function findLastMentionedDrink(conversation = []) {
  const reversedMessages = [...conversation].reverse();

  for (const item of reversedMessages) {
    if (!item?.content) {
      continue;
    }

    const profileMatch = findProfileDrink(item.content);
    if (profileMatch) {
      return { kind: "profile", ...profileMatch };
    }

    const customMatch = findCustomDrink(item.content);
    if (customMatch) {
      return { kind: "custom", drink: customMatch, title: customMatch.name };
    }
  }

  return null;
}

function mergePreferences(base, overrides) {
  return {
    ...base,
    ...Object.fromEntries(Object.entries(overrides).filter(([, value]) => value !== null && value !== undefined))
  };
}

function refinePreferencesFromFollowUp(message, priorPreferences) {
  const normalized = message.toLowerCase();
  const overrides = {};

  if (/less sweet|not sweet|less sugary/.test(normalized)) {
    overrides.sweetnessPreference = "not-sweet";
    overrides.taste = "smooth";
  } else if (/sweeter|more sweet|dessert/.test(normalized)) {
    overrides.sweetnessPreference = "sweet";
    overrides.taste = "sweet";
  }

  if (/less caffeine|not too strong|lighter/.test(normalized)) {
    overrides.caffeinePreference = "low";
    overrides.taste = "smooth";
  } else if (/stronger|more caffeine|wake me up/.test(normalized)) {
    overrides.caffeinePreference = "high";
    overrides.taste = "bitter";
  }

  if (/make it iced|iced version|cold version/.test(normalized)) {
    overrides.temperature = "iced";
    overrides.drinkStyle = priorPreferences?.drinkStyle === "straight" ? "refreshing" : priorPreferences?.drinkStyle;
  } else if (/make it hot|hot version|warm version/.test(normalized)) {
    overrides.temperature = "hot";
  }

  if (/creamier|more comforting|milkier/.test(normalized)) {
    overrides.texturePreference = "creamy";
    overrides.drinkStyle = "milky";
  }

  return mergePreferences(priorPreferences, overrides);
}

function inferPreferencesFromDrink(profile, overrides = {}) {
  return {
    mood: profile.moods?.[0] || "relaxed",
    taste: profile.tastes?.[0] || "smooth",
    time: profile.times?.[0] || "afternoon",
    temperature: overrides.temperature || profile.temperature?.[0] || "hot",
    effort: profile.effort || "quick",
    caffeinePreference: profile.caffeineLevel || "medium",
    sweetnessPreference: profile.sweetnessLevel || "lightly-sweet",
    texturePreference: profile.texture || "creamy",
    drinkStyle: profile.drinkStyle || "milky",
    trySomethingNew: false
  };
}

function classifyIntent(message, conversation = []) {
  if (/(vietnam|vietnamese)/i.test(message) && /(try|drink|something new|specialty)/i.test(message)) {
    return "custom_recommendation";
  }
  if (intentPatterns.brewGuide.test(message)) {
    return "brew_guide";
  }
  if (intentPatterns.comparison.test(message)) {
    return "knowledge";
  }
  if (intentPatterns.knowledge.test(message)) {
    return "knowledge";
  }
  if (intentPatterns.offMenu.test(message)) {
    return "custom_recommendation";
  }
  if (intentPatterns.followUp.test(message) && findLastMentionedDrink(conversation)) {
    return "profile_recommendation";
  }
  return "profile_recommendation";
}

function chooseCustomDrink(preferences) {
  if (preferences.temperature === "iced" && preferences.drinkStyle === "refreshing") {
    return customCoffeeDrinks.find((drink) => drink.id === "espresso-tonic");
  }
  if (preferences.temperature === "iced" && preferences.sweetnessPreference === "sweet") {
    return customCoffeeDrinks.find((drink) => drink.id === "vietnamese-iced-coffee");
  }
  if (preferences.drinkStyle === "milky" && preferences.trySomethingNew) {
    return customCoffeeDrinks.find((drink) => drink.id === "dirty-chai");
  }
  if (preferences.caffeinePreference === "high") {
    return customCoffeeDrinks.find((drink) => drink.id === "red-eye");
  }
  return customCoffeeDrinks.find((drink) => drink.id === "shakerato");
}

function chooseCustomDrinkFromMessage(message, preferences) {
  const normalized = message.toLowerCase();

  if (/vietnam|vietnamese/.test(normalized)) {
    return customCoffeeDrinks.find((drink) => drink.id === "vietnamese-iced-coffee");
  }

  if (/chai|spiced/.test(normalized)) {
    return customCoffeeDrinks.find((drink) => drink.id === "dirty-chai");
  }

  if (/tonic|sparkling|citrus/.test(normalized)) {
    return customCoffeeDrinks.find((drink) => drink.id === "espresso-tonic");
  }

  return chooseCustomDrink(preferences);
}

function buildComparisonKnowledge(message) {
  const normalized = message.toLowerCase();

  if (/latte/.test(normalized) && /cappuccino/.test(normalized)) {
    return {
      title: "Latte vs Cappuccino",
      summary: "A latte is milkier and smoother, while a cappuccino is foamier and feels lighter on the palate.",
      bullets: [
        "Lattes carry more steamed milk, so they taste softer and more comfort-driven.",
        "Cappuccinos use a more pronounced foam layer, which makes the coffee feel airier.",
        "Choose latte for creaminess and cappuccino for texture and stronger coffee definition."
      ]
    };
  }

  if (/cold brew/.test(normalized) && /iced coffee|iced americano/.test(normalized)) {
    return {
      title: "Cold Brew vs Iced Coffee",
      summary: "Cold brew is extracted cold over time, while iced coffee or an iced Americano is brewed hot first and then chilled or poured over ice.",
      bullets: [
        "Cold brew usually tastes smoother and rounder.",
        "Iced coffee styles feel brighter and more immediate.",
        "Choose cold brew for low-acid smoothness and iced Americano for clean crispness."
      ]
    };
  }

  return null;
}

function scoreKnowledgeTopic(message, topic) {
  const normalized = message.toLowerCase();
  let score = 0;

  for (const keyword of topic.keywords || []) {
    if (phraseIncluded(normalized, keyword)) {
      score += keyword.includes(" ") ? 4 : 2;
    }
  }

  if (phraseIncluded(normalized, topic.title.toLowerCase())) {
    score += 5;
  }

  if (topic.id.startsWith("history-") && /history|origin|tradition/.test(normalized)) {
    score += 2;
  }

  if (topic.id !== "history-global" && topic.id.startsWith("history-") && /usa|united states|america|italian|italy|ethiopia|ethiopian|turkey|turkish|vietnam|vietnamese/.test(normalized)) {
    score += 3;
  }

  if (topic.id === "brewing-beginners" && /teach me|learn|basics|beginner|new coffee drinker|start brewing/.test(normalized)) {
    score += 5;
  }

  return score;
}

function getKnowledgeTopic(message) {
  const comparison = buildComparisonKnowledge(message);
  if (comparison) {
    return comparison;
  }

  const rankedTopics = knowledgeTopics
    .map((topic) => ({ topic, score: scoreKnowledgeTopic(message, topic) }))
    .filter((item) => item.score > 0)
    .sort((left, right) => right.score - left.score);

  if (rankedTopics.length > 0) {
    return rankedTopics[0].topic;
  }

  const normalized = message.toLowerCase();
  if (/history|origin|where did coffee come from/.test(normalized)) {
    return coffeeKnowledge.history;
  }
  if (/brew|brewing|pour over|french press|espresso|cold brew|method|home brew/.test(normalized)) {
    return coffeeKnowledge.brewing;
  }
  return coffeeKnowledge.terms;
}

function genericProfileGuide(profile, overrides = {}) {
  const title = overrides.title || profile.name;
  const isIced = overrides.temperature
    ? overrides.temperature === "iced"
    : profile.temperature.includes("iced");
  const coffeePortion = profile.composition.coffee ?? 30;
  const waterPortion = profile.composition.water ?? 0;
  const milkPortion = profile.composition.milk ?? 0;
  const sweetnessPortion = profile.composition.sugar ?? profile.composition.chocolate ?? 0;

  const ingredients = ["freshly brewed coffee or espresso"];
  if (waterPortion > 0) {
    ingredients.push(isIced ? "cold water and ice" : "hot water");
  }
  if (milkPortion > 0) {
    ingredients.push(isIced ? "cold milk and ice" : "milk");
  }
  if (profile.composition.foam) {
    ingredients.push(isIced ? "a light cold foam or optional foam finish" : "milk foam");
  }
  if (sweetnessPortion > 0) {
    ingredients.push("sweetener or chocolate component if desired");
  }

  const steps = [
    `Prepare a concentrated coffee base for ${title}.`,
    waterPortion > 0
      ? `Add ${isIced ? "cold water over ice" : "water"} to open up the coffee and reach a balanced strength.`
      : "Keep the coffee base concentrated so the drink keeps its intended body.",
    milkPortion > 0
      ? `Add ${isIced ? "cold milk" : "milk"} and texture it lightly if the drink style calls for softness.`
      : "Serve without milk to preserve the drink's clean profile."
  ];

  if (profile.composition.foam) {
    steps.push(`Finish with ${isIced ? "a light foam layer if you want a cafe-style top" : "a layer of foam"} for texture.`);
  }

  steps.push("Taste and adjust dilution or sweetness before serving.");

  return {
    title,
    equipment: [
      profile.drinkStyle === "straight" ? "espresso machine, moka pot, or strong brew method" : "espresso machine or strong brew setup",
      isIced ? "glass and ice" : "cup",
      milkPortion > 0 ? "milk pitcher or frother" : "basic serving tools"
    ],
    ingredients,
    steps,
    tips: [
      `Aim for roughly ${coffeePortion}% of the drink to come from the coffee base for a similar balance.`,
      isIced
        ? "Chill the glass and use plenty of ice so the drink stays crisp instead of tasting watered down."
        : "Warm the cup first so the drink stays balanced and aromatic longer."
    ]
  };
}

function buildGuideResponse(title, guide) {
  return {
    title,
    equipment: guide.equipment,
    ingredients: guide.ingredients,
    steps: guide.steps,
    tips: guide.tips
  };
}

function buildLocalReasoningResponse(drinkName, reasoning) {
  return `Based on what you said, I would recommend the ${drinkName}. ${reasoning} I can also refine it if you want it sweeter, stronger, iced, hotter, or easier to make at home.`;
}

function handleProfileRecommendation(preferences, history, conversation = []) {
  const lastMention = findLastMentionedDrink(conversation);
  const latestUserMessage = conversation.at(-1)?.content || "";
  let effectivePreferences = preferences;

  if (intentPatterns.followUp.test(latestUserMessage) && lastMention?.kind === "profile") {
    const basePreferences = inferPreferencesFromDrink(lastMention.profile, {
      temperature: lastMention.temperature || undefined
    });
    effectivePreferences = refinePreferencesFromFollowUp(latestUserMessage, basePreferences);
  }

  const result = recommendCoffee(effectivePreferences, history);
  return {
    mode: "profile_recommendation",
    recommendation: result,
    reply: buildLocalReasoningResponse(result.drink.name, result.reasoning)
  };
}

function handleCustomRecommendation(message, preferences) {
  const drink = chooseCustomDrinkFromMessage(message, preferences);
  return {
    mode: "custom_recommendation",
    customDrink: drink,
    guide: buildGuideResponse(drink.name, drink.homeGuide),
    reply: `If you want something outside the current core coffee profiles, I would suggest ${drink.name}. ${drink.description} I can also guide you through making it at home.`
  };
}

function handleBrewGuide(message, preferences, conversation = []) {
  const matchedProfile = findProfileDrink(message) || (findLastMentionedDrink(conversation)?.kind === "profile"
    ? findLastMentionedDrink(conversation)
    : null);

  if (matchedProfile?.profile) {
    const guide = genericProfileGuide(matchedProfile.profile, {
      title: matchedProfile.title,
      temperature: matchedProfile.temperature
    });

    return {
      mode: "brew_guide",
      guide: buildGuideResponse(guide.title, guide),
      reply: `I can help you make a home version of ${guide.title}.`
    };
  }

  const priorCustom = findLastMentionedDrink(conversation);
  if (priorCustom?.kind === "custom") {
    return {
      mode: "brew_guide",
      guide: buildGuideResponse(priorCustom.title, priorCustom.drink.homeGuide),
      reply: `Here is a home guide for ${priorCustom.title}.`
    };
  }

  const matchedCustom = findCustomDrink(message);
  if (matchedCustom) {
    return {
      mode: "brew_guide",
      guide: buildGuideResponse(matchedCustom.name, matchedCustom.homeGuide),
      reply: `Here is a home guide for ${matchedCustom.name}.`
    };
  }

  const fallback = chooseCustomDrink(preferences);
  return {
    mode: "brew_guide",
    guide: buildGuideResponse(fallback.name, fallback.homeGuide),
    reply: `A good at-home coffee to try based on your request is ${fallback.name}.`
  };
}

function handleKnowledge(message) {
  const topic = getKnowledgeTopic(message);
  return {
    mode: "knowledge",
    knowledge: topic,
    reply: `${topic.title}: ${topic.summary}`
  };
}

export async function getChatRecommendation(message, history = [], conversation = []) {
  const extractedPreferences = heuristicExtraction(message);
  const lastMessage = conversation.at(-1)?.content || message;
  const intent = classifyIntent(lastMessage, conversation);

  let response;
  if (intent === "knowledge") {
    response = handleKnowledge(message);
  } else if (intent === "brew_guide") {
    response = handleBrewGuide(message, extractedPreferences, conversation);
  } else if (intent === "custom_recommendation") {
    response = handleCustomRecommendation(message, extractedPreferences);
  } else {
    response = handleProfileRecommendation(extractedPreferences, history, conversation);
  }

  return {
    ...response,
    extractedPreferences,
    assistantEngine: "local-barista"
  };
}
