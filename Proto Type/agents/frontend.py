import re
from clients.openai_client import get_client
from prompts.frontend import frontend_prompt

def clean_output(raw_input):
    return re.sub(r"^```html\s*|\s*```$", "", raw_input.strip(), flags=re.MULTILINE)
    

def get_response(applicationName):
    client = get_client()
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": frontend_prompt(applicationName)}]
    )

    llm_output = response.choices[0].message.content
    
    # print(llm_output)
    cleaned_res = clean_output(llm_output)
    print(cleaned_res)
    return cleaned_res


def get_frontend_part(applicationName):
    res = get_response(applicationName)
    
    return res