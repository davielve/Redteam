# Screenshot Guide for Red Team Reports

To get the most impressive results:
1. Ensure the target app is reachable via `host.docker.internal` if it's running on your host machine.
2. Use the `mistral` or `llama3` models for high-quality reasoning.
3. The Browser Worker captures full-page screenshots by default.
4. If an agent flags an issue, look for the corresponding screenshot in the `reports/<run_id>/screenshots/` folder.
