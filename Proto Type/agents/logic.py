import re
from clients.openai_client import get_client
from prompts.logic import javascript_prompt

def clean_output(raw_input):
    return re.sub(r"^```javascript\s*|\s*```$", "", raw_input.strip(), flags=re.MULTILINE)
    

def get_response(ApplicationName, frontend):
    
    client = get_client()
    
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": javascript_prompt(ApplicationName, frontend)}]
    )

    llm_output = response.choices[0].message.content
    
    # print(llm_output)
    cleaned_res = clean_output(llm_output)
    # print(cleaned_res)
    return cleaned_res



def get_logic_part(ApplicationName, frontend):
    return get_response(ApplicationName, frontend)