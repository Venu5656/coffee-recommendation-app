export const coffeeProfiles = [
  {
    id: "ristretto",
    name: "Ristretto",
    description: "A shorter espresso shot with a dense, punchy flavor and almost no softness.",
    caffeineLevel: "medium",
    temperature: ["hot"],
    effort: "quick",
    tastes: ["bitter"],
    moods: ["tired", "energetic"],
    times: ["morning", "afternoon"],
    sweetnessLevel: "not-sweet",
    texture: "light",
    drinkStyle: "straight",
    moodsLifestyle: ["minimalist", "focused"],
    tags: ["compact", "intense", "focused"],
    composition: {
      coffee: 95,
      water: 5
    }
  },
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
    sweetnessLevel: "not-sweet",
    texture: "light",
    drinkStyle: "straight",
    moodsLifestyle: ["focused", "routine"],
    tags: ["classic", "strong", "focused"],
    composition: {
      coffee: 90,
      water: 10
    }
  },
  {
    id: "doppio",
    name: "Doppio",
    description: "A double espresso for people who want a stronger ritual without extra dilution.",
    caffeineLevel: "high",
    temperature: ["hot"],
    effort: "quick",
    tastes: ["bitter"],
    moods: ["tired", "energetic"],
    times: ["morning", "afternoon"],
    sweetnessLevel: "not-sweet",
    texture: "light",
    drinkStyle: "straight",
    moodsLifestyle: ["high-energy", "deadline"],
    tags: ["double-shot", "intense"],
    composition: {
      coffee: 92,
      water: 8
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
    sweetnessLevel: "not-sweet",
    texture: "light",
    drinkStyle: "straight",
    moodsLifestyle: ["routine", "practical"],
    tags: ["balanced", "easygoing"],
    composition: {
      coffee: 45,
      water: 55
    }
  },
  {
    id: "pour-over",
    name: "Pour Over",
    description: "A cleaner, aromatic cup for drinkers who care about nuance more than heaviness.",
    caffeineLevel: "medium",
    temperature: ["hot"],
    effort: "elaborate",
    tastes: ["smooth", "bitter"],
    moods: ["relaxed", "energetic"],
    times: ["morning", "afternoon"],
    sweetnessLevel: "not-sweet",
    texture: "light",
    drinkStyle: "straight",
    moodsLifestyle: ["slow-routine", "curious"],
    tags: ["manual", "nuanced", "aromatic"],
    composition: {
      coffee: 35,
      water: 65
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
    sweetnessLevel: "not-sweet",
    texture: "light",
    drinkStyle: "refreshing",
    moodsLifestyle: ["commuter", "summer"],
    tags: ["refreshing", "adventurous"],
    composition: {
      coffee: 55,
      water: 45
    }
  },
  {
    id: "nitro-cold-brew",
    name: "Nitro Cold Brew",
    description: "Cold brew infused for a velvety finish that still lands with serious energy.",
    caffeineLevel: "high",
    temperature: ["iced"],
    effort: "elaborate",
    tastes: ["smooth", "bitter"],
    moods: ["energetic", "tired"],
    times: ["morning", "afternoon"],
    sweetnessLevel: "not-sweet",
    texture: "creamy",
    drinkStyle: "refreshing",
    moodsLifestyle: ["trend-aware", "afternoon-pickup"],
    tags: ["velvety", "modern"],
    composition: {
      coffee: 60,
      water: 40
    }
  },
  {
    id: "iced-americano",
    name: "Iced Americano",
    description: "A crisp and simple choice for drinkers who want clarity without milk.",
    caffeineLevel: "medium",
    temperature: ["iced"],
    effort: "quick",
    tastes: ["bitter", "smooth"],
    moods: ["energetic", "relaxed"],
    times: ["afternoon", "night"],
    sweetnessLevel: "not-sweet",
    texture: "light",
    drinkStyle: "refreshing",
    moodsLifestyle: ["simple", "on-the-go"],
    tags: ["clean", "crisp"],
    composition: {
      coffee: 35,
      water: 65
    }
  },
  {
    id: "macchiato",
    name: "Macchiato",
    description: "Espresso marked with a small amount of milk for someone who wants edge with a touch of softness.",
    caffeineLevel: "high",
    temperature: ["hot"],
    effort: "quick",
    tastes: ["bitter", "smooth"],
    moods: ["energetic", "tired"],
    times: ["morning", "afternoon"],
    sweetnessLevel: "not-sweet",
    texture: "foamy",
    drinkStyle: "straight",
    moodsLifestyle: ["minimalist", "traditional"],
    tags: ["compact", "layered"],
    composition: {
      coffee: 80,
      milk: 10,
      foam: 10
    }
  },
  {
    id: "cortado",
    name: "Cortado",
    description: "A balanced mix of espresso and milk that feels serious without becoming harsh.",
    caffeineLevel: "medium",
    temperature: ["hot"],
    effort: "quick",
    tastes: ["smooth", "bitter"],
    moods: ["relaxed", "energetic"],
    times: ["morning", "afternoon"],
    sweetnessLevel: "not-sweet",
    texture: "creamy",
    drinkStyle: "milky",
    moodsLifestyle: ["balanced", "city-cafe"],
    tags: ["balanced", "compact"],
    composition: {
      coffee: 50,
      milk: 45,
      foam: 5
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
    sweetnessLevel: "not-sweet",
    texture: "creamy",
    drinkStyle: "milky",
    moodsLifestyle: ["daily-regular", "refined"],
    tags: ["refined", "silky"],
    composition: {
      coffee: 40,
      milk: 50,
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
    sweetnessLevel: "not-sweet",
    texture: "foamy",
    drinkStyle: "milky",
    moodsLifestyle: ["classic-cafe", "morning-ritual"],
    tags: ["textured", "classic"],
    composition: {
      coffee: 35,
      milk: 35,
      foam: 30
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
    sweetnessLevel: "lightly-sweet",
    texture: "creamy",
    drinkStyle: "milky",
    moodsLifestyle: ["comfort-seeking", "steady"],
    tags: ["comfort", "creamy"],
    composition: {
      coffee: 30,
      milk: 60,
      foam: 10
    }
  },
  {
    id: "cafe-au-lait",
    name: "Cafe au Lait",
    description: "Brewed coffee with warm milk for a softer everyday routine drink.",
    caffeineLevel: "medium",
    temperature: ["hot"],
    effort: "quick",
    tastes: ["smooth"],
    moods: ["relaxed", "tired"],
    times: ["morning", "afternoon"],
    sweetnessLevel: "lightly-sweet",
    texture: "creamy",
    drinkStyle: "milky",
    moodsLifestyle: ["home-brewer", "habitual"],
    tags: ["simple", "gentle"],
    composition: {
      coffee: 45,
      milk: 55
    }
  },
  {
    id: "vanilla-latte",
    name: "Vanilla Latte",
    description: "A familiar latte with a sweeter finish for comfort-driven drinkers.",
    caffeineLevel: "medium",
    temperature: ["hot", "iced"],
    effort: "quick",
    tastes: ["sweet", "smooth"],
    moods: ["relaxed", "tired"],
    times: ["afternoon", "night"],
    sweetnessLevel: "sweet",
    texture: "creamy",
    drinkStyle: "milky",
    moodsLifestyle: ["comfort-seeking", "friendly"],
    tags: ["approachable", "sweet"],
    composition: {
      coffee: 25,
      milk: 50,
      sugar: 15,
      foam: 10
    }
  },
  {
    id: "caramel-latte",
    name: "Caramel Latte",
    description: "Round, mellow, and dessert-leaning without fully becoming a treat drink.",
    caffeineLevel: "medium",
    temperature: ["hot", "iced"],
    effort: "quick",
    tastes: ["sweet", "smooth"],
    moods: ["relaxed", "energetic"],
    times: ["afternoon", "night"],
    sweetnessLevel: "sweet",
    texture: "creamy",
    drinkStyle: "indulgent",
    moodsLifestyle: ["treat-yourself", "social"],
    tags: ["sweet", "soft"],
    composition: {
      coffee: 25,
      milk: 45,
      sugar: 20,
      foam: 10
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
    sweetnessLevel: "sweet",
    texture: "creamy",
    drinkStyle: "indulgent",
    moodsLifestyle: ["dessert-cup", "cozy-evening"],
    tags: ["indulgent", "cozy"],
    composition: {
      coffee: 25,
      milk: 45,
      chocolate: 20,
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
    sweetnessLevel: "sweet",
    texture: "creamy",
    drinkStyle: "refreshing",
    moodsLifestyle: ["casual", "social"],
    tags: ["playful", "approachable"],
    composition: {
      coffee: 25,
      milk: 45,
      sugar: 20,
      water: 10
    }
  },
  {
    id: "iced-caramel-macchiato",
    name: "Iced Caramel Macchiato",
    description: "Layered, sweet, and high on coffee-shop energy for people who treat coffee like a small event.",
    caffeineLevel: "medium",
    temperature: ["iced"],
    effort: "elaborate",
    tastes: ["sweet", "smooth"],
    moods: ["energetic", "relaxed"],
    times: ["afternoon", "night"],
    sweetnessLevel: "sweet",
    texture: "creamy",
    drinkStyle: "indulgent",
    moodsLifestyle: ["social", "treat-yourself"],
    tags: ["layered", "cafe-style"],
    composition: {
      coffee: 25,
      milk: 40,
      sugar: 20,
      foam: 5,
      water: 10
    }
  },
  {
    id: "affogato",
    name: "Affogato",
    description: "Hot espresso over something cold and sweet, sitting right between coffee and dessert.",
    caffeineLevel: "low",
    temperature: ["hot"],
    effort: "elaborate",
    tastes: ["sweet", "smooth"],
    moods: ["relaxed", "energetic"],
    times: ["afternoon", "night"],
    sweetnessLevel: "sweet",
    texture: "creamy",
    drinkStyle: "indulgent",
    moodsLifestyle: ["dessert-first", "weekend"],
    tags: ["dessert", "playful"],
    composition: {
      coffee: 30,
      milk: 45,
      sugar: 15,
      foam: 10
    }
  }
];

export const filterOptions = {
  mood: ["tired", "relaxed", "energetic"],
  taste: ["bitter", "smooth", "sweet"],
  time: ["morning", "afternoon", "night"],
  temperature: ["hot", "iced"],
  effort: ["quick", "elaborate"],
  caffeinePreference: ["low", "medium", "high"],
  sweetnessPreference: ["not-sweet", "lightly-sweet", "sweet"],
  texturePreference: ["light", "creamy", "foamy"],
  drinkStyle: ["straight", "milky", "refreshing", "indulgent"]
};
