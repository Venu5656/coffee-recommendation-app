import { Pool } from "pg";
import crypto from "node:crypto";

const databaseUrl = process.env.DATABASE_URL || "";

const pool = databaseUrl
  ? new Pool({ connectionString: databaseUrl })
  : null;

const schemaStatements = [
  `
    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE,
      password_hash TEXT NOT NULL,
      created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );
  `,
  `
    CREATE TABLE IF NOT EXISTS user_events (
      id TEXT PRIMARY KEY,
      user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
      event_type TEXT NOT NULL,
      recommendation TEXT,
      prompt TEXT,
      preferences JSONB,
      extracted_preferences JSONB,
      feedback TEXT,
      metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
      created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
    );
  `,
  `
    CREATE INDEX IF NOT EXISTS idx_user_events_user_created_at
    ON user_events (user_id, created_at DESC);
  `
];

export async function initializeDatabase() {
  if (!pool) {
    return { connected: false, reason: "DATABASE_URL is not configured." };
  }

  const client = await pool.connect();

  try {
    for (const statement of schemaStatements) {
      await client.query(statement);
    }
    return { connected: true };
  } finally {
    client.release();
  }
}

export async function query(text, params = []) {
  if (!pool) {
    const error = new Error("Database is not configured. Set DATABASE_URL to enable persistent accounts and history.");
    error.code = "DB_UNAVAILABLE";
    throw error;
  }
  return pool.query(text, params);
}

export function createId() {
  return crypto.randomUUID();
}

export async function closeDatabase() {
  if (!pool) {
    return;
  }
  await pool.end();
}
