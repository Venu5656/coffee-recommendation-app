import { NavLink, Outlet } from "react-router-dom";

const navItems = [
  ["Home", "/"],
  ["Dashboard", "/dashboard"],
  ["Account", "/account"],
  ["Recommend", "/recommend"],
  ["AI Chat", "/chat"],
  ["Result", "/result"],
  ["History", "/history"],
  ["Did You Know?", "/insights"]
];

export function Layout({ user, onLogout }) {
  return (
    <div className="app-shell">
      <header className="hero-bar">
        <div>
          <p className="eyebrow">Coffee Recommendation System</p>
          <h1>Data-backed discovery with rule-based and conversational guidance.</h1>
          <p className="subtle-note">
            {user
              ? `Signed in as ${user.name}. Recommendations now sync to the database.`
              : "Guest mode is active. Sign in to back up history and feedback in the database."}
          </p>
        </div>
        <nav className="nav-tabs">
          {navItems.map(([label, to]) => (
            <NavLink
              key={to}
              to={to}
              className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}
            >
              {label}
            </NavLink>
          ))}
          {user ? (
            <button className="secondary-button" onClick={onLogout} type="button">
              Sign Out
            </button>
          ) : null}
        </nav>
      </header>
      <main className="page-shell">
        <Outlet />
      </main>
    </div>
  );
}
