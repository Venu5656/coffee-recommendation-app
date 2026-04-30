import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { apiRequest } from "../lib/api.js";

const initialForm = {
  mood: "tired",
  taste: "smooth",
  time: "morning",
  temperature: "hot",
  effort: "quick",
  trySomethingNew: false
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
                  <span>{key.replace(/s$/, "")}</span>
                  <select
                    value={form[key.replace(/s$/, "")] ?? form[key]}
                    onChange={(event) => {
                      const targetKey = key.replace(/s$/, "");
                      setForm((current) => ({ ...current, [targetKey]: event.target.value }));
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
