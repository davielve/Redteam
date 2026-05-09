# Local AI App Red Team

Local AI App Red Team er en avanceret, lokal-først audit-platform, der bruger et swarm af AI-agenter til at evaluere webapplikationer. Systemet simulerer en gruppe eksperter (UX, QA, Tilgængelighed), der gennemgår dit site for at finde kritiske fejl, brugervenlighedsproblemer og konverteringsblokeringer.

**100% Privat. 100% Lokalt. Ingen API-omkostninger.**

## Kernefunktioner

- **Autonom Udforskning**: En Playwright-baseret Browser Worker, der ikke bare kigger, men interagerer med din app for at fremprovokere fejl.
- **Multi-Agent Analyse**: Orkestrering af specialiserede agenter via n8n, der hver især fokuserer på deres domæne (UX, QA, CRO, A11y).
- **Lokal LLM Integration**: Bruger Ollama til at køre modeller som Mistral og Llama 3 direkte på din egen hardware eller server.
- **Evidensbaseret Rapportering**: Genererer detaljerede Markdown-rapporter med screenshots, konsol-logs og prioriterede handlingsplaner.

## Arkitektur

Systemet er bygget som en microservice-arkitektur i Docker:

- **n8n**: Hjernen, der styrer workflowet og agent-kommunikationen.
- **Ollama**: Motoren, der leverer AI-intelligensen.
- **Browser Worker (Python/FastAPI)**: Øjnene, der automatiserer Playwright-browseren.
- **Demo App (React)**: En test-app med bevidst indbyggede fejl til validering af systemet.

## Hurtig Start

### Forudsætninger
- Docker og Docker Compose installeret.
- En kørende Ollama-server (lokalt eller på netværket).

### Opsætning
1. Klone repositoriet og konfigurer miljøet:
   ```bash
   cp .env.example .env
   # Rediger .env og indsæt din Ollama IP hvis den kører eksternt
   ```

2. Start alle tjenester:
   ```bash
   make start
   ```

3. Hent de nødvendige modeller til din Ollama-server:
   ```bash
   ollama pull mistral
   ```

4. Konfiguration af n8n:
   - Åbn n8n på `http://localhost:5678`.
   - Importer workflowet fra `n8n/workflows/local-ai-app-red-team-main.json`.
   - Klik på "Manual Audit Trigger" og indtast URL'en på den app, du vil auditere (f.eks. `http://demo-app:3000`).

## Rapportering
Efter hver kørsel gemmes en komplet rapport i `reports/` mappen. Du kan hurtigt læse den seneste rapport direkte i terminalen med:
```bash
make report
```

## Sikkerhed og Lovlighed
Dette værktøj er designet til auditering af egne applikationer eller i lukkede udviklingsmiljøer. Det udfører ikke ondsindede angreb, men fokuserer udelukkende på UX-forbedringer og kvalitetssikring.

## Licens
Open-source under MIT-licensen.
