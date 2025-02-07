#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import json

#-----------------------------------------------------------------------------
# Setzt die Konversationshistorie zurück, indem eine vordefinierte Nachricht gespeichert wird.
#-----------------------------------------------------------------------------

def clear_conversation_history():

    history = [{"role": "developer", "content": "Du bist ein KI-gestütztes Prozessanalyse-Tool."}]

    with open("output/conversation_history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

#-----------------------------------------------------------------------------
# Lädt die gespeicherte Konversationshistorie aus der JSON-Datei.
#-----------------------------------------------------------------------------

def load_conversation_history():

    with open("output/conversation_history.json", "r", encoding="utf-8") as file:
        return json.load(file)

#-----------------------------------------------------------------------------
# Speichert die aktuelle Konversationshistorie in eine JSON-Datei.
#-----------------------------------------------------------------------------

def save_conversation_history(messages):

    with open("output/conversation_history.json", "w", encoding="utf-8") as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)
