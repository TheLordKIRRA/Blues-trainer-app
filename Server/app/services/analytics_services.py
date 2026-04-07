def calculate_total_minutes(sessions):
    return sum(s.duration_minutes for s in sessions)

def calculate_average_duration(sessions):
    return (
        sum(s.duration_minutes for s in sessions) / len(sessions)
        if sessions else 0
    )
