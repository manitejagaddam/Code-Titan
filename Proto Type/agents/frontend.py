from clients.openai_client import get_client
from prompts.frontend import frontend_prompt

def get_response(applicationName):
    client = get_client()
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": frontend_prompt(applicationName)}]
    )

    llm_output = response.choices[0].message.content
    
    print(llm_output)
    return llm_output


def get_frontend_part(applicationName):
    res = get_response(applicationName)
    
    return res