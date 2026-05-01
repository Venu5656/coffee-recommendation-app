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

function normalizeEvents(history = []) {
  return history
    .filter((entry) => entry?.recommendation)
    .map((entry) => {
      const profile = profileByName[entry.recommendation] || null;
      const preferences = entry.preferences || entry.extractedPreferences || null;
      const metadata = entry.metadata || {};

      return {
        recommendation: entry.recommendation,
        type: entry.type,
        timestamp: entry.timestamp,
        preferences,
        feedback: entry.feedback || null,
        explorationUsed: Boolean(metadata.explorationUsed || entry.explorationUsed),
        profile
      };
    });
}

function buildFeedbackMap(history = []) {
  return history.reduce((accumulator, entry) => {
    if (!entry?.recommendation || !entry.feedback) {
      return accumulator;
    }

    accumulator[entry.recommendation] = entry.feedback;
    return accumulator;
  }, {});
}

function scoreDrink(event, feedbackMap) {
  let score = 1;

  if (feedbackMap[event.recommendation] === "like") {
    score += 4;
  }

  if (feedbackMap[event.recommendation] === "dislike") {
    score -= 2;
  }

  if (event.explorationUsed) {
    score += 1;
  }

  return score;
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

function buildTasteProfile(events, feedbackMap) {
  const weightedProfiles = events.flatMap((event) => {
    if (!event.profile) {
      return [];
    }

    const weight = Math.max(1, scoreDrink(event, feedbackMap));
    return Array.from({ length: weight }, () => event.profile);
  });

  const caffeineCounts = countBy(weightedProfiles.map((profile) => profile.caffeineLevel));
  const sweetnessCounts = countBy(weightedProfiles.map((profile) => profile.sweetnessLevel));
  const textureCounts = countBy(weightedProfiles.map((profile) => profile.texture));
  const styleCounts = countBy(weightedProfiles.map((profile) => profile.drinkStyle));
  const tasteCounts = countBy(weightedProfiles.flatMap((profile) => profile.tastes));
  const timeCounts = countBy(events.map((event) => event.preferences?.time).filter(Boolean));

  return {
    preferredCaffeine: topEntry(caffeineCounts, "medium"),
    sweetnessTolerance: topEntry(sweetnessCounts, "lightly-sweet"),
    favoriteTexture: topEntry(textureCounts, "creamy"),
    favoriteStyle: topEntry(styleCounts, "milky"),
    dominantTaste: topEntry(tasteCounts, "smooth"),
    signatureTime: topEntry(timeCounts, "afternoon")
  };
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
  const events = normalizeEvents(history);
  const feedbackMap = buildFeedbackMap(history);
  const recommendationEvents = events.filter((event) => event.type === "filter" || event.type === "chat");
  const recommendationCounts = countBy(recommendationEvents.map((event) => event.recommendation));
  const tasteProfile = buildTasteProfile(recommendationEvents, feedbackMap);
  const exploration = deriveExploration(recommendationEvents);
  const passport = buildPassport(userName, tasteProfile, exploration, feedbackMap, recommendationCounts);
  const timeLeaders = buildContextLeaders(recommendationEvents, feedbackMap, "time");
  const moodLeaders = buildContextLeaders(recommendationEvents, feedbackMap, "mood");

  return {
    passport,
    tasteProfile,
    exploration,
    topDrinks: topEntries(recommendationCounts, 5),
    timeLeaders,
    moodLeaders,
    timeline: buildTimeline(history),
    habitInsights: buildHabitInsights(passport, tasteProfile, exploration, timeLeaders, moodLeaders),
    hasEnoughData: recommendationEvents.length >= 3
  };
}
