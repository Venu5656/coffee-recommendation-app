import { coffeeProfiles } from "./coffeeProfiles.js";

const ATTRIBUTE_WEIGHTS = {
  mood: 3,
  taste: 3,
  time: 2,
  temperature: 2,
  effort: 2
};

function buildHistorySignals(history = []) {
  const counts = {};
  const likes = {};

  history.forEach((entry) => {
    const name = entry.recommendation || entry.name;
    if (!name) {
      return;
    }

    counts[name] = (counts[name] || 0) + 1;

    if (entry.feedback === "like" || entry.liked === true) {
      likes[name] = (likes[name] || 0) + 1;
    }
  });

  const favorite = Object.entries(counts).sort((a, b) => b[1] - a[1])[0]?.[0] || null;
  const repeated = Object.values(counts).some((count) => count >= 3);

  return { counts, likes, favorite, repeated };
}

function scoreProfile(profile, preferences, historySignals) {
  let score = 0;
  const reasons = [];

  if (preferences.mood && profile.moods.includes(preferences.mood)) {
    score += ATTRIBUTE_WEIGHTS.mood;
    reasons.push(`matches your ${preferences.mood} mood`);
  }

  if (preferences.taste && profile.tastes.includes(preferences.taste)) {
    score += ATTRIBUTE_WEIGHTS.taste;
    reasons.push(`fits your preference for ${preferences.taste} flavors`);
  }

  if (preferences.time && profile.times.includes(preferences.time)) {
    score += ATTRIBUTE_WEIGHTS.time;
    reasons.push(`works well for ${preferences.time}`);
  }

  if (preferences.temperature && profile.temperature.includes(preferences.temperature)) {
    score += ATTRIBUTE_WEIGHTS.temperature;
    reasons.push(`is available as a ${preferences.temperature} drink`);
  }

  if (preferences.effort && profile.effort === preferences.effort) {
    score += ATTRIBUTE_WEIGHTS.effort;
    reasons.push(`matches your ${preferences.effort} effort preference`);
  }

  const likedBoost = historySignals.likes[profile.name] || 0;
  if (likedBoost > 0) {
    score += Math.min(2, likedBoost);
    reasons.push("leans toward drinks you previously liked");
  }

  return { score, reasons };
}

function createReasoning(drink, preferences, reasons, explorationUsed) {
  const tasteLine = `Its ${drink.tastes.join(" and ")} profile aligns with what you asked for.`;
  const caffeineLine = `It delivers a ${drink.caffeineLevel} caffeine level, which suits a ${preferences.mood || "current"} mood.`;
  const timeLine = `It is a strong fit for ${preferences.time || "this time of day"} and works as a ${drink.temperature.join(" or ")} option.`;
  const effortLine = `The preparation is ${drink.effort}, so it stays compatible with the amount of effort you want.`;
  const exploreLine = explorationUsed
    ? "Exploration mode nudged the result slightly outside your most familiar pattern to encourage discovery."
    : "The recommendation stays close to your stated preferences and recent habits.";

  return `${drink.name} was selected because it ${reasons.slice(0, 2).join(" and ")}. ${tasteLine} ${caffeineLine} ${timeLine} ${effortLine} ${exploreLine}`;
}

export function recommendCoffee(preferences, history = [], profiles = coffeeProfiles) {
  const historySignals = buildHistorySignals(history);
  const scored = profiles
    .map((profile) => {
      const base = scoreProfile(profile, preferences, historySignals);
      return { profile, ...base };
    })
    .sort((a, b) => b.score - a.score);

  const trySomethingNew = Boolean(preferences.trySomethingNew);
  const shouldExplore = trySomethingNew || historySignals.repeated;
  const explorationShare = shouldExplore ? 0.25 : 0;
  const topCandidates = scored.slice(0, 4);

  let selected = topCandidates[0];
  let explorationUsed = false;

  if (shouldExplore && topCandidates.length > 1) {
    const explorationPool = topCandidates.filter(
      (candidate) =>
        candidate.profile.name !== historySignals.favorite &&
        !candidate.profile.tastes.includes(preferences.taste || "")
    );

    if (explorationPool.length > 0 && Math.random() < explorationShare + 0.05) {
      selected = explorationPool[0];
      explorationUsed = true;
    }
  }

  return {
    drink: selected.profile,
    score: selected.score,
    explorationUsed,
    explorationShare,
    reasoning: createReasoning(selected.profile, preferences, selected.reasons, explorationUsed),
    reasonDetails: {
      tasteMatch: selected.profile.tastes,
      caffeineLevel: selected.profile.caffeineLevel,
      timeSuitability: selected.profile.times,
      effortCompatibility: selected.profile.effort
    },
    alternatives: topCandidates.slice(1, 3).map((candidate) => candidate.profile)
  };
}

export function extractPreferenceSummary(result) {
  return {
    name: result.drink.name,
    caffeineLevel: result.drink.caffeineLevel,
    temperatures: result.drink.temperature,
    effort: result.drink.effort
  };
}
