import { normalizeHistory, buildFeedbackMap, deriveAdaptiveProfile, scoreHistoricalEvent } from "./personalization.js";

function countBy(items) {
  return items.reduce((accumulator, item) => {
    if (!item) {
      return accumulator;
    }

    accumulator[item] = (accumulator[item] || 0) + 1;
    return accumulator;
  }, {});
}

function topEntry(map, fallback) {
  const winner = Object.entries(map).sort((left, right) => right[1] - left[1])[0];
  return winner ? winner[0] : fallback;
}

function topEntries(map, limit = 3) {
  return Object.entries(map)
    .sort((left, right) => right[1] - left[1])
    .slice(0, limit)
    .map(([label, count]) => ({ label, count }));
}

function scoreDrink(event, feedbackMap) {
  return Math.max(1, scoreHistoricalEvent({
    ...event,
    liked: feedbackMap[event.recommendation] === "like" || event.liked,
    disliked: feedbackMap[event.recommendation] === "dislike" || event.disliked
  }));
}

function buildContextLeaders(events, feedbackMap, key) {
  const buckets = {};

  events.forEach((event) => {
    const value = event.preferences?.[key];
    if (!value) {
      return;
    }

    buckets[value] = buckets[value] || {};
    buckets[value][event.recommendation] = (buckets[value][event.recommendation] || 0) + scoreDrink(event, feedbackMap);
  });

  return Object.fromEntries(
    Object.entries(buckets).map(([bucket, scores]) => [bucket, topEntries(scores)])
  );
}

function deriveExploration(events) {
  const recommendationEvents = events.filter((event) => event.type === "filter" || event.type === "chat");
  const explorationCount = recommendationEvents.filter((event) => event.explorationUsed).length;
  const total = recommendationEvents.length || 1;
  const ratio = explorationCount / total;

  let label = "Comfort Zone Drinker";
  if (ratio >= 0.35) {
    label = "Adventure Seeker";
  } else if (ratio >= 0.18) {
    label = "Balanced Explorer";
  }

  return {
    ratio,
    familiarShare: Math.round((1 - ratio) * 100),
    explorationShare: Math.round(ratio * 100),
    label
  };
}

function buildPassport(userName, tasteProfile, exploration, feedbackMap, recommendationCounts) {
  const likedCount = Object.values(feedbackMap).filter((feedback) => feedback === "like").length;
  const topDrink = topEntry(recommendationCounts, "Latte");

  let archetype = "Comfort-Driven Regular";
  if (exploration.label === "Adventure Seeker") {
    archetype = "Curious Coffee Wanderer";
  } else if (tasteProfile.favoriteStyle === "straight") {
    archetype = "Focused Minimalist";
  } else if (tasteProfile.favoriteStyle === "indulgent") {
    archetype = "Treat-Led Sipper";
  } else if (tasteProfile.favoriteStyle === "refreshing") {
    archetype = "Cool Routine Optimizer";
  }

  return {
    userName,
    archetype,
    headline: `${userName} tends to favor ${tasteProfile.favoriteTexture}, ${tasteProfile.preferredCaffeine} caffeine drinks, usually around ${tasteProfile.signatureTime}.`,
    explorationLabel: exploration.label,
    favoriteStyle: tasteProfile.favoriteStyle,
    signatureTime: tasteProfile.signatureTime,
    topDrink,
    likedCount
  };
}

function buildHabitInsights(passport, tasteProfile, exploration, timeLeaders, moodLeaders) {
  const notes = [
    `Your coffee rhythm is strongest in the ${passport.signatureTime}, where you return most often to ${passport.topDrink}.`,
    `Your taste profile leans ${tasteProfile.favoriteTexture} and ${tasteProfile.sweetnessTolerance}, which points to a ${tasteProfile.favoriteStyle} drinking style.`,
    `You currently behave like a ${exploration.label.toLowerCase()}, with ${exploration.explorationShare}% of saved recommendations coming from exploration mode.`
  ];

  const morningTop = timeLeaders.morning?.[0]?.label;
  if (morningTop) {
    notes.push(`When it is morning, your strongest liked pattern currently points toward ${morningTop}.`);
  }

  const relaxedTop = moodLeaders.relaxed?.[0]?.label;
  if (relaxedTop) {
    notes.push(`In relaxed moods, you repeatedly gravitate toward ${relaxedTop}.`);
  }

  return notes;
}

function buildTimeline(history = []) {
  return history
    .slice()
    .sort((left, right) => new Date(right.timestamp || 0) - new Date(left.timestamp || 0))
    .slice(0, 8)
    .map((entry) => ({
      recommendation: entry.recommendation,
      type: entry.type,
      feedback: entry.feedback || null,
      timestamp: entry.timestamp,
      detail: entry.feedback
        ? `Marked ${entry.recommendation} as ${entry.feedback}.`
        : entry.prompt || entry.preferences?.mood || "Saved recommendation event."
    }));
}

export function deriveDashboardData(history = [], userName = "Guest") {
  const events = normalizeHistory(history);
  const feedbackMap = buildFeedbackMap(history);
  const recommendationEvents = events.filter((event) => event.type === "filter" || event.type === "chat");
  const recommendationCounts = countBy(recommendationEvents.map((event) => event.recommendation));
  const adaptiveProfile = deriveAdaptiveProfile(history);
  const tasteProfile = {
    preferredCaffeine: adaptiveProfile.preferredCaffeine,
    sweetnessTolerance: adaptiveProfile.preferredSweetness,
    favoriteTexture: adaptiveProfile.preferredTexture,
    favoriteStyle: adaptiveProfile.preferredStyle,
    dominantTaste: adaptiveProfile.dominantTaste,
    signatureTime: adaptiveProfile.signatureTime
  };
  const exploration = deriveExploration(recommendationEvents);
  const passport = buildPassport(userName, tasteProfile, exploration, feedbackMap, recommendationCounts);
  const timeLeaders = buildContextLeaders(recommendationEvents, feedbackMap, "time");
  const moodLeaders = buildContextLeaders(recommendationEvents, feedbackMap, "mood");

  return {
    passport,
    tasteProfile,
    exploration,
    evaluationMetrics: adaptiveProfile.evaluationMetrics,
    topDrinks: topEntries(recommendationCounts, 5),
    timeLeaders,
    moodLeaders,
    timeline: buildTimeline(history),
    habitInsights: buildHabitInsights(passport, tasteProfile, exploration, timeLeaders, moodLeaders),
    hasEnoughData: recommendationEvents.length >= 3
  };
}
