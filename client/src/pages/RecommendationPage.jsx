import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { apiRequest } from "../lib/api.js";

const initialForm = {
  mood: "tired",
  taste: "smooth",
  time: "morning",
  temperature: "hot",
  effort: "quick",
  caffeinePreference: "medium",
  sweetnessPreference: "lightly-sweet",
  texturePreference: "creamy",
  drinkStyle: "milky",
  trySomethingNew: false
};

const fieldLabels = {
  mood: "Mood",
  taste: "Taste",
  time: "Time",
  temperature: "Temperature",
  effort: "Effort",
  caffeinePreference: "Caffeine",
  sweetnessPreference: "Sweetness",
  texturePreference: "Texture",
  drinkStyle: "Drink Style"
};

export function RecommendationPage({ history, setLastResult, addHistory, token, refreshHistory }) {
  const [form, setForm] = useState(initialForm);
  const [options, setOptions] = useState(null);
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    apiRequest("/api/profiles")
      .then((data) => setOptions(data.filterOptions));
  }, []);

  async function handleSubmit(event) {
    event.preventDefault();
    setLoading(true);
    try {
      const result = await apiRequest("/api/recommend", {
        method: "POST",
        token,
        body: JSON.stringify({ preferences: form, history })
      });
      const payload = { ...result, source: "filters" };
      setLastResult(payload);
      if (token) {
        await refreshHistory();
      } else {
        addHistory({
          type: "filter",
          preferences: form,
          recommendation: result.drink.name,
          explorationUsed: result.explorationUsed,
          timestamp: new Date().toISOString()
        });
      }
      navigate("/result");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="page-grid">
      <section className="panel">
        <p className="eyebrow">Filter Recommendation</p>
        <h2>Build a coffee suggestion from structured inputs.</h2>
        <form className="form-grid" onSubmit={handleSubmit}>
          {options
            ? Object.entries(options).map(([key, values]) => (
                <label key={key}>
                  <span>{fieldLabels[key] || key}</span>
                  <select
                    value={form[key]}
                    onChange={(event) => {
                      setForm((current) => ({ ...current, [key]: event.target.value }));
                    }}
                  >
                    {values.map((value) => (
                      <option key={value} value={value}>{value}</option>
                    ))}
                  </select>
                </label>
              ))
            : null}
          <label className="checkbox-row">
            <input
              type="checkbox"
              checked={form.trySomethingNew}
              onChange={(event) =>
                setForm((current) => ({ ...current, trySomethingNew: event.target.checked }))
              }
            />
            <span>Try something new</span>
          </label>
          <button className="primary-button" type="submit" disabled={loading}>
            {loading ? "Brewing..." : "Get Recommendation"}
          </button>
        </form>
      </section>
      <section className="panel">
        <p className="eyebrow">Exploration Logic</p>
        <h2>How variety is introduced</h2>
        <p>
          Recommendations still favor your main preferences, but exploration can claim roughly
          20-30% of the decision space when you ask for novelty or when history becomes repetitive.
        </p>
      </section>
    </div>
  );
}
