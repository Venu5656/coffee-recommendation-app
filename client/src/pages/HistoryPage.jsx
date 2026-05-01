export function HistoryPage({ history, user }) {
  const ordered = user ? history : [...history].reverse();

  return (
    <section className="panel">
      <p className="eyebrow">Personalization History</p>
      <h2>Recent selections and feedback</h2>
      <p className="subtle-note">
        {user
          ? "This is the raw event stream behind your dashboard and personalized recommendations."
          : "You are viewing guest history stored only in this browser. The dashboard uses this local data too."}
      </p>
      {ordered.length ? (
        <div className="history-list">
          {ordered.map((entry, index) => (
            <article key={`${entry.timestamp}-${index}`} className="history-item">
              <strong>{entry.recommendation}</strong>
              <span>{entry.type}</span>
              <p>
                {entry.feedback
                  ? `Feedback: ${entry.feedback}`
                  : entry.prompt || JSON.stringify(entry.preferences)}
              </p>
            </article>
          ))}
        </div>
      ) : (
        <p>No history yet. Recommendations and feedback will appear here.</p>
      )}
    </section>
  );
}
