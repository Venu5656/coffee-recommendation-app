import { useState } from "react";

const initialLogin = { email: "", password: "" };
const initialRegister = { name: "", email: "", password: "" };

export function AuthPage({ onAuthenticate, authLoading, user }) {
  const [mode, setMode] = useState("login");
  const [loginForm, setLoginForm] = useState(initialLogin);
  const [registerForm, setRegisterForm] = useState(initialRegister);
  const [error, setError] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");

    const path = mode === "login" ? "/api/auth/login" : "/api/auth/register";
    const body = mode === "login" ? loginForm : registerForm;

    try {
      await onAuthenticate(path, body);
    } catch (submitError) {
      setError(submitError.message);
    }
  }

  if (user) {
    return (
      <section className="panel">
        <p className="eyebrow">Account</p>
        <h2>You are signed in as {user.name}.</h2>
        <p>
          Your recommendation history and feedback are now stored in PostgreSQL instead of staying
          only in local browser storage.
        </p>
      </section>
    );
  }

  return (
    <div className="page-grid">
      <section className="panel">
        <p className="eyebrow">Authentication</p>
        <h2>Create an account or sign in to sync your coffee history.</h2>
        <div className="mode-switch">
          <button
            className={mode === "login" ? "nav-link active" : "nav-link"}
            onClick={() => setMode("login")}
            type="button"
          >
            Login
          </button>
          <button
            className={mode === "register" ? "nav-link active" : "nav-link"}
            onClick={() => setMode("register")}
            type="button"
          >
            Register
          </button>
        </div>
        <form className="form-grid" onSubmit={handleSubmit}>
          {mode === "register" ? (
            <label>
              <span>Name</span>
              <input
                value={registerForm.name}
                onChange={(event) =>
                  setRegisterForm((current) => ({ ...current, name: event.target.value }))
                }
              />
            </label>
          ) : null}
          <label>
            <span>Email</span>
            <input
              type="email"
              value={mode === "login" ? loginForm.email : registerForm.email}
              onChange={(event) => {
                const value = event.target.value;
                if (mode === "login") {
                  setLoginForm((current) => ({ ...current, email: value }));
                } else {
                  setRegisterForm((current) => ({ ...current, email: value }));
                }
              }}
            />
          </label>
          <label>
            <span>Password</span>
            <input
              type="password"
              value={mode === "login" ? loginForm.password : registerForm.password}
              onChange={(event) => {
                const value = event.target.value;
                if (mode === "login") {
                  setLoginForm((current) => ({ ...current, password: value }));
                } else {
                  setRegisterForm((current) => ({ ...current, password: value }));
                }
              }}
            />
          </label>
          {error ? <p className="error-text">{error}</p> : null}
          <button className="primary-button" disabled={authLoading} type="submit">
            {authLoading ? "Processing..." : mode === "login" ? "Login" : "Create Account"}
          </button>
        </form>
      </section>
      <section className="panel">
        <p className="eyebrow">Why Sign In?</p>
        <ul className="feature-list">
          <li>Your likes and dislikes persist across devices</li>
          <li>Recommendation history becomes database-backed instead of browser-only</li>
          <li>PostgreSQL makes later backup and deployment much safer than local storage alone</li>
        </ul>
      </section>
    </div>
  );
}
