from autogen import AssistantAgent
from open_router_agent import open_router_agent

def create_frontend():
    return AssistantAgent(
        name="FrontendAgent",
        model_client= open_router_agent,
        system_message=(
            "You are a frontend engineer. "
            "Generate React + Tailwind UI components and write them to files."
        )
    )
