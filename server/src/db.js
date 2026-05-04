import { Pool } from "pg";
import crypto from "node:crypto";

const databaseUrl = process.env.DATABASE_URL || "";
const hasPgVars = Boolean(process.env.PGHOST && process.env.PGUSER && process.env.PGDATABASE);

function sslConfig() {
  const sslMode = (process.env.PGSSLMODE || "").toLowerCase();

  if (!sslMode || sslMode === "disable") {
    return undefined;
  }

  if (sslMode === "no-verify" || sslMode === "require") {
    return { rejectUnauthorized: false };
  }

  return true;
}

const poolConfig = databaseUrl
  ? { connectionString: databaseUrl }
  : hasPgVars
    ? {
        host: process.env.PGHOST,
        port: Number(process.env.PGPORT || 5432),
        user: process.env.PGUSER,
        password: process.env.PGPASSWORD,
        database: process.env.PGDATABASE
      }
    : null;

if (poolConfig) {
  const ssl = sslConfig();
  if (ssl) {
    poolConfig.ssl = ssl;
  }
}

const pool = poolConfig
  ? new Pool(poolConfig)
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
    return { connected: false, reason: "PostgreSQL is not configured. Set DATABASE_URL or PGHOST/PGUSER/PGDATABASE." };
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
    const error = new Error("Database is not configured. Set DATABASE_URL or Railway PostgreSQL variables to enable persistent accounts and history.");
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
