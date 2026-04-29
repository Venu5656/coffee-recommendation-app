import { NavLink, Outlet } from "react-router-dom";

const navItems = [
  ["Home", "/"],
  ["Recommend", "/recommend"],
  ["AI Chat", "/chat"],
  ["Result", "/result"],
  ["History", "/history"],
  ["Did You Know?", "/insights"]
];

export function Layout() {
  return (
    <div className="app-shell">
      <header className="hero-bar">
        <div>
          <p className="eyebrow">Coffee Recommendation System</p>
          <h1>Data-backed discovery with rule-based and conversational guidance.</h1>
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
        </nav>
      </header>
      <main className="page-shell">
        <Outlet />
      </main>
    </div>
  );
}
