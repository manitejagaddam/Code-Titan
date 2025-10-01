

def frontend_prompt(applicationName : str) -> str:
    return f'''
    You are the frontend expert give me only the html code for building the application {applicationName} respectively, int the code include a line of the styling link as teh style.css and dont write any javascript code and include the scripit tag and use the app.js
'''