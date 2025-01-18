#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import pm4py

#-----------------------------------------------------------------------------
# Manipulate Event-Logs
#-----------------------------------------------------------------------------

def manipulate_event_logs(event_logs):

    try:
        net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(event_logs)
        print(f"Petri-Netz erfolgreich generiert und exportiert")
    except Exception as exception:
        raise ValueError(f"Fehler beim Generieren des Petri-Netzes: {exception}")