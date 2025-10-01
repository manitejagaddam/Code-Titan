from prompts.style import styling_prompt
from clients.openai_client import get_client

def get_response(ApplicationName):
    client = get_client()
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": styling_prompt(ApplicationName)}]
    )
    
    llm_output = response.choices[0].message.content
    
    print(llm_output)
    return llm_output



def get_css_part(ApplicationName):
    return get_response(ApplicationName)
