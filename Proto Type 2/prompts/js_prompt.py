

def get_js_prompt(applicationName : str, html : str) -> str:
    return f'''
    You are a CSS styling expert. Produce only valid CSS code for an application named {applicationName} using the HTML code provided as {html}. The CSS must:

    Be self-contained and functional for the provided HTML.

    Include only useful styling—no comments, no extra explanations, no placeholder text.

    Ensure responsive and accessible design where applicable.

    Do not generate HTML or JavaScript—only CSS.

    Output must be only CSS code, ready to be saved as style.css.
'''