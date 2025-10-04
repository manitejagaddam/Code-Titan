

def get_js_prompt(applicationName : str, html : str) -> str:
    return f'''
    You are a JavaScript expert. Produce only valid JavaScript code for an application named {applicationName} using the HTML code provided as {html}. The code must:

    Be self-contained and functional with the provided HTML.

    Include only useful, working JavaScript.

    Do not include any comments, explanations, or extra descriptions.

    Do not generate HTML or CSS—only JavaScript.

    Include code for initializing, handling basic DOM interactions, and wiring up any required functionality based on the given HTML structure.

    Output must be only JavaScript code, ready to be saved as app.js.
'''