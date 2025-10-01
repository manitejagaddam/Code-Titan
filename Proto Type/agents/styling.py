import re
from prompts.style import styling_prompt
from clients.openai_client import get_client

def clean_output(raw_input):
    return re.sub(r"^```css\s*|\s*```$", "", raw_input.strip(), flags=re.MULTILINE)
    

def get_response(ApplicationName, frontend):
    client = get_client()
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": styling_prompt(ApplicationName, frontend)}]
    )
    
    llm_output = response.choices[0].message.content
    
    # print(llm_output)
    cleaned_res = clean_output(llm_output)
    # print(cleaned_res)
    return cleaned_res



def get_css_part(ApplicationName, frontend):
    return get_response(ApplicationName, frontend)
