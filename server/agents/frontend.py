from autogen import AssistantAgent

def create_frontend():
    return AssistantAgent(
        name="FrontendAgent",
        system_message=(
            "You are a frontend engineer. "
            "Generate React + Tailwind UI components and write them to files."
        )
    )
