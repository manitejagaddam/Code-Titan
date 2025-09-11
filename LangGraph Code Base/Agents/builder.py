"""
agents/builder.py

Builder agent: takes the structured plan from the Planner agent
and produces code snippets/files as text output.

Uses gemini_call from llm_clients.
"""
from typing import Dict

from llm_clients import gemini_call


AGENT_NAME = "BuilderAgent"


def run_builder(state: Dict) -> Dict:
    """
    Builder agent function for LangGraph.

    Args:
        state (Dict): Graph state containing at least {"plan": str}

    Returns:
        Dict: Updated state with {"code": str}
    """
    plan = state.get("plan", "").strip()
    if not plan:
        raise ValueError("Builder received empty plan in state")

    build_prompt = f"""
    You are {AGENT_NAME}.
    Based on the following plan, generate code for the application.

    Plan:
    {plan}

    Guidelines:
      - Write modular, production-ready code.
      - Include backend (Python/FastAPI or Flask) and frontend (HTML/React).
      - Add a README.md with setup instructions.
      - Ensure the code is consistent and free of obvious errors.
      - Return the code in structured sections (use markers like ### FILE: filename).
    """

    code = gemini_call(build_prompt)
    return {"code": code}


if __name__ == "__main__":
    test_state = {"plan": "Backend: Flask API for loan recommendation. Frontend: React UI."}
    out = run_builder(test_state)
    print("--- Builder output ---")
    print(out["code"])
