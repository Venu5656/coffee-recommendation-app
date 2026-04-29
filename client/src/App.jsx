import { Route, Routes } from "react-router-dom";
import { Layout } from "./components/Layout.jsx";
import { HomePage } from "./pages/HomePage.jsx";
import { RecommendationPage } from "./pages/RecommendationPage.jsx";
import { ChatPage } from "./pages/ChatPage.jsx";
import { ResultPage } from "./pages/ResultPage.jsx";
import { HistoryPage } from "./pages/HistoryPage.jsx";
import { InsightsPage } from "./pages/InsightsPage.jsx";
import { useLocalStorage } from "./hooks/useLocalStorage.js";

export default function App() {
  const [history, setHistory] = useLocalStorage("coffee-history", []);
  const [lastResult, setLastResult] = useLocalStorage("coffee-last-result", null);

  function addHistory(entry) {
    setHistory((current) => [...current, entry]);
  }

  function addFeedback(feedback, recommendation) {
    setHistory((current) => [
      ...current,
      {
        type: "feedback",
        recommendation,
        feedback,
        timestamp: new Date().toISOString()
      }
    ]);
  }

  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<HomePage />} />
        <Route
          path="/recommend"
          element={
            <RecommendationPage
              history={history}
              setLastResult={setLastResult}
              addHistory={addHistory}
            />
          }
        />
        <Route
          path="/chat"
          element={<ChatPage history={history} setLastResult={setLastResult} addHistory={addHistory} />}
        />
        <Route
          path="/result"
          element={<ResultPage lastResult={lastResult} addFeedback={addFeedback} />}
        />
        <Route path="/history" element={<HistoryPage history={history} />} />
        <Route path="/insights" element={<InsightsPage />} />
      </Route>
    </Routes>
  );
}
