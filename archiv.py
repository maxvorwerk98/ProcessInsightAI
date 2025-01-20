
    with open("prompts/user_performance_prompt_2.txt", "r", encoding="utf-8") as file:
        user_performance_prompt_2 = file.read()

    event_logs_df = pm4py.convert_to_dataframe(event_logs)
    event_logs_df = event_logs_df.groupby('case:concept:name', as_index=False).first()

    event_logs_df['duration'] = None

    case_durations = pm4py.get_all_case_durations(
        event_logs,
        activity_key='concept:name',
        case_id_key='case:concept:name',
        timestamp_key='time:timestamp'
    )

    event_logs_df['duration'] = case_durations

    event_logs_df = event_logs_df.groupby('type_of_accident').agg({'duration': 'mean'}).reset_index()

#-----------------------------------------------------------------------------

    event_logs_df['service_time'] = event_logs_df.groupby('case:concept:name')['time:timestamp'].diff().shift(-1)


    average_service_time = event_logs_df.groupby("user_type")["service_time"].mean().reset_index()

    print(average_service_time)

#-----------------------------------------------------------------------------

    event_logs_df = pm4py.convert_to_dataframe(event_logs)
    event_logs_df = event_logs_df.groupby('case:concept:name', as_index=False).first()

    event_logs_df['duration'] = None

    case_durations = pm4py.get_all_case_durations(
        event_logs,
        activity_key='concept:name',
        case_id_key='case:concept:name',
        timestamp_key='time:timestamp'
    )

    event_logs_df['duration'] = case_durations

    filtered_df = event_logs_df[event_logs_df['duration'] > 50 * 24 * 60 * 60]