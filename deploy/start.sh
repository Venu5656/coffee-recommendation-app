#!/usr/bin/env sh
set -eu

export API_PORT="${API_PORT:-8787}"
export BACKEND_URL="${BACKEND_URL:-http://127.0.0.1:${API_PORT}/api}"

PORT="${API_PORT}" npm run start --workspace server &
API_PID="$!"

cleanup() {
  kill "$API_PID" 2>/dev/null || true
}
trap cleanup INT TERM EXIT

for _ in 1 2 3 4 5 6 7 8 9 10; do
  if python3 - <<'PY'
import os
import urllib.request

url = os.environ.get("BACKEND_URL", "http://127.0.0.1:8787/api").rstrip("/") + "/health"
try:
    with urllib.request.urlopen(url, timeout=1) as response:
        raise SystemExit(0 if response.status == 200 else 1)
except Exception:
    raise SystemExit(1)
PY
  then
    break
  fi
  sleep 1
done

streamlit run frontend/frontend.py \
  --server.address=0.0.0.0 \
  --server.port="${PORT:-8501}" \
  --server.headless=true
