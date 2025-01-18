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
# Process Discovery
#-----------------------------------------------------------------------------

def process_discovery(event_logs):

    net, im, fm = pm4py.discover_petri_net_inductive(event_logs)

    with open("output/petri_net.pnml", "r", encoding="utf-8") as file:
        petri_net = file.read()

    with open("prompts/system_prompt.txt", "r", encoding="utf-8") as file:
        system_prompt = file.read()

    with open("prompts/user_discovery_prompt.txt", "r", encoding="utf-8") as file:
        user_discovery_prompt = file.read()

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_discovery_prompt + "\n\n" + pm4py.llm.abstract_petri_net(net, im, fm )}
        ]
    )

    with open("output/process_discovery_output.txt", "w", encoding="utf-8") as file:
        file.write(response.choices[0].message.content)