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
# Führt eine Schwachstellenanalyse durch, um die möglichen Ursachen für die 
# langen Durchlaufzeiten ermitteln.
#
# Ablauf:
# - Lädt Prompt aus einer Datei
# - Ersetzt Platzhalter im Prompt mit abstrahierten Darstellungen des Prozesses
# - Lädt bestehende Konversationshistorie und fügt die aktuelle Anfrage hinzu
# - Sendet die Anfrage an das LLM 
# - Speichert Antwort in der Konversationshistorie und in einer Datei
# - Fehlerhandling für unerwartete Fehler.
#
# Parameter:
# - event_logs: Prozessdaten in Form von Event-Logs
#
# Rückgabe:
# - Keine Rückgabe
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