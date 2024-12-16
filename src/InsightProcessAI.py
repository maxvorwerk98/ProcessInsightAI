#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import asyncio
import os
import json
import random
import time

from openai import OpenAI
from dotenv import load_dotenv

#-----------------------------------------------------------------------------
# Config
#-----------------------------------------------------------------------------

load_dotenv(dotenv_path='config/.env')

client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

model_name = "gpt-4"

#-----------------------------------------------------------------------------
# Generate user-persona
#-----------------------------------------------------------------------------

def generate_process_analysis():

    with open('templates/system_prompt.txt', 'r') as file:
        system_prompt = file.read()

    with open('templates/user_prompt1.txt', 'r') as file:
        user_prompt1 = file.read()

    with open('templates/user_prompt2.txt', 'r') as file:
        user_prompt2 = file.read()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": [{"type": "text", "text": system_prompt}]
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": user_prompt1}]
            },
            {
                "role": "user",
                "content": [{"type": "text", "text": user_prompt2}]
            },
        ]
    )

    with open("chatgpt_response.txt", "w", encoding="utf-8") as file:
        file.write(response["choices"][0]["message"]["content"])

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------

generate_process_analysis()