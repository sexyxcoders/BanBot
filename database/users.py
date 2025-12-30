from database.mongo import users_col
from datetime import datetime

def add_user(user_id: int):
    if not users_col.find_one({"_id": user_id}):
        users_col.insert_one({
            "_id": user_id,
            "referrals": 0,
            "referred_users": [],
            "balance": 0,
            "joined": datetime.utcnow()
        })

def add_referral(referrer_id: int, new_user_id: int):
    user = users_col.find_one({"_id": referrer_id})
    if not user:
        return

    if new_user_id in user.get("referred_users", []):
        return  # prevent duplicate referral

    users_col.update_one(
        {"_id": referrer_id},
        {
            "$inc": {
                "referrals": 1,
                "balance": 5
            },
            "$push": {
                "referred_users": new_user_id
            }
        }
    )

def get_user(user_id: int):
    user = users_col.find_one({"_id": user_id})
    if not user:
        add_user(user_id)
        user = users_col.find_one({"_id": user_id})
    return user

def reset_referrals(user_id: int):
    users_col.update_one(
        {"_id": user_id},
        {"$set": {"referrals": 0, "balance": 0}}
    )
