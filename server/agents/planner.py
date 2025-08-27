from autogen import AssistantAgent

def create_planner():
    return AssistantAgent(
        name="PlannerAgent",
        system_message=(
            "You are a software architect. "
            "Take a project brief and break it into stack + tasks."
        )
    )
