.PHONY: start stop pull-model logs reset help

help:
	@echo "Local AI App Red Team - Management Commands"
	@echo "  make start       Start all services in background"
	@echo "  make stop        Stop all services"
	@echo "  make pull-model  Pull the configured Ollama model"
	@echo "  make logs        View logs for all services"
	@echo "  make reset       Stop services and remove volumes (WIPE DATA)"

start:
	docker compose up -d

stop:
	docker compose down

pull-model:
	docker exec -it redteam-ollama ollama pull mistral

logs:
	docker compose logs -f

reset:
	docker compose down -v
	rm -rf reports/*

report:
	@ls -t reports/ | head -n 1 | xargs -I {} cat reports/{}/audit_report.md
