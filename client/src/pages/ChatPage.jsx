import { useState } from "react";
import { Link } from "react-router-dom";
import { apiRequest } from "../lib/api.js";
import { RecommendationCard } from "../components/RecommendationCard.jsx";
import { BeakerGraph } from "../components/BeakerGraph.jsx";

function GuideBlock({ guide }) {
  if (!guide) {
    return null;
  }

  return (
    <div className="subtle-block">
      <strong>{guide.title}</strong>
      <p><strong>Equipment:</strong> {guide.equipment.join(", ")}</p>
      <p><strong>Ingredients:</strong> {guide.ingredients.join(", ")}</p>
      <ol className="feature-list">
        {guide.steps.map((step) => (
          <li key={step}>{step}</li>
        ))}
      </ol>
      <p><strong>Tips:</strong> {guide.tips.join(" ")}</p>
    </div>
  );
}

function KnowledgeBlock({ knowledge }) {
  if (!knowledge) {
    return null;
  }

  return (
    <div className="subtle-block">
      <strong>{knowledge.title}</strong>
      <p>{knowledge.summary}</p>
      <ul className="feature-list">
        {knowledge.bullets.map((bullet) => (
          <li key={bullet}>{bullet}</li>
        ))}
      </ul>
    </div>
  );
}

export function ChatPage({ history, setLastResult, addHistory, addFeedback, token, refreshHistory }) {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Ask for a coffee recommendation, an off-menu drink, brewing help, or coffee knowledge. I can act like an experienced barista, not just a menu picker."
    }
  ]);
  const [loading, setLoading] = useState(false);
  const [latest, setLatest] = useState(null);

  async function sendMessage(event) {
    event.preventDefault();
    if (!input.trim()) {
      return;
    }

    const userMessage = { role: "user", content: input };
    const nextMessages = [...messages, userMessage];
    setMessages(nextMessages);
    setLoading(true);
    try {
      const result = await apiRequest("/api/chat", {
        method: "POST",
        token,
        body: JSON.stringify({ message: input, history, messages: nextMessages })
      });
      setMessages((current) => [...current, { role: "assistant", content: result.reply }]);
      setLatest(result);

      if (result.mode === "profile_recommendation" && result.recommendation?.drink) {
        const payload = { ...result.recommendation, source: "chat", chatReply: result.reply };
        setLastResult(payload);
      }

      if (token) {
        await refreshHistory();
      } else if (result.recommendation?.drink?.name) {
        addHistory({
          type: "chat",
          prompt: input,
          recommendation: result.recommendation.drink.name,
          extractedPreferences: result.extractedPreferences,
          timestamp: new Date().toISOString()
        });
      }

      setInput("");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="page-grid chat-layout">
      <section className="panel">
        <p className="eyebrow">AI Chat</p>
        <div className="chat-window">
          {messages.map((message, index) => (
            <div key={`${message.role}-${index}`} className={`chat-bubble ${message.role}`}>
              {message.content}
            </div>
          ))}
        </div>
        <form className="chat-form" onSubmit={sendMessage}>
          <textarea
            rows="4"
            placeholder="I'm tired but want something comforting and not too strong."
            value={input}
            onChange={(event) => setInput(event.target.value)}
          />
          <button className="primary-button" type="submit" disabled={loading}>
            {loading ? "Thinking..." : "Ask the AI Barista"}
          </button>
        </form>
      </section>
      <section className="panel">
        <p className="eyebrow">Latest Barista Response</p>
        {latest ? (
          <>
            {latest.assistantEngine === "local-barista" ? (
              <p className="subtle-note">
                Powered by the app&apos;s local coffee assistant, using the recommendation engine and coffee knowledge base.
              </p>
            ) : null}
            {latest.mode === "profile_recommendation" && latest.recommendation?.drink ? (
              <div className="chat-result-stack">
                <RecommendationCard result={latest.recommendation} onFeedback={addFeedback} />
                <section className="panel panel-nested">
                  <p className="eyebrow">Beaker Visualization</p>
                  <h2>Drink composition</h2>
                  <BeakerGraph composition={latest.recommendation.drink.composition} />
                  <Link className="secondary-button" to="/result">Open full result page</Link>
                </section>
              </div>
            ) : null}
            {latest.mode !== "profile_recommendation" ? (
              <>
                <h2>
                  {latest.mode === "custom_recommendation"
                    ? latest.customDrink?.name
                    : latest.mode === "brew_guide"
                      ? latest.guide?.title
                      : latest.knowledge?.title || "Coffee Knowledge"}
                </h2>
                <p>{latest.reply}</p>
              </>
            ) : null}
            {latest.mode === "custom_recommendation" && latest.customDrink ? (
              <div className="subtle-block">
                <strong>{latest.customDrink.name}</strong>
                <p>{latest.customDrink.description}</p>
              </div>
            ) : null}
            <GuideBlock guide={latest.guide} />
            <KnowledgeBlock knowledge={latest.knowledge} />
          </>
        ) : (
          <p>Your latest recommendation, brew guide, or coffee explanation will appear here.</p>
        )}
      </section>
    </div>
  );
}
