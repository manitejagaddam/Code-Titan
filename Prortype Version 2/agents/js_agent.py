import os
import re
from dotenv import load_dotenv
from clients.groq import GroqAgent
from prompts.js_prompt import get_js_prompt


class JSAgent:
    
    def __init__(self, applicationName : str):
        self.client = GroqAgent.getClient()
        self.applicationName = applicationName
        
    def __get_prompt(self, html: str):
        return get_js_prompt(applicationName=self.applicationName, html=html)
        
    def __clean_output(self, raw_input : str) -> str:
        return re.sub(r"^```javascript\s*|\s*```$", "", raw_input.strip(), flags=re.MULTILINE)
    
    
    def generate(self, html: str):
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": self.__get_prompt(html=html)}]
        )
        
        llm_output = response.choices[0].message.content
        
        cleaned_res = self.__clean_output(llm_output)
        
        return {
            "filename": "app.js",
            "content": cleaned_res
        }
    
