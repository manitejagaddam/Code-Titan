from autogen import UserProxyAgent

def create_executor():
    return UserProxyAgent(
        name="ExecutorAgent",
        human_input_mode="NEVER",
        code_execution_config={"work_dir": "sandbox", "use_docker": False}
    )
