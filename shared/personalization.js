import { coffeeProfiles } from "./coffeeProfiles.js";

const profileByName = Object.fromEntries(coffeeProfiles.map((profile) => [profile.name, profile]));

function countBy(items) {
  return items.reduce((accumulator, item) => {
    if (!item) {
      return accumulator;
    }

    accumulator[item] = (accumulator[item] || 0) + 1;
    return accumulator;
  }, {});
}

function topEntry(map, fallback = null) {
  const winner = Object.entries(map).sort((left, right) => right[1] - left[1])[0];
  return winner ? winner[0] : fallback;
}

function averageMap(entries) {
  return Object.fromEntries(
    Object.entries(entries).map(([key, value]) => [
      key,
      value.count ? value.total / value.count : 0
    ])
  );
}

function weightedTop(weightedProfiles, selector, fallback) {
  const counts = countBy(weightedProfiles.map((profile) => selector(profile)).flat().filter(Boolean));
  return topEntry(counts, fallback);
}

function updateAverageStore(store, key, reward) {
  if (!key) {
    return;
  }

  store[key] = store[key] || { total: 0, count: 0 };
  store[key].total += reward;
  store[key].count += 1;
}

export function normalizeHistory(history = []) {
  return history
    .filter((entry) => entry?.recommendation)
    .map((entry) => {
      const profile = profileByName[entry.recommendation] || profileByName[entry.name] || null;
      const preferences = entry.preferences || entry.extractedPreferences || null;
      const metadata = entry.metadata || {};

      return {
        recommendation: entry.recommendation || entry.name,
        type: entry.type || "history",
        timestamp: entry.timestamp || null,
        preferences,
        feedback: entry.feedback || null,
        liked: entry.feedback === "like" || entry.liked === true,
        disliked: entry.feedback === "dislike" || entry.disliked === true,
        explorationUsed: Boolean(metadata.explorationUsed || entry.explorationUsed),
        profile
      };
    });
}

export function buildFeedbackMap(history = []) {
  return history.reduce((accumulator, entry) => {
    const recommendation = entry?.recommendation || entry?.name;
    if (!recommendation || !entry.feedback) {
      return accumulator;
    }

    accumulator[recommendation] = entry.feedback;
    return accumulator;
  }, {});
}

export function scoreHistoricalEvent(event) {
  let score = 1;

  if (event.liked) {
    score += 4;
  }

  if (event.disliked) {
    score -= 3;
  }

  if (event.explorationUsed) {
    score += 1;
  }

  return score;
}

function recommendationReward(event) {
  if (event.liked) {
    return 1;
  }

  if (event.disliked) {
    return -1;
  }

  return 0.15;
}

