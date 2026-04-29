import { Router } from "express";
import { coffeeProfiles, filterOptions } from "@coffee/shared/coffeeProfiles";
import { didYouKnowInsights } from "@coffee/shared/insights";
import { recommendCoffee } from "@coffee/shared/recommendation";
import { getChatRecommendation } from "../services/chatService.js";

const router = Router();

router.get("/health", (_req, res) => {
  res.json({ ok: true });
});

router.get("/profiles", (_req, res) => {
  res.json({ profiles: coffeeProfiles, filterOptions });
});

router.get("/insights", (_req, res) => {
  res.json({ insights: didYouKnowInsights });
});

router.post("/recommend", (req, res) => {
  const { preferences = {}, history = [] } = req.body || {};
  const recommendation = recommendCoffee(preferences, history);
  res.json(recommendation);
});

router.post("/chat", async (req, res, next) => {
  try {
    const { message = "", history = [] } = req.body || {};
    const result = await getChatRecommendation(message, history);
    res.json(result);
  } catch (error) {
    next(error);
  }
});

export default router;
