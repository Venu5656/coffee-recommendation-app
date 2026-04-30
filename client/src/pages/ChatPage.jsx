import { useState } from "react";
import { Link } from "react-router-dom";
import { apiRequest } from "../lib/api.js";

export function ChatPage({ history, setLastResult, addHistory, token, refreshHistory }) {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Describe how you feel or what kind of coffee situation you are in, and I will translate it into a recommendation."
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
    setMessages((current) => [...current, userMessage]);
    setLoading(true);
    try {
      const result = await apiRequest("/api/chat", {
        method: "POST",
        token,
        body: JSON.stringify({ message: input, history })
      });
      const payload = { ...result.recommendation, source: "chat", chatReply: result.reply };
      setMessages((current) => [...current, { role: "assistant", content: result.reply }]);
      setLatest(payload);
      setLastResult(payload);
      if (token) {
        await refreshHistory();
      } else {
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
        <p className="eyebrow">Latest Chat Recommendation</p>
        {latest?.drink ? (
          <>
            <h2>{latest.drink.name}</h2>
            <p>{latest.chatReply}</p>
            <Link className="secondary-button" to="/result">Open detailed result</Link>
          </>
        ) : (
          <p>Your latest conversational recommendation will appear here.</p>
        )}
      </section>
    </div>
  );
}
