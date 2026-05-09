FROM node:20-slim AS builder
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
RUN npm run build

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /app/dist .
EXPOSE 3000
# Simple python server that doesn't care about hosts or headers
CMD ["python", "-m", "http.server", "3000"]
