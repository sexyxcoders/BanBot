from pyrogram import filters
from bot import app
from keyboards.main import main_inline
from database.users import add_user, add_referral

@app.on_message(filters.command("start"))
async def start_handler(_, m):
    user_id = m.from_user.id
    add_user(user_id)

    if len(m.command) > 1:
        try:
            referrer = int(m.command[1])
            if referrer != user_id:
                add_referral(referrer, user_id)
        except:
            pass

    await m.reply(
        "👋 **Welcome to Referral Bot**\n\n"
        "💰 Earn ₹5 per referral\n"
        "🎯 5 referrals = Reward unlock",
        reply_markup=main_inline
    )