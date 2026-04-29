export const coffeeProfiles = [
  {
    id: "espresso",
    name: "Espresso",
    description: "A concentrated shot with bold flavor and a fast caffeine lift.",
    caffeineLevel: "high",
    temperature: ["hot"],
    effort: "quick",
    tastes: ["bitter"],
    moods: ["tired", "energetic"],
    times: ["morning", "afternoon"],
    tags: ["classic", "strong", "focused"],
    composition: {
      coffee: 90,
      water: 10
    }
  },
  {
    id: "americano",
    name: "Americano",
    description: "Espresso softened with water for a smooth but still assertive cup.",
    caffeineLevel: "medium",
    temperature: ["hot", "iced"],
    effort: "quick",
    tastes: ["bitter", "smooth"],
    moods: ["tired", "relaxed"],
    times: ["morning", "afternoon", "night"],
    tags: ["balanced", "easygoing"],
    composition: {
      coffee: 45,
      water: 55
    }
  },
  {
    id: "latte",
    name: "Latte",
    description: "Creamy and mellow with enough espresso to stay comforting.",
    caffeineLevel: "medium",
    temperature: ["hot", "iced"],
    effort: "elaborate",
    tastes: ["smooth"],
    moods: ["relaxed", "tired"],
    times: ["morning", "afternoon"],
    tags: ["comfort", "creamy"],
    composition: {
      coffee: 30,
      milk: 60,
      foam: 10
    }
  },
  {
    id: "cappuccino",
    name: "Cappuccino",
    description: "A foamy classic that feels rich while keeping the coffee forward.",
    caffeineLevel: "medium",
    temperature: ["hot"],
    effort: "elaborate",
    tastes: ["bitter", "smooth"],
    moods: ["energetic", "relaxed"],
    times: ["morning", "afternoon"],
    tags: ["textured", "classic"],
    composition: {
      coffee: 35,
      milk: 35,
      foam: 30
    }
  },
  {
    id: "mocha",
    name: "Mocha",
    description: "Chocolate-forward and comforting with a dessert-like finish.",
    caffeineLevel: "medium",
    temperature: ["hot", "iced"],
    effort: "elaborate",
    tastes: ["sweet", "smooth"],
    moods: ["tired", "relaxed"],
    times: ["afternoon", "night"],
    tags: ["indulgent", "cozy"],
    composition: {
      coffee: 25,
      milk: 45,
      chocolate: 20,
      foam: 10
    }
  },
  {
    id: "cold-brew",
    name: "Cold Brew",
    description: "Slow-steeped and refreshing with a strong, smooth caffeine kick.",
    caffeineLevel: "high",
    temperature: ["iced"],
    effort: "quick",
    tastes: ["smooth", "bitter"],
    moods: ["tired", "energetic"],
    times: ["morning", "afternoon"],
    tags: ["refreshing", "adventurous"],
    composition: {
      coffee: 55,
      water: 45
    }
  },
  {
    id: "flat-white",
    name: "Flat White",
    description: "Velvety milk with a stronger espresso edge than a latte.",
    caffeineLevel: "medium",
    temperature: ["hot"],
    effort: "elaborate",
    tastes: ["smooth", "bitter"],
    moods: ["energetic", "relaxed"],
    times: ["morning", "afternoon"],
    tags: ["refined", "silky"],
    composition: {
      coffee: 40,
      milk: 50,
      foam: 10
    }
  },
  {
    id: "iced-vanilla-latte",
    name: "Iced Vanilla Latte",
    description: "Sweet, chilled, and easy to drink when you want something friendly.",
    caffeineLevel: "medium",
    temperature: ["iced"],
    effort: "quick",
    tastes: ["sweet", "smooth"],
    moods: ["relaxed", "energetic"],
    times: ["afternoon", "night"],
    tags: ["playful", "approachable"],
    composition: {
      coffee: 25,
      milk: 45,
      sugar: 20,
      water: 10
    }
  }
];

export const filterOptions = {
  moods: ["tired", "relaxed", "energetic"],
  tastes: ["bitter", "smooth", "sweet"],
  times: ["morning", "afternoon", "night"],
  temperatures: ["hot", "iced"],
  efforts: ["quick", "elaborate"]
};
