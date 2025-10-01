from clients.openai_client import get_client
from prompts.logic import javascript_prompt

def get_response(ApplicationName):
    
    client = get_client()
    
    
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": javascript_prompt(ApplicationName)}]
    )

    llm_output = response.choices[0].message.content
    
    print(llm_output)
    return llm_output    



def get_logic_part(ApplicationName):
    return get_response(ApplicationName)