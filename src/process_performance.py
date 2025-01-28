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
# Process Performance Analysis
#-----------------------------------------------------------------------------

def process_performance(event_logs):

    try:
        with open("prompts/user_performance_prompt.txt", "r", encoding="utf-8") as file:
            user_performance_prompt = file.read()

        user_performance_prompt = user_performance_prompt.replace("<<DFG>>", pm4py.llm.abstract_dfg(event_logs))

        messages = load_conversation_history()
        messages.append({"role": "user", "content": user_performance_prompt})

        response = client.chat.completions.create(
            model=model_name,
            messages=messages
        )

        result = response.choices[0].message.content
        
        messages.append({"role": "assistant", "content": result})
        save_conversation_history(messages)

        with open("output/process_performance_output.txt", "w", encoding="utf-8") as file:
            file.write(result)

    except Exception as exception:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {exception}")