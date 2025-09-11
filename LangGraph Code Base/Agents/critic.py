"""
agents/critic.py

Critic agent: reviews generated code for correctness, style, and security.
Suggests improvements or corrections if necessary.

Uses gemini_call from llm_clients.
"""
from typing import Dict

from llm_clients import gemini_call


AGENT_NAME = "CriticAgent"


def run_critic(state: Dict) -> Dict:
    """
    Critic agent function for LangGraph.

    Args:
        state (Dict): Graph state containing at least {"code": str}

    Returns:
        Dict: Updated state with {"review": str}
    """
    code = state.get("code", "").strip()
    if not code:
        raise ValueError("Critic received empty code in state")

    critic_prompt = f"""
    You are {AGENT_NAME}.
    Review the following code carefully:

    {code}

    Check for:
      - Syntax errors
      - Logical mistakes
      - Security vulnerabilities
      - Code style and best practices

    If issues exist, suggest specific improvements. Otherwise, confirm it looks good.
    Return your review in clear bullet points.
    """

    review = gemini_call(critic_prompt)
    return {"review": review}


if __name__ == "__main__":
    test_state = {"code": "### FILE: app.py\nprint('Hello world')"}
    out = run_critic(test_state)
    print("--- Critic output ---")
    print(out["review"])
