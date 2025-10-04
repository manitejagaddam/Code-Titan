import os
from dotenv import load_dotenv
from groq import Groq

class GroqAgent:
    
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)

    @classmethod
    def getClient(cls):
        """Factory style: creates a new client from a new instance"""
        instance = cls()
        return instance.client
