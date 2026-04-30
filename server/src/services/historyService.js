import { createId, query } from "../db.js";

function mapEvent(row) {
  return {
    id: row.id,
    userId: row.user_id,
    type: row.event_type,
    recommendation: row.recommendation,
    prompt: row.prompt,
    preferences: row.preferences,
    extractedPreferences: row.extracted_preferences,
    feedback: row.feedback,
    metadata: row.metadata || {},
    timestamp: row.created_at
  };
}

export async function listUserEvents(userId, limit = 50) {
  const result = await query(
    `
      SELECT id, user_id, event_type, recommendation, prompt, preferences,
             extracted_preferences, feedback, metadata, created_at
      FROM user_events
      WHERE user_id = $1
      ORDER BY created_at DESC
      LIMIT $2
    `,
    [userId, limit]
  );

  return result.rows.map(mapEvent);
}

export async function createUserEvent(userId, entry) {
  const result = await query(
    `
      INSERT INTO user_events (
        id, user_id, event_type, recommendation, prompt, preferences,
        extracted_preferences, feedback, metadata
      )
      VALUES ($1, $2, $3, $4, $5, $6::jsonb, $7::jsonb, $8, $9::jsonb)
      RETURNING id, user_id, event_type, recommendation, prompt, preferences,
                extracted_preferences, feedback, metadata, created_at
    `,
    [
      createId(),
      userId,
      entry.type,
      entry.recommendation || null,
      entry.prompt || null,
      JSON.stringify(entry.preferences || null),
      JSON.stringify(entry.extractedPreferences || null),
      entry.feedback || null,
      JSON.stringify(entry.metadata || {})
    ]
  );

  return mapEvent(result.rows[0]);
}

export function buildRecommendationHistory(events) {
  return events.map((event) => ({
    recommendation: event.recommendation,
    name: event.recommendation,
    feedback: event.feedback,
    liked: event.feedback === "like"
  }));
}
