"""
config.py

Central configuration for the CodeTitan / LangGraph project.
- Loads environment variables (from .env if present)
- Validates required secrets (GEMINI_API_KEY)
- Exposes defaults for GEMINI model and runtime directories

This file intentionally keeps logic minimal and raises early if required secrets are missing.
"""
from pathlib import Path
import os
from dotenv import load_dotenv

# --- base paths ---
BASE_DIR = Path(__file__).resolve().parent

# Load .env if present
# env_path = ".env"
# if env_path.exists():
#     load_dotenv(env_path)

load_dotenv()

# --- Provider selection ---
# We'll default to Gemini as requested. Keep this configurable so tests and CI can override.
USE_PROVIDER = os.getenv("USE_PROVIDER", "gemini").strip().lower()

# --- Gemini specific ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

# --- App defaults ---
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
PROJECT_NAME = os.getenv("PROJECT_NAME", "code_titan")
OUTPUT_DIR = Path(os.getenv("OUTPUT_DIR", str(BASE_DIR / "output")))

# Ensure output directory exists
try:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
except Exception as e:
    raise RuntimeError(f"Failed to create output directory {OUTPUT_DIR}: {e}")

# --- Basic validation ---
if USE_PROVIDER == "gemini" and not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. Add it to your environment or a .env file as GEMINI_API_KEY."
    )

# Export a small config dict for convenience
CONFIG = {
    "use_provider": USE_PROVIDER,
    "gemini": {
        "api_key": GEMINI_API_KEY,
        "model": GEMINI_MODEL,
    },
    "project_name": PROJECT_NAME,
    "output_dir": str(OUTPUT_DIR),
    "log_level": LOG_LEVEL,
}

# Helpful repr for debugging
if __name__ == "__main__":
    import json
    print(json.dumps(CONFIG, indent=2))
