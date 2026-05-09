import os
import json
from datetime import datetime
from .config import REPORTS_DIR

def create_run_folder():
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(REPORTS_DIR, run_id)
    os.makedirs(path, exist_ok=True)
    os.makedirs(os.path.join(path, "screenshots"), exist_ok=True)
    return run_id, path

def save_json(path, filename, data):
    with open(os.path.join(path, filename), "w") as f:
        json.dump(data, f, indent=2)

def get_screenshot_path(run_id, filename):
    return os.path.join(run_id, "screenshots", filename)
