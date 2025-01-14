#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import os

from openai import OpenAI
from dotenv import load_dotenv

#-----------------------------------------------------------------------------
# Config
#-----------------------------------------------------------------------------

load_dotenv(dotenv_path='config/.env')

client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

model_name = "gpt-4o"

#-----------------------------------------------------------------------------
# Process Discovery
#-----------------------------------------------------------------------------

def process_discovery(formatted_event_logs):

    with open("/templates/system_prompt.txt", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    with open("templates/user_prompt.txt", "r", encoding="utf-8") as file:
        user_prompt = file.read().format(event_logs=formatted_event_logs)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": [{"type": "text", "text": system_prompt}]
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": user_prompt}]
            }
        ]
    )

    with open("chatgpt_response.txt", "w", encoding="utf-8") as file:
        file.write(response["choices"][0]["message"]["content"])

    return response["choices"][0]["message"]["content"]