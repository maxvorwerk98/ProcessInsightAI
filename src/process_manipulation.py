#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import pandas
import pm4py

#-----------------------------------------------------------------------------
# Manipulate Event-Logs
#-----------------------------------------------------------------------------

def manipulate_event_logs(event_logs):

    try:
        manipulated_event_logs = event_logs[["case:concept:name", "concept:name", "time:timestamp"]]
        return manipulated_event_logs
    except Exception as exception:
        raise ValueError(f"Fehler beim Reduzieren der Event-Logs: {exception}")