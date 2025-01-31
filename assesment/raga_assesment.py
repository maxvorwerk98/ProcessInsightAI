#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import os
import json

from openai import OpenAI
from dotenv import load_dotenv
from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, answer_correctness, answer_similarity

#-----------------------------------------------------------------------------
# Config
#-----------------------------------------------------------------------------

load_dotenv(dotenv_path='config/.env')

client = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

#-----------------------------------------------------------------------------
# RAGAs-Framework Assesment
#-----------------------------------------------------------------------------

with open("assesment/raga_assesment.json", "r", encoding="utf-8") as file:
    data = json.load(file)

prompts = [entry["prompt"] for entry in data]
responses = [entry["generated_response"] for entry in data]
ground_truths = [entry["ground_truth"] for entry in data]

data = Dataset.from_dict({
    "question": prompts,
    "answer": responses,
    "ground_truth": ground_truths
})

scores = evaluate(data, metrics=[answer_relevancy, answer_correctness, answer_similarity])

print(scores)
