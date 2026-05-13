import json
import os
from pathlib import Path

CONFIG_FILE = Path.home() / '.devkit' / 'config.json'
DEFAULTS = {
    'ai_tool': 'claude',  # ou 'gemini'
    'theme': 'dark',
    'show_spinner': True,
}

def load_config() -> dict:
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r') as f:
                return {**DEFAULTS, **json.loads(f.read())}
        except Exception:
            return DEFAULTS
    return DEFAULTS

def save_config(cfg: dict):
    CONFIG_FILE.parent.mkdir(exist_ok=True)
    with open(CONFIG_FILE, 'w') as f:
        json.dump(cfg, f, indent=2)
