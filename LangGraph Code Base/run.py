"""
run.py

CLI entry point to execute the CodeTitan LangGraph workflow.
"""
import argparse
import logging
from graph import build_graph
from configuration.config import CONFIG

# --- Logging setup ---
logging.basicConfig(level=CONFIG['log_level'].upper())
logger = logging.getLogger(CONFIG['project_name'])


def main():
    parser = argparse.ArgumentParser(description="Run CodeTitan LangGraph workflow.")
    parser.add_argument("prompt", type=str, help="High-level prompt describing the application")

    args = parser.parse_args()
    user_prompt = args.prompt.strip()

    if not user_prompt:
        logger.error("Prompt is empty. Exiting.")
        return

    # Build and compile graph
    graph = build_graph()
    workflow = graph.compile()

    # Run workflow
    logger.info("Running workflow for prompt: %s", user_prompt)
    final_state = workflow({"prompt": user_prompt})

    # Print outputs
    print("\n--- Final Workflow Output ---")
    for key, value in final_state.items():
        print(f"\n[{key.upper()}]:\n{value}")


if __name__ == "__main__":
    main()
