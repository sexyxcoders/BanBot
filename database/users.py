from database.mongo import get_db

def _col():
    return get_db()["users"]

def add_user(user_id: int):
    """Create user if not exists"""
    _col().update_one(
        {"_id": user_id},
        {
            "$setOnInsert": {
                "referrals": 0,
                "balance": 0,
                "joined": False
            }
        },
        upsert=True
    )

def get_user(user_id: int):
    user = _col().find_one({"_id": user_id})
    if not user:
        add_user(user_id)
        user = _col().find_one({"_id": user_id})
    return user

def add_referral(user_id: int):
    _col().update_one(
        {"_id": user_id},
        {"$inc": {"referrals": 1, "balance": 5}},
        upsert=True
    )

def mark_joined(user_id: int):
    _col().update_one(
        {"_id": user_id},
        {"$set": {"joined": True}},
        upsert=True
    )