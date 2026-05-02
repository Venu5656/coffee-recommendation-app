import { Router } from "express";
import { coffeeProfiles, filterOptions } from "@coffee/shared/coffeeProfiles";
import { deriveDashboardData } from "@coffee/shared/dashboard";
import { didYouKnowInsights, insightsDashboard } from "@coffee/shared/insights";
import { recommendCoffee } from "@coffee/shared/recommendation";
import { getChatRecommendation } from "../services/chatService.js";
import { loginUser, registerUser } from "../services/authService.js";
import { buildRecommendationHistory, createUserEvent, listUserEvents } from "../services/historyService.js";
import { optionalAuth, requireAuth } from "../middleware/auth.js";

const router = Router();

router.use(optionalAuth);

router.get("/health", (_req, res) => {
  res.json({ ok: true });
});

router.post("/auth/register", async (req, res, next) => {
  try {
    const { name = "", email = "", password = "" } = req.body || {};

    if (!name.trim() || !email.trim() || password.length < 8) {
      return res.status(400).json({
        error: "Name, email, and a password with at least 8 characters are required."
      });
    }

    const auth = await registerUser({ name, email, password });
    return res.status(201).json(auth);
  } catch (error) {
    return next(error);
  }
});

router.post("/auth/login", async (req, res, next) => {
  try {
    const { email = "", password = "" } = req.body || {};

    if (!email.trim() || !password) {
      return res.status(400).json({ error: "Email and password are required." });
    }

    const auth = await loginUser({ email, password });
    return res.json(auth);
  } catch (error) {
    return next(error);
  }
});

router.get("/auth/me", requireAuth, (req, res) => {
  res.json({ user: req.user });
});

router.get("/profiles", (_req, res) => {
  res.json({ profiles: coffeeProfiles, filterOptions });
});

router.get("/insights", (_req, res) => {
  res.json({ insights: didYouKnowInsights, dashboard: insightsDashboard });
});

router.get("/history", requireAuth, async (req, res, next) => {
  try {
    const history = await listUserEvents(req.user.id);
    res.json({ history });
  } catch (error) {
    next(error);
  }
});

router.get("/dashboard", requireAuth, async (req, res, next) => {
  try {
    const history = await listUserEvents(req.user.id, 200);
    const dashboard = deriveDashboardData(history, req.user.name);
    res.json({ dashboard });
  } catch (error) {
    next(error);
  }
});

router.post("/feedback", requireAuth, async (req, res, next) => {
  try {
    const { recommendation = "", feedback = "" } = req.body || {};

    if (!recommendation || !feedback) {
      return res.status(400).json({ error: "Recommendation and feedback are required." });
    }

    const entry = await createUserEvent(req.user.id, {
      type: "feedback",
      recommendation,
      feedback,
      metadata: {}
    });

    return res.status(201).json({ entry });
  } catch (error) {
    return next(error);
  }
});

router.post("/recommend", async (req, res, next) => {
  try {
    const { preferences = {}, history = [] } = req.body || {};
    const effectiveHistory = req.user
      ? await listUserEvents(req.user.id, 200)
      : history;

    const recommendation = recommendCoffee(preferences, effectiveHistory);
    let persistedEntry = null;

    if (req.user) {
      persistedEntry = await createUserEvent(req.user.id, {
        type: "filter",
        recommendation: recommendation.drink.name,
        preferences,
        metadata: {
          explorationUsed: recommendation.explorationUsed,
          source: "filters"
        }
      });
    }

    res.json({ ...recommendation, persistedEntry });
  } catch (error) {
    next(error);
  }
});

router.post("/chat", async (req, res, next) => {
  try {
    const { message = "", history = [] } = req.body || {};
    const effectiveHistory = req.user
      ? buildRecommendationHistory(await listUserEvents(req.user.id))
      : history;

    const result = await getChatRecommendation(message, effectiveHistory);
    let persistedEntry = null;

    if (req.user) {
      persistedEntry = await createUserEvent(req.user.id, {
        type: "chat",
        recommendation: result.recommendation.drink.name,
        prompt: message,
        extractedPreferences: result.extractedPreferences,
        metadata: {
          source: "chat",
          usedLlm: result.usedLlm
        }
      });
    }

    res.json({ ...result, persistedEntry });
  } catch (error) {
    next(error);
  }
});

export default router;
