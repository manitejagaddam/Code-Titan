

def styling_prompt(applicationName : str, html : str) -> str:
    return f'''
    You are the Styling expert in CSS give me only the CSS code for building the application {applicationName} respectively as the html code is {html} i need no extra description or any extra comments other than the usefull
'''