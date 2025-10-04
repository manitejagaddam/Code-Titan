import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()



class GroqAgent:
    
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
    
    def getClient(self):
        return self.client  