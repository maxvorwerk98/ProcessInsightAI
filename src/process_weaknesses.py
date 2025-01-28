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
# Process Weaknesses Analysis
#-----------------------------------------------------------------------------

def process_weaknesses(event_logs):

    try:
        with open("prompts/user_weaknesses_prompt.txt", "r", encoding="utf-8") as file:
            user_weaknesses_prompt = file.read()

        user_weaknesses_prompt = user_weaknesses_prompt.replace("<<Event-Logs>>", pm4py.llm.abstract_log_features(event_logs))
        user_weaknesses_prompt = user_weaknesses_prompt.replace("<<Variants>>", pm4py.llm.abstract_variants(event_logs))

        messages = load_conversation_history()
        messages.append({"role": "user", "content": user_weaknesses_prompt})

        response = client.chat.completions.create(
            model=model_name,
            messages=messages
        )

        result = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": result})
        save_conversation_history(messages)

        with open("output/process_weaknesses_output.txt", "w", encoding="utf-8") as file:
            file.write(result)

    except Exception as exception:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {exception}")