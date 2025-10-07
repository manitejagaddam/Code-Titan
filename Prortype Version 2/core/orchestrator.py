import webbrowser
import os
from agents.html_agent import HTMLAgent
from agents.css_agent import CSSAgent
from agents.js_agent import JSAgent
from agents.critic import CriticAgent

from core.file_manager import FileManager



class Orchestrator:
    
    def __init__(self, applicationName):
        # Creating all the Agents 
        self.html_agent = HTMLAgent(applicationName=applicationName)
        self.css_agent = CSSAgent(applicationName=applicationName)
        self.js_agent = JSAgent(applicationName=applicationName)
        self.critic = CriticAgent()
        self.file_manager = FileManager()
    
    
    def __build(self, user_prompt: str, output_dir="output"):
        # Step 1: HTML
        html_output = self.html_agent.generate()

        # Step 2: CSS
        css_output = self.css_agent.generate(html_output["content"])

        # Step 3: JS
        js_output = self.js_agent.generate(html_output["content"])

        # Step 4: Critic Validation
        files = [html_output, css_output, js_output]
        self.critic.review(files)

        # Step 5: File Saving
        for f in files:
            self.file_manager.write_file(f["filename"], f["content"], output_dir)

        return f"App generated in {output_dir}/"
    
    def __open_file(self, output_dir = "output"):
        file_path = os.path.abspath(f"{output_dir}/index.html")  # replace with your file name
        file_url = f"file://{file_path}"   # Convert file path to URL format
        print("file url : ", file_url)
        webbrowser.open(file_url)
        
    def build_app(self, user_promt: str, output_dir = "output"):
        return self.__build(user_prompt = user_promt, output_dir = output_dir)
    
    def build_and_run(self, user_prompt: str, output_dir = "output"):
        self.__build(user_prompt=user_prompt, output_dir=output_dir)
        self.__open_file(output_dir)