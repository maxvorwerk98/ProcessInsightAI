#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import os
import pm4py
import pandas as pd

from openai import OpenAI
from dotenv import load_dotenv


import pm4py
import xml.etree.ElementTree as ET
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.log.exporter.xes import exporter as xes_exporter

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

    with open("prompts/user_performance_prompt_2.txt", "r", encoding="utf-8") as file:
        user_performance_prompt_2 = file.read()

    event_logs_df = pm4py.convert_to_dataframe(event_logs)
    event_logs_df = event_logs_df[['case:concept:name', 'claim_amount', 'type_of_accident']]
    event_logs_df = event_logs_df.groupby('case:concept:name', as_index=False).first()

    event_logs_df['duration'] = None

    case_durations = pm4py.get_all_case_durations(
        event_logs,
        activity_key='concept:name',
        case_id_key='case:concept:name',
        timestamp_key='time:timestamp'
    )

    event_logs_df['duration'] = case_durations

    event_logs_df = event_logs_df.groupby('type_of_accident').agg({
        'claim_amount': 'mean',
        'duration': 'mean'
    }).reset_index()

    event_logs_json = event_logs_df.to_json(orient="records", lines=False)

    user_performance_prompt_2 = user_performance_prompt_2.replace("<<Event-Logs>>", event_logs_json)

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": user_performance_prompt_2}
        ]
    )

    result_performance_2 = response.choices[0].message.content

    with open("output/process_performance_output_2.txt", "w", encoding="utf-8") as file:
        file.write(result_performance_2)