import path from "node:path";
import { fileURLToPath } from "node:url";
import fs from "node:fs";
import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import apiRouter from "./routes/api.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

dotenv.config({ path: path.resolve(__dirname, "../../.env") });

const app = express();
const port = Number(process.env.PORT || 8787);
const clientDist = path.resolve(__dirname, "../../client/dist");

app.use(cors());
app.use(express.json());
app.use("/api", apiRouter);

if (fs.existsSync(clientDist)) {
  app.use(express.static(clientDist));
  app.get("*", (_req, res) => {
    res.sendFile(path.join(clientDist, "index.html"));
  });
}

app.use((error, _req, res, _next) => {
  res.status(500).json({
    error: error.message || "Unexpected server error"
  });
});

app.listen(port, () => {
  console.log(`Coffee API listening on http://localhost:${port}`);
});
