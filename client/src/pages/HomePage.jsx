import { Link } from "react-router-dom";

export function HomePage({ user }) {
  return (
    <div className="home-grid">
      <section className="panel feature-panel">
        <p className="eyebrow">Project Overview</p>
        <h2>Turn midterm coffee insights into an interactive recommendation experience.</h2>
        <p>
          This temporary interface combines rule-based recommendations, an AI chat workflow,
          controlled exploration, and visual composition breakdowns. Your later custom home page
          can replace this entry view without changing the backend or recommendation logic.
        </p>
        <div className="cta-row">
          <Link className="primary-button" to="/recommend">Start with Filters</Link>
          <Link className="secondary-button" to="/chat">Ask the AI Barista</Link>
          {!user ? <Link className="secondary-button" to="/account">Create Account</Link> : null}
        </div>
      </section>
      <section className="panel">
        <p className="eyebrow">What This App Includes</p>
        <ul className="feature-list">
          <li>Filter-based recommendation with reasoning</li>
          <li>Exploration mode to avoid repetitive choices</li>
          <li>Conversational AI recommendations with follow-ups</li>
          <li>Beaker-style ingredient visualization</li>
          <li>Local history and feedback tracking</li>
          <li>Separate insight cards from your prior analysis</li>
        </ul>
      </section>
    </div>
  );
}
