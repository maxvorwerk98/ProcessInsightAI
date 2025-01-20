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
# Process Technology Analysis
#-----------------------------------------------------------------------------

def process_technology(event_logs):

    try: 
        with open("prompts/user_technology_prompt.txt", "r", encoding="utf-8") as file:
            user_technology_prompt = file.read()

        with open("output/process_weaknesses_output.txt", "r", encoding="utf-8") as file:
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

    except Exception as exception:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {exception}")