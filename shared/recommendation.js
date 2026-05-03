import { coffeeProfiles } from "./coffeeProfiles.js";
import { buildFeedbackMap, deriveAdaptiveProfile, normalizeHistory } from "./personalization.js";

const ATTRIBUTE_WEIGHTS = {
  mood: 3,
  taste: 3,
  time: 2,
  temperature: 2,
  effort: 2,
  caffeinePreference: 3,
  sweetnessPreference: 2,
  texturePreference: 2,
  drinkStyle: 2
};

const PERSONALIZATION_WEIGHTS = {
  preferredCaffeine: 1.4,
  preferredSweetness: 1.2,
  preferredTexture: 1.2,
  preferredStyle: 1.2,
  preferredTemperature: 1,
  preferredEffort: 0.8,
  dominantTaste: 1,
  signatureTime: 0.8,
  signatureMood: 0.8,
  favoriteDrink: 1.4,
  dislikedDrinkPenalty: 4,
  dislikedTastePenalty: 1.5,
  rankingAffinity: 2.2
};

const EXPLICIT_MISMATCH_PENALTIES = {
  caffeinePreference: 4.2,
  temperature: 3.2,
  drinkStyle: 2.8,
  taste: 2.2,
  sweetnessPreference: 1.6,
  texturePreference: 1.4,
  effort: 1.2,
  time: 1,
  mood: 1
};

function valueSignal(map, key) {
  if (!key) {
    return 0;
  }

  return map?.[key] || 0;
}

function listSignal(map, values = []) {
  if (!values.length) {
    return 0;
  }

  return Math.max(...values.map((value) => valueSignal(map, value)), 0);
}

function buildHistorySignals(history = []) {
  const counts = {};
  const likes = {};
  const dislikes = {};
  const events = normalizeHistory(history);
  const feedbackMap = buildFeedbackMap(history);

  history.forEach((entry) => {
    const name = entry.recommendation || entry.name;
    if (!name) {
      return;
    }

    counts[name] = (counts[name] || 0) + 1;

    if (entry.feedback === "like" || entry.liked === true) {
      likes[name] = (likes[name] || 0) + 1;
    }

    if (entry.feedback === "dislike" || entry.disliked === true) {
      dislikes[name] = (dislikes[name] || 0) + 1;
    }
  });

  const favorite = Object.entries(counts).sort((a, b) => b[1] - a[1])[0]?.[0] || null;
  const repeated = Object.values(counts).some((count) => count >= 3);
  const adaptiveProfile = deriveAdaptiveProfile(history);

  return { counts, likes, dislikes, favorite, repeated, adaptiveProfile, feedbackMap, events };
}

