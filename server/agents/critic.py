from autogen import AssistantAgent

def create_critic():
    return AssistantAgent(
        name="CriticAgent",
        system_message=(
            "You are a code reviewer. "
            "Check generated code for correctness, style, and security."
        )
    )
