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
        event_logs = pm4py.read_xes(file_path)
        return event_logs
    except Exception as exception:
        raise ValueError(f"Fehler beim Laden der Event-Logs: {exception}")