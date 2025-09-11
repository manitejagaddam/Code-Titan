"""
llm_clients.py

Provides wrappers for interacting with Gemini (Google Generative AI).
Relies on configuration from config.py. Exposes a simple call interface
for agents and graphs to use.

Usage:
    from llm_clients import gemini_call
    response = gemini_call("Hello world")
"""
import google.generativeai as genai
import logging
import time
from typing import Optional

from configuration.config import CONFIG

# --- Setup logging ---
logger = logging.getLogger(CONFIG["project_name"])
logger.setLevel(CONFIG["log_level"].upper())

# --- Configure Gemini ---
genai.configure(api_key=CONFIG["gemini"]["api_key"])
_model_name = CONFIG["gemini"]["model"]

# --- Core call function ---
def gemini_call(prompt: str, model: Optional[str] = None, max_retries: int = 3) -> str:
    """
    Call Gemini with the given prompt. Retries on transient errors.

    Args:
        prompt (str): User/system prompt to send.
        model (Optional[str]): Gemini model override (default from config).
        max_retries (int): Number of retries on failure.

    Returns:
        str: Text output from Gemini.
    """
    chosen_model = model or _model_name
    last_err = None

    for attempt in range(1, max_retries + 1):
        try:
            gemini_model = genai.GenerativeModel(chosen_model)
            response = gemini_model.generate_content(prompt)
            if hasattr(response, "text") and response.text:
                return response.text
            # If Gemini returns empty
            logger.warning("Empty response from Gemini on attempt %s", attempt)
            return ""
        except Exception as e:
            last_err = e
            logger.error("Gemini call failed (attempt %s/%s): %s", attempt, max_retries, e)
            time.sleep(1.5 * attempt)

    raise RuntimeError(f"Gemini call failed after {max_retries} attempts: {last_err}")


# --- Convenience wrapper for structured outputs ---
def gemini_json(prompt: str, model: Optional[str] = None, max_retries: int = 3):
    """
    Ask Gemini for JSON output. Assumes the prompt requests JSON.

    Returns parsed Python object if valid JSON, else raw text.
    """
    import json

    text = gemini_call(prompt, model=model, max_retries=max_retries)
    try:
        return json.loads(text)
    except Exception:
        logger.warning("Gemini JSON parse failed, returning raw text")
        return text


if __name__ == "__main__":
    # Simple smoke test
    out = gemini_call("Write a haiku about LangGraph.")
    print("--- Gemini response ---")
    print(out)
