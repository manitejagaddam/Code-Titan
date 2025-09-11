"""
agents/planner.py

Planner agent: takes a high-level prompt (application description)
and breaks it into structured tasks for builder/critic agents.

Uses gemini_call from llm_clients.
"""
from typing import Dict

from llm_clients import gemini_call


AGENT_NAME = "PlannerAgent"


def run_planner(state: Dict) -> Dict:
    """
    Planner agent function for LangGraph.

    Args:
        state (Dict): Graph state containing at least {"prompt": str}

    Returns:
        Dict: Updated state with {"plan": str}
    """
    prompt = state.get("prompt", "").strip()
    if not prompt:
        raise ValueError("Planner received empty prompt in state")

    plan_prompt = f"""
    You are {AGENT_NAME}.
    The user provided the following request for an application:

    {prompt}

    Break this down into a structured plan with clear steps for implementation.
    Focus on:
      - Backend tasks (framework, routes, APIs)
      - Frontend tasks (UI components, pages)
      - Integrations (database, external APIs)
      - Deployment considerations
    Return the plan in bullet points.
    """

    plan = gemini_call(plan_prompt)
    return {"plan": plan}


if __name__ == "__main__":
    test_state = {"prompt": "Build me a fintech loan recommendation website"}
    out = run_planner(test_state)
    print("--- Planner output ---")
    print(out["plan"])
