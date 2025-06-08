from datetime import datetime


def parse_wmata_timestamp(value: str) -> datetime:
    """
    Convert WMATA's ISO8601 datetime string (with 'Z' suffix for UTC)
    into a Python datetime object.
    """
    return datetime.fromisoformat(value.replace("Z", "+00:00"))