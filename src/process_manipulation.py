#-----------------------------------------------------------------------------
# Import
#-----------------------------------------------------------------------------

import pm4py

#-----------------------------------------------------------------------------
# Manipulate Event-Logs
#-----------------------------------------------------------------------------

def manipulate_event_logs(event_logs):

    try:
        net, initial_marking, final_marking = alpha_miner.apply(event_logs)
        return manipulated_event_logs
    except Exception as exception:
        raise ValueError(f"Fehler beim manipulieren der Event-Logs: {exception}")