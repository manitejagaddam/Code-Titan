from autogen import AssistantAgent
from open_router_agent import open_router_agent


def create_backend():
    return AssistantAgent(
        name="BackendAgent",
        model_client= open_router_agent,
        system_message=(
            "You are a backend engineer. "
            "Generate FastAPI endpoints, Pydantic models, and Postgres schema."
        )
    )
