#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import os
import pm4py

from openai import OpenAI
from dotenv import load_dotenv

from src.chat_manager import load_conversation_history, save_conversation_history

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

        messages = load_conversation_history()
        messages.append({"role": "user", "content": user_technology_prompt})

        response = client.chat.completions.create(
            model=model_name,
            messages=messages
        )

        result = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": result})
        save_conversation_history(messages)

        with open("output/process_technology_output.txt", "w", encoding="utf-8") as file:
            file.write(result)

    except Exception as exception:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {exception}")