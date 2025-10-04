import os
import re
from dotenv import load_dotenv
from clients.groq import GroqAgent
from prompts.html_prompt import get_html_prompt


class HTMLAgent:
    
    def __init__(self, applicationName : str):
        self.client = GroqAgent.getClient()
        self.applicationName = applicationName
    
    def __get_prompt(self):
        return get_html_prompt(applicationName=self.applicationName)
        
    def __clean_output(self, raw_input : str) -> str:
        return re.sub(r"^```html\s*|\s*```$", "", raw_input.strip(), flags=re.MULTILINE)
    
    
    def generate(self):
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": self.__get_prompt()}]
        )
        
        llm_output = response.choices[0].message.content
        
        cleaned_res = self.__clean_output(llm_output)
        
        return {
            "filename": "index.html",
            "content": cleaned_res
        }
    
