from database.mongo import requests_col
from datetime import datetime

def create_request(user_id: int):
    if requests_col.find_one({"user_id": user_id, "status": "pending"}):
        return False

    requests_col.insert_one({
        "user_id": user_id,
        "status": "pending",
        "created_at": datetime.utcnow()
    })
    return True

def approve_request(user_id: int):
    requests_col.update_one(
        {"user_id": user_id},
        {"$set": {"status": "approved"}}
    )

def reject_request(user_id: int):
    requests_col.update_one(
        {"user_id": user_id},
        {"$set": {"status": "rejected"}}
    )

def get_pending_requests():
    return list(requests_col.find({"status": "pending"}))
