import os

REPORTS_DIR = os.getenv("REPORTS_DIR", "/app/reports")
MAX_STEPS = 10
TIMEOUT = 30000  # ms
DEFAULT_VIEWPORT = {"width": 1280, "height": 800}
MOBILE_VIEWPORT = {"width": 375, "height": 667}
