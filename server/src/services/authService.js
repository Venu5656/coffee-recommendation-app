import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import { createId, query } from "../db.js";

const JWT_SECRET = process.env.JWT_SECRET || "development-only-secret";
const TOKEN_EXPIRY = "7d";

function sanitizeUser(row) {
  if (!row) {
    return null;
  }

  return {
    id: row.id,
    name: row.name,
    email: row.email,
    createdAt: row.created_at
  };
}

function signToken(user) {
  return jwt.sign(
    {
      sub: user.id,
      email: user.email,
      name: user.name
    },
    JWT_SECRET,
    { expiresIn: TOKEN_EXPIRY }
  );
}

export function verifyToken(token) {
  return jwt.verify(token, JWT_SECRET);
}

export async function findUserById(id) {
  const result = await query(
    `
      SELECT id, name, email, created_at
      FROM users
      WHERE id = $1
    `,
    [id]
  );

  return sanitizeUser(result.rows[0]);
}

export async function registerUser({ name, email, password }) {
  const normalizedEmail = email.trim().toLowerCase();
  const existing = await query("SELECT id FROM users WHERE email = $1", [normalizedEmail]);

  if (existing.rowCount > 0) {
    throw new Error("An account with that email already exists.");
  }

  const passwordHash = await bcrypt.hash(password, 10);
  const id = createId();

  const result = await query(
    `
      INSERT INTO users (id, name, email, password_hash)
      VALUES ($1, $2, $3, $4)
      RETURNING id, name, email, created_at
    `,
    [id, name.trim(), normalizedEmail, passwordHash]
  );

  const user = sanitizeUser(result.rows[0]);

  return {
    user,
    token: signToken(user)
  };
}

export async function loginUser({ email, password }) {
  const normalizedEmail = email.trim().toLowerCase();
  const result = await query(
    `
      SELECT id, name, email, password_hash, created_at
      FROM users
      WHERE email = $1
    `,
    [normalizedEmail]
  );

  const row = result.rows[0];
  if (!row) {
    throw new Error("Invalid email or password.");
  }

  const passwordMatches = await bcrypt.compare(password, row.password_hash);
  if (!passwordMatches) {
    throw new Error("Invalid email or password.");
  }

  const user = sanitizeUser(row);

  return {
    user,
    token: signToken(user)
  };
}
