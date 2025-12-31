from database.mongo import get_db
from datetime import datetime

def _col():
    return get_db()["requests"]

def create_request(user_id: int, category: str = "unknown"):
    _col().insert_one({
        "user_id": user_id,
        "category": category,
        "status": "pending",
        "created_at": datetime.utcnow()
    })

def get_pending_requests():
    return list(_col().find({"status": "pending"}))

def approve_request(user_id: int):
    _col().update_one(
        {"user_id": user_id, "status": "pending"},
        {"$set": {"status": "approved", "updated_at": datetime.utcnow()}}
    )

def reject_request(user_id: int):
    _col().update_one(
        {"user_id": user_id, "status": "pending"},
        {"$set": {"status": "rejected", "updated_at": datetime.utcnow()}}
    )