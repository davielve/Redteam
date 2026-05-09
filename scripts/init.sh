#!/bin/bash
cp .env.example .env
docker compose up -d --build
./scripts/pull-model.sh