function scoreProfile(profile, preferences, historySignals) {
  let score = 0;
  const reasons = [];
  const personalizationReasons = [];

  if (preferences.mood && !profile.moods.includes(preferences.mood)) {
    score -= EXPLICIT_MISMATCH_PENALTIES.mood;
  }

  if (preferences.mood && profile.moods.includes(preferences.mood)) {
    score += ATTRIBUTE_WEIGHTS.mood;
    reasons.push(`matches your ${preferences.mood} mood`);
  }

  if (preferences.taste && !profile.tastes.includes(preferences.taste)) {
    score -= EXPLICIT_MISMATCH_PENALTIES.taste;
  }

  if (preferences.taste && profile.tastes.includes(preferences.taste)) {
    score += ATTRIBUTE_WEIGHTS.taste;
    reasons.push(`fits your preference for ${preferences.taste} flavors`);
  }

  if (preferences.time && !profile.times.includes(preferences.time)) {
    score -= EXPLICIT_MISMATCH_PENALTIES.time;
  }

  if (preferences.time && profile.times.includes(preferences.time)) {
    score += ATTRIBUTE_WEIGHTS.time;
    reasons.push(`works well for ${preferences.time}`);
  }

  if (preferences.temperature && !profile.temperature.includes(preferences.temperature)) {
    score -= EXPLICIT_MISMATCH_PENALTIES.temperature;
  }

  if (preferences.temperature && profile.temperature.includes(preferences.temperature)) {
    score += ATTRIBUTE_WEIGHTS.temperature;
    reasons.push(`is available as a ${preferences.temperature} drink`);
  }

  if (preferences.effort && profile.effort !== preferences.effort) {
    score -= EXPLICIT_MISMATCH_PENALTIES.effort;
  }

  if (preferences.effort && profile.effort === preferences.effort) {
    score += ATTRIBUTE_WEIGHTS.effort;
    reasons.push(`matches your ${preferences.effort} effort preference`);
  }

  if (preferences.caffeinePreference && profile.caffeineLevel !== preferences.caffeinePreference) {
    score -= EXPLICIT_MISMATCH_PENALTIES.caffeinePreference;
  }

  if (preferences.caffeinePreference && profile.caffeineLevel === preferences.caffeinePreference) {
    score += ATTRIBUTE_WEIGHTS.caffeinePreference;
    reasons.push(`lands at your preferred ${preferences.caffeinePreference} caffeine level`);
  }

  if (preferences.sweetnessPreference && profile.sweetnessLevel !== preferences.sweetnessPreference) {
    score -= EXPLICIT_MISMATCH_PENALTIES.sweetnessPreference;
  }

  if (preferences.sweetnessPreference && profile.sweetnessLevel === preferences.sweetnessPreference) {
    score += ATTRIBUTE_WEIGHTS.sweetnessPreference;
    reasons.push(`matches your ${preferences.sweetnessPreference} sweetness preference`);
  }

  if (preferences.texturePreference && profile.texture !== preferences.texturePreference) {
    score -= EXPLICIT_MISMATCH_PENALTIES.texturePreference;
  }

  if (preferences.texturePreference && profile.texture === preferences.texturePreference) {
    score += ATTRIBUTE_WEIGHTS.texturePreference;
    reasons.push(`fits the ${preferences.texturePreference} texture you tend to like`);
  }

  if (preferences.drinkStyle && profile.drinkStyle !== preferences.drinkStyle) {
    score -= EXPLICIT_MISMATCH_PENALTIES.drinkStyle;
  }

  if (preferences.drinkStyle && profile.drinkStyle === preferences.drinkStyle) {
    score += ATTRIBUTE_WEIGHTS.drinkStyle;
    reasons.push(`aligns with your ${preferences.drinkStyle} drink style`);
  }

  const likedBoost = historySignals.likes[profile.name] || 0;
  if (likedBoost > 0) {
    score += Math.min(2, likedBoost);
    reasons.push("leans toward drinks you previously liked");
  }

  const dislikeCount = historySignals.dislikes[profile.name] || 0;
  if (dislikeCount > 0) {
    score -= PERSONALIZATION_WEIGHTS.dislikedDrinkPenalty + dislikeCount - 1;
    personalizationReasons.push("pulls away from drinks you previously rejected");
  }

  const adaptive = historySignals.adaptiveProfile;
  if (adaptive.historyDepth >= 3) {
    const rankingSignals = adaptive.rankingSignals || {};

    if (!preferences.caffeinePreference && profile.caffeineLevel === adaptive.preferredCaffeine) {
      score += PERSONALIZATION_WEIGHTS.preferredCaffeine;
      personalizationReasons.push("matches your learned caffeine band");
    }

    if (!preferences.sweetnessPreference && profile.sweetnessLevel === adaptive.preferredSweetness) {
      score += PERSONALIZATION_WEIGHTS.preferredSweetness;
      personalizationReasons.push("fits your learned sweetness tolerance");
    }

    if (!preferences.texturePreference && profile.texture === adaptive.preferredTexture) {
      score += PERSONALIZATION_WEIGHTS.preferredTexture;
      personalizationReasons.push("fits the texture you usually enjoy");
    }

    if (!preferences.drinkStyle && profile.drinkStyle === adaptive.preferredStyle) {
      score += PERSONALIZATION_WEIGHTS.preferredStyle;
      personalizationReasons.push("aligns with your usual drink style");
    }

    if (!preferences.temperature && profile.temperature.includes(adaptive.preferredTemperature)) {
      score += PERSONALIZATION_WEIGHTS.preferredTemperature;
      personalizationReasons.push("stays close to your normal temperature preference");
    }

    if (!preferences.effort && profile.effort === adaptive.preferredEffort) {
      score += PERSONALIZATION_WEIGHTS.preferredEffort;
      personalizationReasons.push("matches the effort level you usually choose");
    }

    if (!preferences.taste && profile.tastes.includes(adaptive.dominantTaste)) {
      score += PERSONALIZATION_WEIGHTS.dominantTaste;
      personalizationReasons.push("tracks with your strongest flavor direction");
    }

    if (!preferences.time && profile.times.includes(adaptive.signatureTime)) {
      score += PERSONALIZATION_WEIGHTS.signatureTime;
      personalizationReasons.push("suits the time of day you most often drink coffee");
    }

    if (!preferences.mood && profile.moods.includes(adaptive.signatureMood)) {
      score += PERSONALIZATION_WEIGHTS.signatureMood;
      personalizationReasons.push("fits the mood pattern that appears most in your history");
    }

    if (adaptive.favoriteDrink && profile.name === adaptive.favoriteDrink) {
      score += PERSONALIZATION_WEIGHTS.favoriteDrink;
      personalizationReasons.push("stays close to your most repeated favorite");
    }

    if (adaptive.dislikedTastes.some((taste) => profile.tastes.includes(taste))) {
      score -= PERSONALIZATION_WEIGHTS.dislikedTastePenalty;
    }

    const affinityScore =
      (preferences.caffeinePreference ? 0 : valueSignal(rankingSignals.caffeineAffinities, profile.caffeineLevel)) +
      (preferences.sweetnessPreference ? 0 : valueSignal(rankingSignals.sweetnessAffinities, profile.sweetnessLevel)) +
      (preferences.texturePreference ? 0 : valueSignal(rankingSignals.textureAffinities, profile.texture)) +
      (preferences.drinkStyle ? 0 : valueSignal(rankingSignals.styleAffinities, profile.drinkStyle)) +
      (preferences.effort ? 0 : valueSignal(rankingSignals.effortAffinities, profile.effort)) +
      (preferences.temperature ? 0 : listSignal(rankingSignals.temperatureAffinities, profile.temperature)) +
      (preferences.taste ? 0 : listSignal(rankingSignals.tasteAffinities, profile.tastes)) +
      valueSignal(rankingSignals.drinkAffinities, profile.name);

    if (affinityScore !== 0) {
      score += affinityScore * PERSONALIZATION_WEIGHTS.rankingAffinity;
      if (affinityScore > 0) {
        personalizationReasons.push("is boosted by your live ranking signals");
      }
    }

    if (preferences.time) {
      const timeSignal = valueSignal(rankingSignals.timeAffinities, preferences.time);
      score += timeSignal * 0.9;
    }

    if (preferences.mood) {
      const moodSignal = valueSignal(rankingSignals.moodAffinities, preferences.mood);
      score += moodSignal * 0.9;
    }
  }

  return { score, reasons, personalizationReasons };
}

