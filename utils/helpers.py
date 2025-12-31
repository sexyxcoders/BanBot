from datetime import datetime, timedelta

def utc_now():
    return datetime.utcnow()

def after_24_hours(dt):
    return dt + timedelta(hours=24)