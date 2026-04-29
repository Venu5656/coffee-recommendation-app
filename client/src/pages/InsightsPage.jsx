import { useEffect, useState } from "react";

export function InsightsPage() {
  const [insights, setInsights] = useState([]);

  useEffect(() => {
    fetch("/api/insights")
      .then((response) => response.json())
      .then((data) => setInsights(data.insights));
  }, []);

  return (
    <section className="panel">
      <p className="eyebrow">Did You Know?</p>
      <h2>Insights carried forward from the earlier country-level analysis</h2>
      <div className="insight-grid">
        {insights.map((insight) => (
          <article key={insight.title} className="insight-card">
            <h3>{insight.title}</h3>
            <p>{insight.body}</p>
          </article>
        ))}
      </div>
      <p className="subtle-note">
        These insight cards are intentionally separate from recommendation logic.
      </p>
    </section>
  );
}
