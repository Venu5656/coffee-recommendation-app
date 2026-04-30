export function HistoryPage({ history, user }) {
  const ordered = user ? history : [...history].reverse();

  return (
    <section className="panel">
      <p className="eyebrow">Personalization History</p>
      <h2>Recent selections and feedback</h2>
      <p className="subtle-note">
        {user
          ? "This history is coming from your authenticated database record."
          : "You are viewing guest history stored only in this browser."}
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
