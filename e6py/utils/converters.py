from datetime import datetime


def convert_timestamp(value):
    if isinstance(value, datetime):
        pass
    elif isinstance(value, str):
        return datetime.fromisoformat(value)
