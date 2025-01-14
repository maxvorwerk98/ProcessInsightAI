#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import pandas
import pm4py

#-----------------------------------------------------------------------------
# Load Event-Logs
#-----------------------------------------------------------------------------

def load_event_logs(file_path):
    try:
        event_logs = pm4py.read_csv(file_path)
        formatted_event_logs = formatting_event_logs(event_logs)
        return formatted_event_logs
    except Exception as exception:
        raise ValueError(f"Fehler beim Laden der Event-Logs: {exception}")

#-----------------------------------------------------------------------------
# Formatting Event-Logs
#-----------------------------------------------------------------------------

def formatting_event_logs(event_logs):
    formatted_event_logs = event_logs.to_csv(index=False)
    return formatted_event_logs