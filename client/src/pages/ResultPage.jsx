import { BeakerGraph } from "../components/BeakerGraph.jsx";
import { RecommendationCard } from "../components/RecommendationCard.jsx";

export function ResultPage({ lastResult, addFeedback }) {
  return (
    <div className="page-grid result-layout">
      <RecommendationCard result={lastResult} onFeedback={addFeedback} />
      <section className="panel">
        <p className="eyebrow">Beaker Visualization</p>
        <h2>Drink composition</h2>
        {lastResult?.drink ? (
          <BeakerGraph composition={lastResult.drink.composition} />
        ) : (
          <p>No recommendation yet. Use the filter or chat flow first.</p>
        )}
      </section>
    </div>
  );
}
