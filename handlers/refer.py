from pyrogram import filters
from bot import app

@app.on_callback_query(filters.regex("^refer$"))
async def refer_handler(_, q):
    link = f"https://t.me/{app.username}?start={q.from_user.id}"
    await q.message.reply(
        f"👥 **Your Referral Link**\n\n{link}\n\n"
        "💸 Earn ₹5 per referral"
    )