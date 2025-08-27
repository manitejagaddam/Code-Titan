from autogen.agentchat import GroupChatManager
import os
from dotenv import load_dotenv

load_dotenv()

def create_chat_manager(groupchat):
    llm_config = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "api_base": "https://openrouter.ai/api/v1",
        "api_key": os.getenv("OPENROUTER_API_KEY"),
        "temperature": 0,
    }

    return GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config
    )
