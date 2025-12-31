from database.mongo import users
from datetime import datetime

def add_user(user_id: int):
    if users.find_one({"_id": user_id}):
        return

    users.insert_one({
        "_id": user_id,
        "referrals": 0,
        "referred_users": [],
        "balance": 0,
        "joined_at": datetime.utcnow()
    })


def get_user(user_id: int):
    user = users.find_one({"_id": user_id})
    if not user:
        add_user(user_id)
        user = users.find_one({"_id": user_id})
    return user


def add_referral(referrer_id: int, new_user_id: int):
    referrer = users.find_one({"_id": referrer_id})
    if not referrer:
        return False

    if new_user_id in referrer.get("referred_users", []):
        return False  # duplicate referral

    users.update_one(
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
    return True