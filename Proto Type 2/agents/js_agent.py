import os
import re
from dotenv import load_dotenv
from clients.groq import GroqAgent
from prompts.js_prompt import get_js_prompt


class HtmlAgent:
    
    def __init__(self, applicationName : str, html : str):
        self.client = GroqAgent.getClient()
        self.prompt = get_js_prompt(applicationName=applicationName, html=html)
        
    def clean_output(raw_input : str) -> str:
        return re.sub(r"^```html\s*|\s*```$", "", raw_input.strip(), flags=re.MULTILINE)
    
    
    def response(self):
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": self.prompt}]
        )
        
        llm_output = response.choices[0].message.content
        
        cleaned_res = self.clean_output(llm_output)
        
        return {
            "filename": "app.js",
            "content": cleaned_res
        }
    
