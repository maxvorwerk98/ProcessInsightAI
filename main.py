#-----------------------------------------------------------------------------
# Program description
#-----------------------------------------------------------------------------
#
#   ProcessInsightAI is an LLM-powered tool designed to analyze processes using real process data in the form of event logs. Based on the event logs, the tool 
#   conducts a four-phase technology analysis, structured as follows:
#
#   Process Discovery: Performs a fundamental analysis to gain an initial overview of the process, understand its structure, and identify its main steps.
#   Performance Analysis: Examines the process to identify bottlenecks, delays, inefficiencies, or potential cases of fraud that impact performance.
#   Technology Analysis: Evaluates suitable technologies to address the previously identified anomalies and provides a detailed plan for their implementation.
#   Forecasting: Assesses the impact of the selected technologies on the process to analyze their potential benefits and effectiveness.
#
#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

from src.process_input import load_event_logs
from src.process_discovery import process_discovery
from src.process_performance import process_performance
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
        #process_discovery(event_logs)
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
        process_technology(event_logs)
        print("Process-Technology-Analysis erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------

if __name__ == "__main__":
    main()