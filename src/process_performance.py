#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import os
import pm4py
import pandas as pd

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


    data_frame = pm4py.convert.convert_to_dataframe(event_logs)

    # Umwandlung des Timestamps in ein Datetime-Format
    data_frame['timestamp'] = pd.to_datetime(data_frame['timestamp'])

    # Berechnung der Durchlaufzeiten pro case_id
    durations = data_frame.groupby('case_id')['timestamp'].agg(['min', 'max'])
    durations['duration'] = (durations['max'] - durations['min']).dt.total_seconds()

    # Zusammenführen der Durchlaufzeiten mit den ursprünglichen Daten
    data_frame = data_frame.merge(durations[['duration']], left_on='case_id', right_index=True)
    print(data_frame.head())

    relevant_data = data_frame[['concept:name', 'claim_amount', 'type_of_accident', 'user_type', 'duration']]
    print(relevant_data.head())

    relevant_data = pd.get_dummies(relevant_data, columns=['type_of_accident', 'user_type'])

    correlations = relevant_data.corr()['duration'].sort_values(ascending=False)
    print(correlations)

    correlations_dict = correlations.to_dict()
    print(correlations_dict)


    with open("prompts/user_performance_prompt_2.txt", "r", encoding="utf-8") as file:
        user_performance_prompt_2 = file.read()

    user_performance_prompt_2 = user_performance_prompt_2.replace("<<Process-Variants>>", correlations_dict)

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