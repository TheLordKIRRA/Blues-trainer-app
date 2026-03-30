from datetime import datetime, timedelta

def calculate_streak(sessions):
    if not sessions:
        return 0

    streak = 1
    sessions_sorted = sorted(sessions, key=lambda s: s.timestamp, reverse=True)

    for i in range(1, len(sessions_sorted)):
        prev = sessions_sorted[i - 1].timestamp.date()
        curr = sessions_sorted[i].timestamp.date()

        if prev - curr == timedelta(days=1):
            streak += 1
        else:
            break

    return streak
