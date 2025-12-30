from database.users import get_user
from utils.constants import MIN_REFERRALS

def has_min_referrals(user_id: int) -> bool:
    user = get_user(user_id)
    return user["referrals"] >= MIN_REFERRALS
