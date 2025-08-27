from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
import os 
from dotenv import load_dotenv


load_dotenv()

open_router_api_key = os.getenv("OPEN_ROUTER_API_KEY")


def open_router_agent():
    agent = OpenAIChatCompletionClient(
        base_url="https://openrouter.ai/api/v1",
        # model="google/gemma-3-27b-it:free",
        model="google/gemini-2.0-flash-exp:free",
        # model="qwen/qwen2.5-vl-72b-instruct:free",
        # model="mistralai/mistral-small-3.1-24b-instruct:free",
        # model="deepseek/deepseek-r1-0528:free",
        api_key=open_router_api_key,
        model_info={
            "family": "google",
            "vision": True,
            "function_calling": True,
            "json_output": False,
            "structured_output":True
        }
    )
    return agent