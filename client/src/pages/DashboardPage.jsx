import { useMemo, useState } from "react";
import { DrinkImageCard } from "../components/DrinkImageCard.jsx";

const timeOptions = ["morning", "afternoon", "night"];
const moodOptions = ["tired", "relaxed", "energetic"];

function EmptyState({ message }) {
  return <p className="subtle-note">{message}</p>;
}

function DashboardList({ items, emptyMessage }) {
  if (!items?.length) {
    return <EmptyState message={emptyMessage} />;
  }

  return (
    <div className="dashboard-drink-gallery">
      {items.map((item) => (
        <DrinkImageCard key={item.label} name={item.label} count={item.count} />
      ))}
    </div>
  );
}

export function DashboardPage({ dashboard, user }) {
  const [selectedTime, setSelectedTime] = useState("morning");
  const [selectedMood, setSelectedMood] = useState("relaxed");

  const timeDrinks = useMemo(
    () => dashboard?.timeLeaders?.[selectedTime] || [],
    [dashboard, selectedTime]
  );
  const moodDrinks = useMemo(
    () => dashboard?.moodLeaders?.[selectedMood] || [],
    [dashboard, selectedMood]
  );

  if (!dashboard) {
    return (
      <section className="panel">
        <p className="eyebrow">Dashboard</p>
        <h2>Loading your coffee dashboard...</h2>
      </section>
    );
  }

  return (
    <div className="insights-layout">
      <section className="panel dashboard-passport">
        <div className="panel-header">
          <div>
            <p className="eyebrow">Coffee Passport</p>
            <h2>{dashboard.passport.archetype}</h2>
            <p className="lead">{dashboard.passport.headline}</p>
          </div>
          <div className="passport-badge">
            <span>{dashboard.passport.explorationLabel}</span>
            <strong>{user?.name || dashboard.passport.userName}</strong>
          </div>
        </div>
        <div className="insight-metric-grid">
          <article className="insight-metric-card">
            <span>Favorite style</span>
            <strong>{dashboard.passport.favoriteStyle}</strong>
            <p>Most repeated profile in your stored coffee history.</p>
          </article>
          <article className="insight-metric-card">
            <span>Signature time</span>
            <strong>{dashboard.passport.signatureTime}</strong>
            <p>Your recommendations cluster most strongly around this part of the day.</p>
          </article>
          <article className="insight-metric-card">
            <span>Top drink</span>
            <strong>{dashboard.passport.topDrink}</strong>
            <p>The drink your account returns to most often.</p>
          </article>
          <article className="insight-metric-card">
            <span>Likes recorded</span>
            <strong>{dashboard.passport.likedCount}</strong>
            <p>Saved positive reactions used to refine future suggestions.</p>
          </article>
        </div>
      </section>

      <div className="page-grid dashboard-main-grid">
        <section className="panel">
          <p className="eyebrow">Taste Profile</p>
          <h2>Your coffee identity at a glance</h2>
          <div className="dashboard-profile-grid">
            <article className="profile-pill-card">
              <span>Caffeine band</span>
              <strong>{dashboard.tasteProfile.preferredCaffeine}</strong>
            </article>
            <article className="profile-pill-card">
              <span>Sweetness tolerance</span>
              <strong>{dashboard.tasteProfile.sweetnessTolerance}</strong>
            </article>
            <article className="profile-pill-card">
              <span>Texture</span>
              <strong>{dashboard.tasteProfile.favoriteTexture}</strong>
            </article>
            <article className="profile-pill-card">
              <span>Drink style</span>
              <strong>{dashboard.tasteProfile.favoriteStyle}</strong>
            </article>
            <article className="profile-pill-card">
              <span>Flavor direction</span>
              <strong>{dashboard.tasteProfile.dominantTaste}</strong>
            </article>
            <article className="profile-pill-card">
              <span>Peak coffee time</span>
              <strong>{dashboard.tasteProfile.signatureTime}</strong>
            </article>
          </div>
        </section>

        <section className="panel">
          <p className="eyebrow">Exploration Score</p>
          <h2>How far you usually step outside your comfort zone</h2>
          <div className="exploration-meter">
            <div className="exploration-track">
              <div
                className="exploration-fill"
                style={{ width: `${dashboard.exploration.explorationShare}%` }}
              />
            </div>
            <div className="exploration-stats">
              <article className="profile-pill-card">
                <span>Explorer type</span>
                <strong>{dashboard.exploration.label}</strong>
              </article>
              <article className="profile-pill-card">
                <span>Familiar picks</span>
                <strong>{dashboard.exploration.familiarShare}%</strong>
              </article>
              <article className="profile-pill-card">
                <span>Exploration picks</span>
                <strong>{dashboard.exploration.explorationShare}%</strong>
              </article>
            </div>
          </div>
        </section>
      </div>

      <section className="panel">
        <p className="eyebrow">Live Evaluation</p>
        <h2>How the adaptive model is performing on your account</h2>
        <div className="insight-metric-grid">
          <article className="insight-metric-card">
            <span>Recommendations logged</span>
            <strong>{dashboard.evaluationMetrics.totalRecommendations}</strong>
            <p>Used as the training stream for personalization.</p>
          </article>
          <article className="insight-metric-card">
            <span>Like rate</span>
            <strong>{Math.round(dashboard.evaluationMetrics.likeRate * 100)}%</strong>
            <p>Positive feedback share across rated recommendations.</p>
          </article>
          <article className="insight-metric-card">
            <span>Exploration success</span>
            <strong>{Math.round(dashboard.evaluationMetrics.explorationSuccessRate * 100)}%</strong>
            <p>How often exploratory picks later converted into likes.</p>
          </article>
          <article className="insight-metric-card">
            <span>Adaptation readiness</span>
            <strong>{dashboard.evaluationMetrics.adaptationReadiness}</strong>
            <p>Confidence band for how strongly the model should trust your history.</p>
          </article>
        </div>
      </section>

      <div className="page-grid dashboard-main-grid">
        <section className="panel">
          <p className="eyebrow">Drinking Rhythm</p>
          <h2>Liked drinks by time of day</h2>
          <div className="chart-tabs">
            {timeOptions.map((option) => (
              <button
                key={option}
                className={selectedTime === option ? "legend-chip active" : "legend-chip"}
                onClick={() => setSelectedTime(option)}
                type="button"
              >
                {option}
              </button>
            ))}
          </div>
          <DashboardList
            items={timeDrinks}
            emptyMessage="Not enough liked history for this time yet. Keep rating drinks to train this view."
          />
        </section>

        <section className="panel">
          <p className="eyebrow">Mood Match</p>
          <h2>Best choices from the moods you have already lived through</h2>
          <div className="chart-tabs">
            {moodOptions.map((option) => (
              <button
                key={option}
                className={selectedMood === option ? "legend-chip active" : "legend-chip"}
                onClick={() => setSelectedMood(option)}
                type="button"
              >
                {option}
              </button>
            ))}
          </div>
          <DashboardList
            items={moodDrinks}
            emptyMessage="No strong mood-specific history here yet. More sessions will make this sharper."
          />
        </section>
      </div>

      <div className="page-grid dashboard-main-grid">
        <section className="panel">
          <p className="eyebrow">Top Drinks</p>
          <h2>Your most repeated drinks so far</h2>
          <DashboardList
            items={dashboard.topDrinks}
            emptyMessage="Your top drinks will appear once you start building history."
          />
        </section>

        <section className="panel">
          <p className="eyebrow">Habit Insights</p>
          <h2>What your coffee behavior is saying</h2>
          <div className="timeline">
            {dashboard.habitInsights.map((insight) => (
              <article key={insight} className="timeline-card">
                <span className="timeline-era">Pattern</span>
                <p>{insight}</p>
              </article>
            ))}
          </div>
        </section>
      </div>

      <section className="panel">
        <p className="eyebrow">History Timeline</p>
        <h2>Recent recommendation and feedback activity</h2>
        {dashboard.timeline.length ? (
          <div className="timeline">
            {dashboard.timeline.map((item) => (
              <article key={`${item.timestamp}-${item.recommendation}`} className="timeline-card">
                <span className="timeline-era">{item.type}</span>
                <strong>{item.recommendation}</strong>
                <small>{new Date(item.timestamp).toLocaleString()}</small>
                <p>{item.detail}</p>
              </article>
            ))}
          </div>
        ) : (
          <EmptyState message="No saved dashboard timeline yet. Start using recommendations and feedback first." />
        )}
      </section>

      {!dashboard.hasEnoughData ? (
        <section className="panel insight-footnote">
          <p className="eyebrow">Still Learning</p>
          <h2>Your passport is being built</h2>
          <p>
            This dashboard becomes much sharper after a few recommendations and a couple of likes or
            dislikes. Right now it is showing the first detectable patterns, not a finished profile.
          </p>
        </section>
      ) : null}
    </div>
  );
}
