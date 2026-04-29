const colors = {
  coffee: "#4b2e1f",
  milk: "#e9d8b6",
  foam: "#fffdf6",
  sugar: "#d6a55d",
  water: "#8ecae6",
  chocolate: "#6b3f2b"
};

export function BeakerGraph({ composition }) {
  const segments = Object.entries(composition || {}).filter(([, value]) => value > 0);

  return (
    <div className="beaker-card">
      <div className="beaker">
        {segments.map(([name, value]) => (
          <div
            key={name}
            className="beaker-segment"
            style={{
              height: `${value}%`,
              background: colors[name]
            }}
            title={`${name}: ${value}%`}
          />
        ))}
      </div>
      <div className="legend">
        {segments.map(([name, value]) => (
          <div key={name} className="legend-item">
            <span className="swatch" style={{ background: colors[name] }} />
            <span>{name}</span>
            <strong>{value}%</strong>
          </div>
        ))}
      </div>
    </div>
  );
}
