import { Route, Routes } from "react-router-dom";
import { useEffect, useState } from "react";
import { Layout } from "./components/Layout.jsx";
import { HomePage } from "./pages/HomePage.jsx";
import { RecommendationPage } from "./pages/RecommendationPage.jsx";
import { ChatPage } from "./pages/ChatPage.jsx";
import { ResultPage } from "./pages/ResultPage.jsx";
import { HistoryPage } from "./pages/HistoryPage.jsx";
import { InsightsPage } from "./pages/InsightsPage.jsx";
import { AuthPage } from "./pages/AuthPage.jsx";
import { DashboardPage } from "./pages/DashboardPage.jsx";
import { useLocalStorage } from "./hooks/useLocalStorage.js";
import { apiRequest } from "./lib/api.js";
import { deriveDashboardData } from "@coffee/shared/dashboard";

export default function App() {
  const [guestHistory, setGuestHistory] = useLocalStorage("coffee-history", []);
  const [lastResult, setLastResult] = useLocalStorage("coffee-last-result", null);
  const [token, setToken] = useLocalStorage("coffee-auth-token", "");
  const [user, setUser] = useState(null);
  const [remoteHistory, setRemoteHistory] = useState([]);
  const [authLoading, setAuthLoading] = useState(false);
  const [remoteDashboard, setRemoteDashboard] = useState(null);

  const history = token ? remoteHistory : guestHistory;
  const guestDashboard = deriveDashboardData(guestHistory, "Guest");
  const dashboard = token ? remoteDashboard : guestDashboard;

  useEffect(() => {
    if (!token) {
      setUser(null);
      setRemoteHistory([]);
      setRemoteDashboard(null);
      return;
    }

    let cancelled = false;

    async function hydrateSession() {
      setAuthLoading(true);

      try {
        const [{ user: currentUser }, { history: currentHistory }, { dashboard: currentDashboard }] = await Promise.all([
          apiRequest("/api/auth/me", { token }),
          apiRequest("/api/history", { token }),
          apiRequest("/api/dashboard", { token })
        ]);

        if (!cancelled) {
          setUser(currentUser);
          setRemoteHistory(currentHistory);
          setRemoteDashboard(currentDashboard);
        }
      } catch {
        if (!cancelled) {
          setToken("");
          setUser(null);
          setRemoteHistory([]);
          setRemoteDashboard(null);
        }
      } finally {
        if (!cancelled) {
          setAuthLoading(false);
        }
      }
    }

    hydrateSession();

    return () => {
      cancelled = true;
    };
  }, [token, setToken]);

  function addHistory(entry) {
    setGuestHistory((current) => [...current, entry]);
  }

  async function refreshHistory() {
    if (!token) {
      return;
    }

    const [{ history: currentHistory }, { dashboard: currentDashboard }] = await Promise.all([
      apiRequest("/api/history", { token }),
      apiRequest("/api/dashboard", { token })
    ]);
    setRemoteHistory(currentHistory);
    setRemoteDashboard(currentDashboard);
  }

  async function handleAuthenticate(path, body) {
    setAuthLoading(true);

    try {
      const response = await apiRequest(path, {
        method: "POST",
        body: JSON.stringify(body)
      });

      setToken(response.token);
      setUser(response.user);
      const [{ history: currentHistory }, { dashboard: currentDashboard }] = await Promise.all([
        apiRequest("/api/history", { token: response.token }),
        apiRequest("/api/dashboard", { token: response.token })
      ]);
      setRemoteHistory(currentHistory);
      setRemoteDashboard(currentDashboard);
    } finally {
      setAuthLoading(false);
    }
  }

  function handleLogout() {
    setToken("");
    setUser(null);
    setRemoteHistory([]);
    setRemoteDashboard(null);
  }

  async function addFeedback(feedback, recommendation) {
    if (token) {
      await apiRequest("/api/feedback", {
        method: "POST",
        token,
        body: JSON.stringify({ feedback, recommendation })
      });
      await refreshHistory();
      return;
    }

    setGuestHistory((current) => [
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
      <Route element={<Layout user={user} onLogout={handleLogout} />}>
        <Route path="/" element={<HomePage user={user} />} />
        <Route path="/dashboard" element={<DashboardPage dashboard={dashboard} user={user} />} />
        <Route
          path="/account"
          element={
            <AuthPage
              onAuthenticate={handleAuthenticate}
              authLoading={authLoading}
              user={user}
            />
          }
        />
        <Route
          path="/recommend"
          element={
            <RecommendationPage
              history={history}
              setLastResult={setLastResult}
              addHistory={addHistory}
              token={token}
              refreshHistory={refreshHistory}
            />
          }
        />
        <Route
          path="/chat"
          element={
            <ChatPage
              history={history}
              setLastResult={setLastResult}
              addHistory={addHistory}
              addFeedback={addFeedback}
              token={token}
              refreshHistory={refreshHistory}
            />
          }
        />
        <Route
          path="/result"
          element={<ResultPage lastResult={lastResult} addFeedback={addFeedback} />}
        />
        <Route path="/history" element={<HistoryPage history={history} user={user} />} />
        <Route path="/insights" element={<InsightsPage />} />
      </Route>
    </Routes>
  );
}
