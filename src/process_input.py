#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import pm4py

#-----------------------------------------------------------------------------
# Lädt die Event-Logs aus einer XES-Datei.
#
# Parameter:
# - file_path: Pfad zur XES-Datei
#
# Rückgabe:
# - event_logs: Prozessdaten in Form von Event-Logs
#-----------------------------------------------------------------------------

def load_event_logs(file_path):
    
    try:
        event_logs = pm4py.read_xes(file_path)
        return event_logs
    except Exception as exception:
        raise ValueError(f"Fehler beim Laden der Event-Logs: {exception}")