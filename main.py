#-----------------------------------------------------------------------------
# Program description
#-----------------------------------------------------------------------------
#
#   ProcessInsightAI is an LLM-powered tool designed to analyze processes based on real process data in the form of event logs. Using these event logs, the tool #   performs a four-stage technology analysis, divided into the following phases:
#
#   - Process Discovery: Fundamental analysis to identify the process structure and key process steps.
#   - Performance Analysis: Examination of the process to identify delays and bottlenecks affecting performance.
#   - Weakness Analysis: Investigation of the root causes of previously identified anomalies.
#   - Technology Analysis: Evaluation of suitable technologies to address the identified anomalies.
#
#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

from src.process_input import load_event_logs
from src.process_discovery import process_discovery
from src.process_performance import process_performance
from src.process_weaknesses import process_weaknesses 
from src.process_technology import process_technology

#-----------------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------------

def main():

    file_path = "input/data_claim_process.xes"

#-----------------------------------------------------------------------------

    try:
        event_logs = load_event_logs(file_path)
        print("Event-Logs erfolgreich geladen.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------

    try:
        process_discovery(event_logs)
        print("Process-Discovery erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------

    try:
        process_performance(event_logs)
        print("Process-Performance-Analysis erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------

    try:
        process_weaknesses(event_logs)
        print("Process-Weakness-Analysis erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------

    try:
        process_technology(event_logs)
        print("Process-Technology-Analysis erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------

if __name__ == "__main__":
    main()