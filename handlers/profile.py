from pyrogram import filters
from bot import app
from database.users import get_user

@app.on_callback_query(filters.regex("^profile$"))
async def profile_handler(_, q):
    user = get_user(q.from_user.id)

    await q.message.reply(
        f"👤 **Your Profile**\n\n"
        f"🆔 ID: `{q.from_user.id}`\n"
        f"👥 Referrals: {user['referrals']}\n"
        f"💰 Balance: ₹{user['balance']}"
    )