function createReasoning(drink, preferences, reasons, personalizationReasons, explorationUsed, adaptiveProfile) {
  const tasteLine = `Its ${drink.tastes.join(" and ")} profile aligns with what you asked for.`;
  const caffeineLine = `It delivers a ${drink.caffeineLevel} caffeine level, which suits a ${preferences.mood || "current"} mood and a ${preferences.caffeinePreference || drink.caffeineLevel} energy preference.`;
  const timeLine = `It is a strong fit for ${preferences.time || "this time of day"} and works as a ${drink.temperature.join(" or ")} option.`;
  const textureLine = `Its body is ${drink.texture} with a ${drink.drinkStyle} profile, which helps it feel closer to an everyday drinking style rather than a one-off match.`;
  const effortLine = `The preparation is ${drink.effort}, so it stays compatible with the amount of effort you want.`;
  const learnedLine = adaptiveProfile.historyDepth >= 3 && personalizationReasons.length
    ? `It also aligns with your learned profile by ${personalizationReasons.slice(0, 2).join(" and ")}.`
    : "As your history grows, the system will adapt more strongly to your long-term coffee patterns.";
  const exploreLine = explorationUsed
    ? "Exploration mode nudged the result slightly outside your most familiar pattern to encourage discovery."
    : "The recommendation stays close to your stated preferences and recent habits.";

  const topReasons = reasons.length ? reasons.slice(0, 3).join(" and ") : "fits your overall profile";

  return `${drink.name} was selected because it ${topReasons}. ${tasteLine} ${caffeineLine} ${timeLine} ${textureLine} ${effortLine} ${learnedLine} ${exploreLine}`;
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
    reasoning: createReasoning(
      selected.profile,
      preferences,
      selected.reasons,
      selected.personalizationReasons,
      explorationUsed,
      historySignals.adaptiveProfile
    ),
    reasonDetails: {
      tasteMatch: selected.profile.tastes,
      caffeineLevel: selected.profile.caffeineLevel,
      sweetnessLevel: selected.profile.sweetnessLevel,
      texture: selected.profile.texture,
      drinkStyle: selected.profile.drinkStyle,
      timeSuitability: selected.profile.times,
      effortCompatibility: selected.profile.effort,
      learnedProfile: historySignals.adaptiveProfile,
      personalizationReasons: selected.personalizationReasons,
      evaluationMetrics: historySignals.adaptiveProfile.evaluationMetrics
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
