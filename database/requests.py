from database.mongo import requests
from datetime import datetime

def create_request(user_id: int) -> bool:
    if requests.find_one({"user_id": user_id, "status": "pending"}):
        return False

    requests.insert_one({
        "user_id": user_id,
        "status": "pending",
        "created_at": datetime.utcnow()
    })
    return True


def approve_request(user_id: int):
    requests.update_one(
        {"user_id": user_id, "status": "pending"},
        {"$set": {"status": "approved"}}
    )


def reject_request(user_id: int):
    requests.update_one(
        {"user_id": user_id, "status": "pending"},
        {"$set": {"status": "rejected"}}
    )


def has_pending_request(user_id: int) -> bool:
    return bool(requests.find_one({"user_id": user_id, "status": "pending"}))