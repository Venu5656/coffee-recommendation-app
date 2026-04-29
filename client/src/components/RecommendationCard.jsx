export function RecommendationCard({ result, onFeedback }) {
  if (!result?.drink) {
    return null;
  }

  const { drink, reasoning, explorationUsed, alternatives } = result;

  return (
    <section className="panel">
      <div className="panel-header">
        <div>
          <p className="eyebrow">Recommended Drink</p>
          <h2>{drink.name}</h2>
        </div>
        {explorationUsed ? <span className="pill accent">Exploration Mode</span> : null}
      </div>
      <p className="lead">{drink.description}</p>
      <div className="attribute-grid">
        <div className="attribute"><span>Caffeine</span><strong>{drink.caffeineLevel}</strong></div>
        <div className="attribute"><span>Temperature</span><strong>{drink.temperature.join(", ")}</strong></div>
        <div className="attribute"><span>Effort</span><strong>{drink.effort}</strong></div>
        <div className="attribute"><span>Taste</span><strong>{drink.tastes.join(", ")}</strong></div>
      </div>
      <p>{reasoning}</p>
      {alternatives?.length ? (
        <div className="subtle-block">
          <strong>Other strong matches:</strong> {alternatives.map((item) => item.name).join(", ")}
        </div>
      ) : null}
      {onFeedback ? (
        <div className="feedback-row">
          <button className="secondary-button" onClick={() => onFeedback("like", drink.name)}>👍 Like</button>
          <button className="secondary-button" onClick={() => onFeedback("dislike", drink.name)}>👎 Not for me</button>
        </div>
      ) : null}
    </section>
  );
}
