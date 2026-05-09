# JSON Schemas for Agent Outputs

## Specialist Finding Schema (UX, QA, CRO, A11y)
```json
{
  "agent": "string",
  "findings": [
    {
      "issue": "string",
      "severity": "Critical | High | Medium | Low",
      "evidence": "string (reference DOM/logs)",
      "rationale": "string",
      "suggestion": "string"
    }
  ],
  "confidence_score": "number (0-1)"
}
```

## Fix Plan Schema
```json
{
  "executive_summary": "string",
  "prioritized_fixes": [
    {
      "rank": "number",
      "issue": "string",
      "agent_source": "string",
      "severity": "string",
      "effort": "Low | Medium | High",
      "description": "string",
      "action_steps": ["string"]
    }
  ]
}
```

## Final Report Schema
```json
{
  "metadata": {
    "url": "string",
    "timestamp": "string",
    "goal": "string"
  },
  "summary": "string",
  "scorecards": {
    "ux": "number",
    "qa": "number",
    "cro": "number",
    "a11y": "number"
  },
  "detailed_findings": [],
  "fix_plan": {}
}
```
