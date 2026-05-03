export const customCoffeeDrinks = [
  {
    id: "espresso-tonic",
    name: "Espresso Tonic",
    description: "A bright, sparkling espresso drink with a bitter-citrus finish and a modern cafe feel.",
    tags: ["refreshing", "bitter", "iced", "adventurous"],
    homeGuide: {
      equipment: ["espresso machine or moka pot", "glass", "ice"],
      ingredients: [
        "1 double shot espresso",
        "120-150 ml chilled tonic water",
        "ice",
        "optional orange peel"
      ],
      steps: [
        "Fill a glass with ice and tonic first.",
        "Pour the espresso slowly over the back of a spoon for cleaner layering.",
        "Add orange peel if you want a brighter aroma.",
        "Stir gently just before drinking."
      ],
      tips: [
        "Use very cold tonic so the drink stays lively.",
        "A concentrated moka pot brew works if you do not have espresso."
      ]
    }
  },
  {
    id: "vietnamese-iced-coffee",
    name: "Vietnamese Iced Coffee",
    description: "A bold and sweet iced coffee built from dark coffee and condensed milk.",
    tags: ["sweet", "strong", "iced", "rich"],
    homeGuide: {
      equipment: ["phin filter or strong brew method", "glass", "ice"],
      ingredients: [
        "2-3 tablespoons sweetened condensed milk",
        "90-120 ml strong dark coffee",
        "ice"
      ],
      steps: [
        "Add condensed milk to a glass.",
        "Brew or pour strong coffee over it.",
        "Stir until fully combined.",
        "Pour over ice and serve."
      ],
      tips: [
        "Use darker roast coffee for the right intensity.",
        "Make the coffee stronger rather than adding more sweetness if it tastes flat."
      ]
    }
  },
  {
    id: "dirty-chai",
    name: "Dirty Chai Latte",
    description: "A chai latte sharpened with espresso for a spiced, comforting, caffeinated cup.",
    tags: ["spiced", "comforting", "milky", "hot"],
    homeGuide: {
      equipment: ["espresso machine or moka pot", "saucepan or milk steamer"],
      ingredients: [
        "1 shot espresso",
        "180 ml chai concentrate or strong chai",
        "120 ml milk"
      ],
      steps: [
        "Prepare a strong chai base.",
        "Heat or steam the milk until silky.",
        "Pour chai into the cup, then add espresso.",
        "Finish with the milk and optional cinnamon."
      ],
      tips: [
        "Use less chai if you want more coffee definition.",
        "Oat milk works especially well here."
      ]
    }
  },
  {
    id: "red-eye",
    name: "Red Eye",
    description: "A brewed coffee strengthened with espresso for users who want function-first caffeine.",
    tags: ["strong", "high-caffeine", "straight", "hot"],
    homeGuide: {
      equipment: ["drip brewer or pour over", "espresso machine or moka pot"],
      ingredients: [
        "1 cup brewed coffee",
        "1 shot espresso"
      ],
      steps: [
        "Brew a regular cup of coffee.",
        "Make one separate espresso shot.",
        "Combine them and serve immediately."
      ],
      tips: [
        "Lower the base brew strength slightly if it turns too harsh.",
        "Best used when caffeine is the main priority."
      ]
    }
  },
  {
    id: "shakerato",
    name: "Shakerato",
    description: "An Italian-style shaken espresso that feels colder, lighter, and more elegant than a standard iced coffee.",
    tags: ["refreshing", "smooth", "iced", "light"],
    homeGuide: {
      equipment: ["cocktail shaker or sealed jar", "ice"],
      ingredients: [
        "2 shots espresso",
        "ice",
        "optional sugar syrup"
      ],
      steps: [
        "Pull the espresso shots fresh.",
        "Add them to a shaker with ice and optional syrup.",
        "Shake hard for 10-15 seconds.",
        "Strain into a chilled glass."
      ],
      tips: [
        "Shake hard enough to build a light foam on top.",
        "Drink quickly while the texture is still lively."
      ]
    }
  }
];