export function deriveAdaptiveProfile(history = []) {
  const events = normalizeHistory(history);
  const recommendationEvents = events.filter((event) => event.profile);
  const recommendationOnlyEvents = recommendationEvents.filter(
    (event) => event.type === "filter" || event.type === "chat" || event.type === "history"
  );
  const weightedProfiles = recommendationEvents.flatMap((event) => {
    const weight = Math.max(1, scoreHistoricalEvent(event));
    return Array.from({ length: weight }, () => event.profile);
  });

  const recommendationCounts = countBy(recommendationEvents.map((event) => event.recommendation));
  const timeCounts = countBy(recommendationEvents.map((event) => event.preferences?.time).filter(Boolean));
  const moodCounts = countBy(recommendationEvents.map((event) => event.preferences?.mood).filter(Boolean));
  const dislikedDrinks = recommendationEvents.filter((event) => event.disliked).map((event) => event.recommendation);
  const dislikedTastes = recommendationEvents
    .filter((event) => event.disliked)
    .flatMap((event) => event.profile?.tastes || []);

  const caffeineAffinities = {};
  const sweetnessAffinities = {};
  const textureAffinities = {};
  const styleAffinities = {};
  const effortAffinities = {};
  const temperatureAffinities = {};
  const tasteAffinities = {};
  const drinkAffinities = {};
  const timeAffinities = {};
  const moodAffinities = {};

  recommendationOnlyEvents.forEach((event) => {
    const reward = recommendationReward(event);
    const profile = event.profile;
    if (!profile) {
      return;
    }

    updateAverageStore(caffeineAffinities, profile.caffeineLevel, reward);
    updateAverageStore(sweetnessAffinities, profile.sweetnessLevel, reward);
    updateAverageStore(textureAffinities, profile.texture, reward);
    updateAverageStore(styleAffinities, profile.drinkStyle, reward);
    updateAverageStore(effortAffinities, profile.effort, reward);
    profile.temperature.forEach((value) => updateAverageStore(temperatureAffinities, value, reward));
    profile.tastes.forEach((value) => updateAverageStore(tasteAffinities, value, reward));
    updateAverageStore(drinkAffinities, event.recommendation, reward);
    updateAverageStore(timeAffinities, event.preferences?.time, reward);
    updateAverageStore(moodAffinities, event.preferences?.mood, reward);
  });

  const likeCount = recommendationEvents.filter((event) => event.liked).length;
  const dislikeCount = recommendationEvents.filter((event) => event.disliked).length;
  const feedbackCount = likeCount + dislikeCount;
  const explorationEvents = recommendationOnlyEvents.filter((event) => event.explorationUsed);
  const explorationFeedbackEvents = explorationEvents.filter((event) => event.liked || event.disliked);
  const successfulExploration = explorationFeedbackEvents.filter((event) => event.liked).length;
  const repeatedFavoriteCount = topEntry(recommendationCounts, null)
    ? recommendationCounts[topEntry(recommendationCounts, null)] || 0
    : 0;
  const learningConfidence = Math.min(1, recommendationOnlyEvents.length / 15);

  return {
    historyDepth: recommendationEvents.length,
    favoriteDrink: topEntry(recommendationCounts, null),
    preferredCaffeine: weightedTop(weightedProfiles, (profile) => profile.caffeineLevel, "medium"),
    preferredSweetness: weightedTop(weightedProfiles, (profile) => profile.sweetnessLevel, "lightly-sweet"),
    preferredTexture: weightedTop(weightedProfiles, (profile) => profile.texture, "creamy"),
    preferredStyle: weightedTop(weightedProfiles, (profile) => profile.drinkStyle, "milky"),
    preferredTemperature: weightedTop(weightedProfiles, (profile) => profile.temperature, "hot"),
    preferredEffort: weightedTop(weightedProfiles, (profile) => profile.effort, "quick"),
    dominantTaste: weightedTop(weightedProfiles, (profile) => profile.tastes, "smooth"),
    signatureTime: topEntry(timeCounts, "afternoon"),
    signatureMood: topEntry(moodCounts, "relaxed"),
    dislikedDrinks,
    dislikedTastes: Array.from(new Set(dislikedTastes)),
    timeCounts,
    moodCounts,
    learningConfidence,
    rankingSignals: {
      caffeineAffinities: averageMap(caffeineAffinities),
      sweetnessAffinities: averageMap(sweetnessAffinities),
      textureAffinities: averageMap(textureAffinities),
      styleAffinities: averageMap(styleAffinities),
      effortAffinities: averageMap(effortAffinities),
      temperatureAffinities: averageMap(temperatureAffinities),
      tasteAffinities: averageMap(tasteAffinities),
      drinkAffinities: averageMap(drinkAffinities),
      timeAffinities: averageMap(timeAffinities),
      moodAffinities: averageMap(moodAffinities)
    },
    evaluationMetrics: {
      totalRecommendations: recommendationOnlyEvents.length,
      totalFeedback: feedbackCount,
      likeRate: feedbackCount ? likeCount / feedbackCount : 0,
      dislikeRate: feedbackCount ? dislikeCount / feedbackCount : 0,
      explorationRate: recommendationOnlyEvents.length
        ? explorationEvents.length / recommendationOnlyEvents.length
        : 0,
      explorationSuccessRate: explorationFeedbackEvents.length
        ? successfulExploration / explorationFeedbackEvents.length
        : 0,
      repeatRate: recommendationOnlyEvents.length
        ? repeatedFavoriteCount / recommendationOnlyEvents.length
        : 0,
      adaptationReadiness: learningConfidence >= 0.7 ? "high" : learningConfidence >= 0.35 ? "medium" : "early"
    }
  };
}
