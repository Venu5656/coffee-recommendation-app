export const didYouKnowInsights = [
  {
    id: "income-stability",
    title: "Stable habits in high-income countries",
    body: "Coffee consumption stays comparatively steady in higher-income markets, suggesting established rituals rather than volatile swings."
  },
  {
    id: "work-intensity",
    title: "Work intensity is not everything",
    body: "The prior analysis suggested an inverse relationship in several cases, which means busier work environments did not automatically translate into more coffee."
  },
  {
    id: "gdp-signal",
    title: "GDP growth is a weak signal",
    body: "Short-term economic growth had limited explanatory power. Coffee behavior appears more anchored in culture and routine than in macro growth cycles."
  },
  {
    id: "culture-dominance",
    title: "Culture shapes the cup",
    body: "Regional habits, rituals, and local taste traditions were stronger drivers than broad economic indicators."
  }
];

export const insightsDashboard = {
  headline:
    "Coffee behavior looks less like a pure economic reaction and more like a durable cultural habit.",
  spotlightMetrics: [
    {
      label: "High-income stability",
      value: "Low variance",
      detail: "Consumption clusters tightly across mature coffee markets."
    },
    {
      label: "Work intensity effect",
      value: "Mostly inverse",
      detail: "Higher work pressure did not consistently increase consumption."
    },
    {
      label: "GDP growth signal",
      value: "Weak",
      detail: "Macro growth alone was not a strong predictor of coffee demand."
    },
    {
      label: "Culture weight",
      value: "High",
      detail: "Regional norms explained more than broad economic indicators."
    }
  ],
  charts: [
    {
      id: "consumption-trend",
      title: "Consumption Stability by Income Group",
      type: "line",
      narrative:
        "Higher-income groups stay relatively flat over time, while lower-income groups show wider movement. The pattern supports the idea that mature markets settle into repeatable drinking habits.",
      xLabels: ["2019", "2020", "2021", "2022", "2023"],
      series: [
        {
          name: "High income",
          color: "#5c3b22",
          values: [88, 89, 88, 90, 89]
        },
        {
          name: "Upper-middle income",
          color: "#9b6b43",
          values: [71, 69, 73, 74, 72]
        },
        {
          name: "Lower-middle income",
          color: "#d39a56",
          values: [52, 47, 55, 58, 54]
        }
      ]
    },
    {
      id: "work-vs-consumption",
      title: "Work Intensity vs Coffee Consumption",
      type: "scatter",
      narrative:
        "Several country observations land on a slight downward slope. The takeaway is not that work pressure eliminates coffee, but that the relationship is weaker and less intuitive than many people expect.",
      xLabel: "Work intensity index",
      yLabel: "Coffee consumption index",
      points: [
        { label: "Country A", x: 82, y: 54, region: "North" },
        { label: "Country B", x: 74, y: 61, region: "North" },
        { label: "Country C", x: 65, y: 66, region: "West" },
        { label: "Country D", x: 55, y: 76, region: "West" },
        { label: "Country E", x: 47, y: 79, region: "South" },
        { label: "Country F", x: 38, y: 83, region: "South" }
      ]
    },
    {
      id: "drivers",
      title: "Relative Strength of Demand Drivers",
      type: "bar",
      narrative:
        "Culture dominates the explanatory mix. GDP growth remains present but small, while work intensity contributes less consistently and often in the opposite direction.",
      bars: [
        { label: "Cultural norms", value: 91, color: "#5c3b22" },
        { label: "Regional habits", value: 84, color: "#7f5539" },
        { label: "Income level", value: 58, color: "#b08968" },
        { label: "Work intensity", value: 34, color: "#ddb892" },
        { label: "GDP growth", value: 21, color: "#e6ccb2" }
      ]
    }
  ],
  timeline: [
    {
      era: "Origins",
      period: "Early coffee history",
      title: "Coffee emerges as a ritual drink",
      body: "Coffee spread from a regional discovery into a social and spiritual routine, long before it became a global commodity."
    },
    {
      era: "Coffeehouses",
      period: "Urban social era",
      title: "The cafe becomes a public thinking space",
      body: "Coffeehouses helped connect coffee with conversation, work, news, and social exchange."
    },
    {
      era: "Industrial spread",
      period: "Mass adoption",
      title: "Convenience and scale accelerate demand",
      body: "Production, distribution, and faster preparation widened the audience and normalized daily consumption."
    },
    {
      era: "Specialty era",
      period: "Taste-led consumption",
      title: "Consumers start caring about craft and identity",
      body: "Coffee becomes part habit, part self-expression, with more attention on origin, style, and ritual."
    }
  ]
};