export const coffeeKnowledge = {
  history: {
    title: "Coffee History",
    summary:
      "Coffee evolved from a regional ritual drink into a global daily habit through trade, coffeehouse culture, industrial scale, and specialty craft movements.",
    bullets: [
      "Early coffee drinking was tied to ritual, study, and social gathering.",
      "Coffeehouses later became spaces for conversation, work, and public exchange.",
      "Industrial distribution normalized coffee as a daily routine product.",
      "Specialty coffee shifted attention toward origin, roast, and brewing craft."
    ]
  },
  brewing: {
    title: "Brewing Methods",
    summary:
      "Different brew methods change body, clarity, sweetness, and perceived acidity more than many drinkers expect.",
    bullets: [
      "Espresso is concentrated, intense, and texture-driven.",
      "Pour over usually gives clearer flavors and more separation in the cup.",
      "French press creates heavier body and more oils.",
      "Cold brew often tastes smoother and less sharp than hot extraction."
    ]
  },
  terms: {
    title: "Coffee Terms",
    summary:
      "Many coffee terms describe extraction balance, mouthfeel, roast behavior, or preparation style rather than just naming drinks.",
    bullets: [
      "Body means how heavy or light coffee feels in the mouth.",
      "Under-extracted coffee often tastes sour, thin, or incomplete.",
      "Over-extracted coffee often tastes bitter, dry, or hollow.",
      "Extraction refers to how much soluble flavor the brew pulled from the grounds."
    ]
  }
};

