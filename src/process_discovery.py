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
# Führt eine grundlegende Prozessanalyse durch, um den Happy-Path des Prozesses zu identifizieren.
#
# Ablauf:
# - Lädt Prompt aus einer Datei
# - Ersetzt Platzhalter im Prompt mit abstrahierter Darstellung des Prozesses
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

def process_discovery(event_logs):
    
    try:
        with open("prompts/user_discovery_prompt.txt", "r", encoding="utf-8") as file:
            user_discovery_prompt = file.read()

        user_discovery_prompt = user_discovery_prompt.replace("<<DFG>>", pm4py.llm.abstract_dfg(event_logs))

        messages = load_conversation_history()
        messages.append({"role": "user", "content": user_discovery_prompt})

        response = client.chat.completions.create(
            model=model_name,
            messages=messages
        )

        result = response.choices[0].message.content

        messages.append({"role": "assistant", "content": result})
        save_conversation_history(messages)

        with open("output/process_discovery_output.txt", "w", encoding="utf-8") as file:
            file.write(result)

    except Exception as exception:
        print(f"Ein unerwarteter Fehler ist aufgetreten: {exception}")