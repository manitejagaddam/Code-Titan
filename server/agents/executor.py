from autogen_agentchat.agents import AssistantAgent
from .open_router_agent import open_router_agent
from tools.run_ops import run_command


def create_executor():
    def run_code(cmd: str) -> str:
        return run_command(cmd)

    agent = AssistantAgent(
        name="ExecutorAgent",
        model_client=open_router_agent(),
        tools=[run_code],
        reflect_on_tool_use = True
        
    )


    return agent
