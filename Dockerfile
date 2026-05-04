FROM node:20-bookworm

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-pip python3-venv \
    && rm -rf /var/lib/apt/lists/*

COPY package.json package-lock.json ./
COPY client/package.json ./client/package.json
COPY server/package.json ./server/package.json
COPY shared/package.json ./shared/package.json
RUN npm ci

COPY frontend/requirements.txt ./frontend/requirements.txt
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/venv/bin/pip install --no-cache-dir -r frontend/requirements.txt

COPY . .

RUN npm run build

ENV PATH="/opt/venv/bin:${PATH}"
ENV NODE_ENV=production
ENV API_PORT=8787
ENV BACKEND_URL=http://127.0.0.1:8787/api

EXPOSE 8501

CMD ["./deploy/start.sh"]
