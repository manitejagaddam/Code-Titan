from autogen_agentchat.agents import AssistantAgent
from .open_router_agent import open_router_agent

def create_planner():
    return AssistantAgent(
        name="PlannerAgent",
        model_client= open_router_agent(),
        system_message=(
            "You are a software architect. "
            "Take a project brief and break it into stack + tasks."
        )
    )
