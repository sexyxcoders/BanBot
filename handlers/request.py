from pyrogram import filters
from bot import app
from assets.ascii import ANIMATION
from database.requests import create_request
from config import ADMIN_GROUP

@app.on_message(filters.command("request"))
async def request_reward(_, m):
    create_request(m.from_user.id)

    await m.reply(ANIMATION)

    await app.send_message(
        ADMIN_GROUP,
        f"🆕 **New Reward Request**\n\n"
        f"👤 User: {m.from_user.mention}\n"
        f"🆔 ID: `{m.from_user.id}`"
    )

    await m.reply(
        "⏳ Request sent.\n"
        "⏰ If not fulfilled in 24 hours,\n"
        "👉 Join @NexaMeetup"
    )
