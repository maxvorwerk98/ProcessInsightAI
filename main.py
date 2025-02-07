#-----------------------------------------------------------------------------
# Program description
#-----------------------------------------------------------------------------
#
#   ProcessInsightAI ist ein LLM-gestütztes Tool zur Analyse von Prozessen auf Basis realer Prozessdaten, die in Form von Event-Logs vorliegen. 
#   Dabei führt "ProcessInsightAI" eine vierstufige Technologieanalyse durch, die in fol-gende Phasen unterteilt ist:
# 
#   -	Process Discovery: Grundlegende Analyse zur Erkennung der Prozessstruktur und der wesentlichen Prozessschritte.
#   -	Process Performance: Analyse des Prozesses zur Identifikation von Verzögerun-gen und Engpässen, die die Leistung beeinträchtigen.
#   -	Process Weaknesses: Analyse der Ursachen für die zuvor identifizierten Ano-malien.
#   -	Process Technology: Evaluation geeigneter Technologien, um die zuvor identifi-zierten Anomalien zu beheben.
#
#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

from src.chat_manager import clear_conversation_history
from src.process_input import load_event_logs
from src.process_discovery import process_discovery
from src.process_performance import process_performance
from src.process_weaknesses import process_weaknesses 
from src.process_technology import process_technology

#-----------------------------------------------------------------------------
# Config
#-----------------------------------------------------------------------------

def main():

    clear_conversation_history()

    file_path = "input/data_claim_process.xes"

#-----------------------------------------------------------------------------
# Lädt die Event-Logs
#-----------------------------------------------------------------------------

    try:
        event_logs = load_event_logs(file_path)
        print("Event-Logs erfolgreich geladen.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------
# Führt die Prozessentdeckung durch
#-----------------------------------------------------------------------------

    try:
        process_discovery(event_logs)
        print("Process-Discovery erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------
# Führt die Leistungsanalyse durch
#-----------------------------------------------------------------------------

    try:
        process_performance(event_logs)
        print("Process-Performance-Analysis erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------
# Führt die Schwachstellenanalyse durch
#-----------------------------------------------------------------------------

    try:
        process_weaknesses(event_logs)
        print("Process-Weakness-Analysis erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------
# Führt die Technologieanalyse durc
#-----------------------------------------------------------------------------

    try:
        process_technology(event_logs)
        print("Process-Technology-Analysis erfolgreich durchgeführt.")
    except ValueError as exception:
        print(exception)

#-----------------------------------------------------------------------------
# Startpunkt des Programms
#-----------------------------------------------------------------------------

if __name__ == "__main__":
    main()