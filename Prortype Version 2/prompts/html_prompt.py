

def get_html_prompt(applicationName):
    
    return f'''
    You are a frontend expert. Produce only valid HTML5 code for an application named {applicationName}. The HTML must:

    Include a responsive meta tag and a <title> that uses {applicationName}.

    Include a stylesheet link: <link rel="stylesheet" href="style.css">.

    Do not include any JavaScript code inside the HTML (no <script> contents, no inline event handlers).

    Still include a script tag that references app.js: <script src="app.js"></script> placed at the end of the <body>.

    Use semantic HTML (header, main, nav, footer, sections) and accessible structure (aria where appropriate).

    Do not include any explanatory text, comments, or anything else—output must be only the HTML code.

    Produce a complete, well-formatted HTML document with placeholders where needed (but no extra prose).
'''