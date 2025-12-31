from database.mongo import get_db

def _col():
    return get_db()["referrals"]

def add_referral(inviter_id: int, invited_id: int):
    _col().insert_one({
        "inviter": inviter_id,
        "invited": invited_id
    })