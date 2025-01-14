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

model_name = "gpt-4o-mini"

#-----------------------------------------------------------------------------
# Process Discovery
#-----------------------------------------------------------------------------

def process_discovery(formatted_event_logs):

    with open("prompts/system_prompt.txt", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    with open("prompts/user_discovery_prompt.txt", "r", encoding="utf-8") as file:
        user_discovery_prompt = file.read().format(event_logs=formatted_event_logs)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system", "content": system_prompt  
            },
            {
                "role": "user", "content": user_discovery_prompt
            }
        ]
    )

    with open("output/process_discovery_output.txt", "w", encoding="utf-8") as file:
        file.write(response.choices[0].message.content)

    print("Process-Discovery erfolgreich durchgeführt.")