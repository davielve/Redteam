# System Architecture

## Core Components

### 1. n8n (Orchestrator)
The central nervous system. It handles:
- Workflow logic
- Data transformation
- Agent coordination
- Reporting

### 2. Ollama (LLM Engine)
Provides the intelligence. 
- Default Model: `mistral`
- Task: Analyzes structured data and generates JSON findings.

### 3. Browser Worker (The Eyes)
A Python/FastAPI service that wraps Playwright.
- Captures full-page screenshots.
- Extracts "Important Elements" (buttons, links, inputs) to stay within token limits.
- Collects Console logs and Network failures.

### 4. Demo App (The Target)
A Vite/React app designed to fail. It includes:
- **QA**: A button that logs a console error instead of working.
- **UX**: Confusing signup flow and weak CTAs.
- **A11y**: Poor contrast and missing labels.
- **Mobile**: A hidden menu that crashes when clicked.

## Data Flow
1. **Intake**: n8n receives a URL and a goal.
2. **Browsing**: Browser Worker visits the URL and collects "Evidence".
3. **Reasoning**: n8n splits the evidence among specialist agents (UX, QA, etc.).
4. **Synthesis**: A "Fix Planner" agent prioritizes the findings.
5. **Output**: Markdown and HTML reports are saved to the `reports/` volume.
