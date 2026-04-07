from datetime import datetime, timedelta, date
from typing import List, Tuple

def get_current_date() -> date:
    """Get the current date."""
    return datetime.utcnow().date()

def format_date(dt: datetime) -> str:
    """Format a datetime to ISO string."""
    return dt.isoformat()

def parse_date(date_str: str) -> datetime:
    """Parse an ISO date string to datetime."""
    return datetime.fromisoformat(date_str)

def get_date_range(start_date: date, end_date: date) -> List[date]:
    """Get a list of dates between start and end (inclusive)."""
    if start_date > end_date:
        return []
    return [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

def is_consecutive_dates(dates: List[date]) -> bool:
    """Check if a list of dates is consecutive."""
    if not dates:
        return True
    sorted_dates = sorted(set(dates))
    for i in range(1, len(sorted_dates)):
        if (sorted_dates[i] - sorted_dates[i-1]).days != 1:
            return False
    return True

def calculate_days_since(dt: datetime) -> int:
    """Calculate days since a given datetime."""
    return (datetime.utcnow() - dt).days

def get_week_start(dt: datetime) -> date:
    """Get the start of the week (Monday) for a given datetime."""
    return (dt - timedelta(days=dt.weekday())).date()