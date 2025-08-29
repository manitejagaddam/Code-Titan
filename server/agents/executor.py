from autogen import UserProxyAgent
from .open_router_agent import open_router_agent
from tools.run_ops import run_command

def create_executor():
    agent = UserProxyAgent(
        name="ExecutorAgent",
        model_client= open_router_agent,
        human_input_mode="NEVER",
        code_execution_config={"work_dir": "sandbox", "use_docker": False}
    )

    # Custom helper: run shell commands
    def run_code(cmd: str):
        return run_command(cmd)

    # Expose tool
    agent.run_code = run_code
    return agent
