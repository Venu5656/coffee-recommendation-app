import { findUserById, verifyToken } from "../services/authService.js";

function getBearerToken(headerValue = "") {
  if (!headerValue.startsWith("Bearer ")) {
    return null;
  }

  return headerValue.slice("Bearer ".length).trim();
}

export async function optionalAuth(req, _res, next) {
  try {
    const token = getBearerToken(req.headers.authorization);
    if (!token) {
      req.user = null;
      return next();
    }

    const payload = verifyToken(token);
    const user = await findUserById(payload.sub);
    req.user = user;
    return next();
  } catch {
    req.user = null;
    return next();
  }
}

export function requireAuth(req, res, next) {
  if (!req.user) {
    return res.status(401).json({ error: "Authentication required." });
  }

  return next();
}
