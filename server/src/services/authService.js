import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { createId, query } from "../db.js";

const JWT_SECRET = process.env.JWT_SECRET || "development-only-secret";
const TOKEN_EXPIRY = "7d";

// In-memory fallback store used when PostgreSQL is unavailable
const _memUsers = new Map();

function isDbError(err) {
  return err?.code === "ENOENT" || err?.code === "ECONNREFUSED" ||
    err?.message?.includes("ENOENT") || err?.message?.includes("connect");
}

function sanitizeUser(row) {
  if (!row) return null;
  return { id: row.id, name: row.name, email: row.email, createdAt: row.created_at || row.createdAt };
}

function signToken(user) {
  return jwt.sign({ sub: user.id, email: user.email, name: user.name }, JWT_SECRET, { expiresIn: TOKEN_EXPIRY });
}

export function verifyToken(token) {
  return jwt.verify(token, JWT_SECRET);
}

export async function findUserById(id) {
  try {
    const result = await query(`SELECT id, name, email, created_at FROM users WHERE id = $1`, [id]);
    return sanitizeUser(result.rows[0]);
  } catch (err) {
    if (isDbError(err)) {
      const u = _memUsers.get(id);
      return u ? sanitizeUser(u) : null;
    }
    throw err;
  }
}

export async function registerUser({ name, email, password }) {
  const normalizedEmail = email.trim().toLowerCase();

  try {
    const existing = await query("SELECT id FROM users WHERE email = $1", [normalizedEmail]);
    if (existing.rowCount > 0) throw new Error("An account with that email already exists.");

    const passwordHash = await bcrypt.hash(password, 10);
    const id = createId();
    const result = await query(
      `INSERT INTO users (id, name, email, password_hash) VALUES ($1, $2, $3, $4) RETURNING id, name, email, created_at`,
      [id, name.trim(), normalizedEmail, passwordHash]
    );
    const user = sanitizeUser(result.rows[0]);
    return { user, token: signToken(user) };
  } catch (err) {
    if (!isDbError(err)) throw err;

    // DB unavailable — use in-memory store
    for (const u of _memUsers.values()) {
      if (u.email === normalizedEmail) throw new Error("An account with that email already exists.");
    }
    const passwordHash = await bcrypt.hash(password, 10);
    const id = createId();
    const user = { id, name: name.trim(), email: normalizedEmail, createdAt: new Date().toISOString() };
    _memUsers.set(id, { ...user, password_hash: passwordHash });
    return { user, token: signToken(user) };
  }
}

export async function loginUser({ email, password }) {
  const normalizedEmail = email.trim().toLowerCase();

  try {
    const result = await query(
      `SELECT id, name, email, password_hash, created_at FROM users WHERE email = $1`,
      [normalizedEmail]
    );
    const row = result.rows[0];
    if (!row) throw new Error("Invalid email or password.");
    const passwordMatches = await bcrypt.compare(password, row.password_hash);
    if (!passwordMatches) throw new Error("Invalid email or password.");
    const user = sanitizeUser(row);
    return { user, token: signToken(user) };
  } catch (err) {
    if (!isDbError(err)) throw err;

    // DB unavailable — use in-memory store
    let found = null;
    for (const u of _memUsers.values()) {
      if (u.email === normalizedEmail) { found = u; break; }
    }
    if (!found) throw new Error("Invalid email or password.");
    const passwordMatches = await bcrypt.compare(password, found.password_hash);
    if (!passwordMatches) throw new Error("Invalid email or password.");
    const user = sanitizeUser(found);
    return { user, token: signToken(user) };
  }
}
