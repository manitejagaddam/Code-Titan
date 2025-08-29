from autogen import AssistantAgent
from .open_router_agent import open_router_agent

def create_critic():
    return AssistantAgent(
        name="CriticAgent",
        model_client= open_router_agent,
        system_message=(
            "You are a code reviewer. "
            "Check generated code for correctness, style, and security."
        )
    )
