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
# Process Performance
#-----------------------------------------------------------------------------

def process_performance(event_logs):

    with open("prompts/user_performance_prompt_1.txt", "r", encoding="utf-8") as file:
        user_performance_prompt_1 = file.read()

    user_performance_prompt_1 = user_performance_prompt_1.replace("<<DFG>>", pm4py.llm.abstract_dfg(event_logs))

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": user_performance_prompt_1}
        ]
    )

    result_performance_1 = response.choices[0].message.content

    with open("output/process_performance_output_1.txt", "w", encoding="utf-8") as file:
        file.write(result_performance_1)

#-----------------------------------------------------------------------------


    event_logs_df = pm4py.convert.convert_to_dataframe(event_logs)

    event_logs_df = event_logs_df[['concept:name', 'time:timestamp', 'claim_amount', 'type_of_accident', 'user_type']]

    event_logs_text = event_logs_df.to_string(index=False)

    with open("prompts/user_performance_prompt_2.txt", "r", encoding="utf-8") as file:
        user_performance_prompt_2 = file.read()

    user_performance_prompt_2 = user_performance_prompt_2.replace("<<Process-Variants>>", event_logs_text)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "assistant", "content": result_performance_1},
            {"role": "user", "content": user_performance_prompt_2}
        ]
    )

    result_performance_2 = response.choices[0].message.content

    with open("output/process_performance_output_2.txt", "w", encoding="utf-8") as file:
        file.write(result_performance_2)