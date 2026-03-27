from pathlib import Path
from datetime import datetime
import json

LOG_DIR = Path("generated/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

def write_log(step: str, payload:dict) -> None:
    timestamp = datetime.utcnow().isoformat()
    filename = LOG_DIR / f"{timestamp}_{step}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)