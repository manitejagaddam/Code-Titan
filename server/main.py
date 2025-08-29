# from agents.planner import create_planner
# from agents.frontend import create_frontend
# from agents.backend import create_backend
# from agents.critic import create_critic
# from agents.executor import create_executor
# from orchestrator.chat_manager import create_chat_manager

# def main():
#     # Create agents
#     planner = create_planner()
#     frontend = create_frontend()
#     backend = create_backend()
#     critic = create_critic()
#     executor = create_executor()

#     agents = [planner, frontend, backend, critic, executor]

#     # Create manager
#     manager = create_chat_manager(agents)

#     # Start conversation
#     planner.initiate_chat(
#         manager,
#         message="Build a loan app MVP with login, dashboard, loan form, and admin panel."
#     )

#     # Example: run pytest after code is generated
#     result = executor.run_code("pytest -q")
#     print("Test run results:", result)

# if __name__ == "__main__":
#     main()



import asyncio
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.teams import RoundRobinGroupChat


from .agents.backend import create_backend
from .agents.critic import create_critic
from .agents.executor import create_executor
from .agents.frontend import create_frontend
from .agents.planner import create_planner



def get_agents():
    planner = create_planner()
    frontend = create_frontend()
    backend = create_backend()
    critic = create_critic()
    executor = create_executor()

    agents = [planner, frontend, backend, critic, executor]


team = RoundRobinGroupChat(
    participants=get_agents(),
    max_turns=2
)


async def run_team():
    task = MultiModalMessage(content=["create a basic to do application"], source="user")
    
    result = await team.run(task=task)
    print(result.messages)
    return result.messages


if __name__ == "__main__":
    asyncio.run(run_team())