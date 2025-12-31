import asyncio
from pyrogram import filters
from bot import app
from assets.ascii import FRAMES
from database.requests import create_request
from database.users import get_user
from keyboards.admin import admin_request_keyboard
from utils.constants import MIN_REFERRALS, WARNING_CHANNEL
from config import ADMIN_GROUP

@app.on_message(filters.command("request"))
async def request_handler(_, m):
    user_id = m.from_user.id
    user = get_user(user_id)

    if user["referrals"] < MIN_REFERRALS:
        await m.reply(
            f"❌ You need {MIN_REFERRALS} referrals to request reward."
        )
        return

    if not create_request(user_id):
        await m.reply("⏳ You already have a pending request.")
        return

    msg = await m.reply(FRAMES[0])
    for frame in FRAMES[1:]:
        await asyncio.sleep(0.7)
        await msg.edit(frame)

    await app.send_message(
        ADMIN_GROUP,
        text=(
            "🆕 **New Reward Request**\n\n"
            f"👤 User: {m.from_user.mention}\n"
            f"🆔 ID: `{user_id}`\n"
            f"👥 Referrals: {user['referrals']}"
        ),
        reply_markup=admin_request_keyboard(user_id)
    )

    await m.reply(
        "✅ Request submitted.\n\n"
        "⏰ If not fulfilled in 24 hours:\n"
        f"👉 {WARNING_CHANNEL}"
    )