export const knowledgeTopics = [
  {
    id: "history-global",
    title: "Global Coffee History",
    summary:
      "Coffee spread from East Africa and the Arabian Peninsula into a worldwide habit through trade, religion, colonial routes, coffeehouses, and later industrial and specialty movements.",
    bullets: [
      "Coffee is widely associated with Ethiopian origins and early cultivation and trade through Yemen.",
      "Historic coffeehouses became social and intellectual spaces in the Middle East and Europe.",
      "Colonial agriculture expanded coffee cultivation across Latin America, Asia, and Africa.",
      "Modern specialty coffee shifted attention toward origin, processing, roasting, and brew craft."
    ],
    keywords: ["history", "origin", "global", "world", "worldwide", "where did coffee come from"]
  },
  {
    id: "history-usa",
    title: "Coffee History in the United States",
    summary:
      "Coffee in the United States grew from an imported household staple into a mass-market routine drink and later into a cafe and specialty culture.",
    bullets: [
      "Coffee became popular in the U.S. through trade and everyday domestic consumption rather than a single ritual origin story.",
      "Industrial roasting, canned coffee, and diner culture helped make coffee a daily mainstream habit.",
      "Large chains later normalized takeaway cafe coffee and flavored milk-based drinks.",
      "Third-wave specialty coffee brought more attention to sourcing, roast profiles, brew methods, and espresso quality."
    ],
    keywords: ["usa", "united states", "america", "american", "u.s."]
  },
  {
    id: "history-italy",
    title: "Italian Coffee Tradition",
    summary:
      "Italy shaped modern espresso culture through compact bar service, fast preparation, and drink conventions that still influence cafes worldwide.",
    bullets: [
      "Italian coffee bars helped define espresso as a fast social ritual rather than a long sit-down drink.",
      "Classic drinks such as espresso, cappuccino, macchiato, and shakerato carry strong cultural expectations.",
      "Milk-heavy espresso drinks are often treated as morning drinks in Italian cafe culture.",
      "Italian tradition emphasizes balance, speed, and repeatable bar service more than large customized menus."
    ],
    keywords: ["italy", "italian", "espresso culture", "rome", "milan"]
  },
  {
    id: "history-ethiopia",
    title: "Ethiopian Coffee Tradition",
    summary:
      "Ethiopia holds a foundational place in coffee history and is known for ceremonial preparation, hospitality, and strong ties between coffee and social life.",
    bullets: [
      "Ethiopia is deeply tied to coffee's origin story and to some of the most historically important coffee-growing regions.",
      "Traditional coffee ceremonies emphasize roasting, brewing, aroma, time, and community.",
      "The ritual dimension of Ethiopian coffee is as important as the beverage itself.",
      "Many modern specialty coffees still celebrate Ethiopian beans for floral, citrus, and tea-like character."
    ],
    keywords: ["ethiopia", "ethiopian", "ceremony", "coffee ceremony", "origin"]
  },
  {
    id: "history-turkey",
    title: "Turkish Coffee Tradition",
    summary:
      "Turkish coffee tradition centers on very fine grounds, small servings, and a preparation style that treats coffee as ritual, hospitality, and conversation.",
    bullets: [
      "Turkish coffee is brewed directly with very fine grounds rather than filtered after extraction.",
      "It is often served in small cups and can be tied to hospitality and shared social time.",
      "Texture, foam, and controlled heating matter more than speed.",
      "Its tradition highlights how coffee can function as culture and ceremony rather than just caffeine delivery."
    ],
    keywords: ["turkey", "turkish", "ibrik", "cezve", "middle east", "ottoman"]
  },
  {
    id: "history-vietnam",
    title: "Vietnamese Coffee Tradition",
    summary:
      "Vietnamese coffee culture is known for strong brewing, condensed milk, and practical adaptation to local tastes and ingredients.",
    bullets: [
      "Vietnamese coffee often uses bold coffee and sweetened condensed milk to create high contrast in intensity and sweetness.",
      "The phin filter is central to the visual and practical identity of many Vietnamese coffee drinks.",
      "Iced versions became especially iconic because they fit climate and daily rhythm.",
      "Vietnamese coffee shows how coffee traditions adapt imported crops into distinct local identity."
    ],
    keywords: ["vietnam", "vietnamese", "phin", "condensed milk"]
  },
  {
    id: "brewing-beginners",
    title: "Brewing Basics for Beginners",
    summary:
      "New coffee drinkers learn fastest when they focus on grind, water, ratio, temperature, and tasting rather than chasing advanced equipment first.",
    bullets: [
      "Start with one simple method such as French press, pour over, AeroPress, or basic espresso-style concentrate if available.",
      "Use fresh coffee, clean water, and a repeatable dose-to-water ratio.",
      "If coffee tastes sour or weak, extraction is usually too low; if it tastes harsh or dry, extraction is often too high.",
      "Change one variable at a time so you can actually learn what affected the cup."
    ],
    keywords: ["beginner", "new to coffee", "start brewing", "learn coffee", "how to brew"]
  },
  {
    id: "brewing-methods",
    title: "Coffee Brewing Methods",
    summary:
      "Different brew methods change body, clarity, sweetness, and texture because they extract coffee in different ways and at different concentrations.",
    bullets: [
      "Espresso is concentrated, fast, and texture-driven.",
      "Pour over usually gives clearer flavors and more separation in the cup.",
      "French press creates heavier body and allows more oils through.",
      "Cold brew often tastes smoother and less sharp than hot extraction."
    ],
    keywords: ["method", "methods", "brew method", "brewing", "pour over", "french press", "espresso", "cold brew"]
  },
  {
    id: "brew-ratios",
    title: "Coffee Ratios and Extraction",
    summary:
      "Good brewing usually comes down to balanced ratio, grind size, contact time, and water temperature more than brand or equipment prestige.",
    bullets: [
      "Ratio controls strength and extraction direction more than many beginners expect.",
      "Finer grind usually increases extraction speed, while coarser grind slows it down.",
      "Longer contact time can improve fullness up to a point, then start creating bitterness.",
      "Taste should guide adjustment more than fixed internet recipes."
    ],
    keywords: ["ratio", "extraction", "grind size", "water temperature", "dose", "brew time"]
  },
  {
    id: "coffee-terms",
    title: "Coffee Terms",
    summary:
      "Many coffee terms describe extraction balance, mouthfeel, roast behavior, or preparation style rather than just naming drinks.",
    bullets: [
      "Body means how heavy or light coffee feels in the mouth.",
      "Under-extracted coffee often tastes sour, thin, or incomplete.",
      "Over-extracted coffee often tastes bitter, dry, or hollow.",
      "Extraction refers to how much soluble flavor the brew pulled from the grounds."
    ],
    keywords: ["term", "terms", "body", "extraction", "under extracted", "over extracted", "mouthfeel"]
  },
  {
    id: "beans-arabica-robusta",
    title: "Arabica vs Robusta",
    summary:
      "Arabica and robusta are different species with different flavor tendencies, growing conditions, and typical market roles.",
    bullets: [
      "Arabica is often associated with more nuanced acidity and aromatic complexity.",
      "Robusta is often stronger, earthier, and higher in caffeine.",
      "Neither is automatically better in every use case; blend design and roast matter.",
      "Espresso blends often use robusta strategically for crema and intensity."
    ],
    keywords: ["arabica", "robusta", "beans", "bean types", "species"]
  },
  {
    id: "roast-levels",
    title: "Roast Levels",
    summary:
      "Roast level shapes flavor, body, bitterness, and origin clarity, but it does not act independently from bean type and brewing method.",
    bullets: [
      "Lighter roasts usually preserve more origin character and perceived acidity.",
      "Medium roasts often balance sweetness, body, and origin clarity.",
      "Darker roasts usually feel heavier, more bitter, and less origin-distinct.",
      "Roast preference is not just taste; it also depends on brew method and drink style."
    ],
    keywords: ["roast", "roast level", "light roast", "dark roast", "medium roast"]
  }
];
