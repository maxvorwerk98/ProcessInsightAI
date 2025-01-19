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

    with open("prompts/user_discovery_prompt.txt", "r", encoding="utf-8") as file:
        user_discovery_prompt = file.read()

    user_discovery_prompt = user_discovery_prompt.replace("<<Petri-Netz>>", pm4py.llm.abstract_petri_net(net, im, fm))

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": user_discovery_prompt}
        ]
    )

    with open("output/process_discovery_output.txt", "w", encoding="utf-8") as file:
        file.write(response.choices[0].message.content)