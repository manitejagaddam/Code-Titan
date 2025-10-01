import openai
import os
from groq import Groq
from dotenv import load_dotenv




def client():
    load_dotenv()

    api_key = os.getenv("GROQ_KEY")

    client = Groq(api_key = api_key)
    
    return client