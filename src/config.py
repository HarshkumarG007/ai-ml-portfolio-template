import yaml
from pathlib import Path
import logging

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def load_yaml(file_name):
    file_path = PROJECT_ROOT / "configs" / file_name
    try:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        logging.warning(f"Config {file_name} not found.")
        return {}

PATHS = load_yaml("paths.yaml")
CONFIG = load_yaml("config.yaml")
