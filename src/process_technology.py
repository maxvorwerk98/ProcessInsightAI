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
# Führt eine Technologieanalyse durch, um Technologien oder Maßnahmen zu 
# evaluieren, um die zuvor identifizierten Schwachstellen zu adressieren.
#
# Ablauf:
# - Lädt Prompt aus einer Datei
# - Lädt zuvor ermittelten Schwachstellen aus einer Datei
# - Ersetzt Platzhalter im Prompt mit Schwachstellen
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