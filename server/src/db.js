import { Pool } from "pg";
import crypto from "node:crypto";

const databaseUrl =
  process.env.DATABASE_URL || "postgresql:///postgres?host=/tmp";

const pool = new Pool({
  connectionString: databaseUrl
});

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
  const client = await pool.connect();

  try {
    for (const statement of schemaStatements) {
      await client.query(statement);
    }
  } finally {
    client.release();
  }
}

export async function query(text, params = []) {
  return pool.query(text, params);
}

export function createId() {
  return crypto.randomUUID();
}

export async function closeDatabase() {
  await pool.end();
}
