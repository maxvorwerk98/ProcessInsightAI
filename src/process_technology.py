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
# Process_Technology
#-----------------------------------------------------------------------------

def process_technology(event_logs):

    with open("prompts/user_performance_prompt.txt", "r", encoding="utf-8") as file:
        user_performance_prompt = file.read()

    user_performance_prompt = user_performance_prompt.replace("<<DFG-Abstraction>>", pm4py.llm.abstract_dfg(event_logs))

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": user_performance_prompt}
        ]
    )

    with open("output/process_performance_output.txt", "w", encoding="utf-8") as file:
        file.write(response.choices[0].message.content)