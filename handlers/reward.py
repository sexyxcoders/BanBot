from pyrogram import filters
from bot import app
from database.users import get_user
from keyboards.reward import reward_keyboard
from utils.constants import MIN_REFERRALS

@app.on_callback_query(filters.regex("^reward$"))
async def reward_handler(_, q):
    user = get_user(q.from_user.id)

    if user["referrals"] < MIN_REFERRALS:
        await q.message.reply(
            f"❌ You need {MIN_REFERRALS} referrals.\n"
            f"📊 Current: {user['referrals']}/{MIN_REFERRALS}"
        )
        return

    await q.message.reply(
        "🎁 **Choose Reward Category**",
        reply_markup=reward_keyboard
    )