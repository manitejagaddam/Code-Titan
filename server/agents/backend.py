from autogen import AssistantAgent

def create_backend():
    return AssistantAgent(
        name="BackendAgent",
        system_message=(
            "You are a backend engineer. "
            "Generate FastAPI endpoints, Pydantic models, and Postgres schema."
        )
    )
