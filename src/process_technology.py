#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import os
import pm4py

from openai import OpenAI
from dotenv import load_dotenv

#-----------------------------------------------------------------------------
# Config
#-----------------------------------------------------------------------------

load_dotenv(dotenv_path='config/.env')

client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

model_name = "gpt-4"

#-----------------------------------------------------------------------------
# Process Technology
#-----------------------------------------------------------------------------

def process_technology(event_logs):

    with open("prompts/user_technology_prompt.txt", "r", encoding="utf-8") as file:
        user_technology_prompt = file.read()

    with open("output/process_performance_output_2.txt", "r", encoding="utf-8") as file:
        weaknesses = file.read()

    user_technology_prompt = user_technology_prompt.replace("<<Weaknesses>>", weaknesses)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": user_technology_prompt}
        ]
    )

    with open("output/process_technology_output.txt", "w", encoding="utf-8") as file:
        file.write(response.choices[0].message.content)