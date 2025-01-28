#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import json

#-----------------------------------------------------------------------------
# Chat Manager
#-----------------------------------------------------------------------------

def clear_conversation_history():

    history = [{"role": "system", "content": "Du bist ein KI-gestütztes Prozessanalyse-Tool."}]

    with open("output/conversation_history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=4)

#-----------------------------------------------------------------------------

def load_conversation_history():

    with open("output/conversation_history.json", "r", encoding="utf-8") as file:
        return json.load(file)

#-----------------------------------------------------------------------------

def save_conversation_history(messages):

    with open("output/conversation_history.json", "w", encoding="utf-8") as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)
