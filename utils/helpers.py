from datetime import datetime, timedelta

def now_utc():
    return datetime.utcnow()

def after_24_hours(time):
    return time + timedelta(hours=24)
