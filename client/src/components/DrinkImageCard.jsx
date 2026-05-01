import { coffeeProfiles } from "@coffee/shared/coffeeProfiles";

const compositionColors = {
  coffee: "#4b2e1f",
  milk: "#ead9bb",
  foam: "#fffaf0",
  sugar: "#d6a15e",
  water: "#9ecae1",
  chocolate: "#6d3f2a"
};

const profileByName = Object.fromEntries(coffeeProfiles.map((profile) => [profile.name, profile]));

export function DrinkImageCard({ name, count }) {
  const profile = profileByName[name];
  const segments = Object.entries(profile?.composition || {}).filter(([, value]) => value > 0);

  return (
    <article className="drink-visual-card">
      <div className="drink-visual-stage">
        <svg viewBox="0 0 220 220" className="drink-visual-svg" role="img" aria-label={name}>
          <defs>
            <linearGradient id={`drink-bg-${profile?.id || name}`} x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#fff6e8" />
              <stop offset="100%" stopColor="#ecd7b4" />
            </linearGradient>
          </defs>
          <rect x="0" y="0" width="220" height="220" rx="30" fill={`url(#drink-bg-${profile?.id || name})`} />
          <ellipse cx="110" cy="176" rx="58" ry="14" fill="rgba(77, 52, 34, 0.12)" />
          <path
            d="M62 55 C62 45, 74 38, 90 38 H130 C146 38, 158 45, 158 55 V160 C158 171, 148 180, 136 180 H84 C72 180, 62 171, 62 160 Z"
            fill="#fef8ef"
            stroke="#6e4930"
            strokeWidth="5"
          />
          <path
            d="M158 68 H174 C184 68, 192 76, 192 88 V102 C192 114, 184 122, 174 122 H158"
            fill="none"
            stroke="#6e4930"
            strokeWidth="5"
            strokeLinecap="round"
          />
          <clipPath id={`drink-fill-${profile?.id || name}`}>
            <path d="M68 55 H152 V160 C152 168, 145 174, 136 174 H84 C75 174, 68 168, 68 160 Z" />
          </clipPath>
          <g clipPath={`url(#drink-fill-${profile?.id || name})`}>
            {segments.reduceRight(
              (accumulator, [ingredient, value]) => {
                const nextY = accumulator.y - value;
                accumulator.elements.push(
                  <rect
                    key={ingredient}
                    x="68"
                    y={nextY}
                    width="84"
                    height={value}
                    fill={compositionColors[ingredient]}
                  />
                );
                return { y: nextY, elements: accumulator.elements };
              },
              { y: 174, elements: [] }
            ).elements}
          </g>
          <ellipse cx="110" cy="55" rx="42" ry="9" fill="rgba(255,255,255,0.6)" />
          <text x="110" y="202" textAnchor="middle" className="drink-visual-label">
            {name}
          </text>
        </svg>
      </div>
      <div className="drink-visual-meta">
        <strong>{name}</strong>
        <span>{count} strong matches</span>
      </div>
    </article>
  );
}
