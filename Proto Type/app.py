from agents.frontend import get_frontend_part
from agents.styling import get_css_part
from agents.logic import get_logic_part
import os
import webbrowser

def write_to_file_in_path(folder_path, filename, content):
    os.makedirs(folder_path, exist_ok=True)  # Ensure folder exists
    file_path = os.path.join(folder_path, filename)
    with open(file_path, 'w', encoding='utf-8') as file:  # Use UTF-8 encoding
        file.write(content + '\n')
    print(f"Content added to {file_path}.")
    
    
    
    
def open_file():
    file_path = os.path.abspath("sandbox/index.html")  # replace with your file name

    # Convert file path to URL format
    file_url = f"file://{file_path}"

    # Open in default web browser
    webbrowser.open(file_url)
    
    
def createApp(ApplicationName):
    frontend = get_frontend_part(ApplicationName)
    styling = get_css_part(ApplicationName, frontend=frontend)  
    logic = get_logic_part(ApplicationName, frontend = frontend)
    
    folder_path = "sandbox"
    
    write_to_file_in_path(folder_path, "index.html", frontend)
    write_to_file_in_path(folder_path, "style.css", styling)
    write_to_file_in_path(folder_path, "app.js", logic)
    
    open_file()

def main():
    applicationName = input("Enter your application name: ")
    createApp(applicationName)

if __name__ == "__main__":
    main()
