from pyrogram import filters
from pyrogram.types import Message
from bot import app
from keyboards.main import main_inline
from database.users import add_user, add_referral

@app.on_message(filters.command("start"))
async def start(_, message: Message):
    user_id = message.from_user.id
    ref = None

    if len(message.command) > 1:
        ref = int(message.command[1])

    add_user(user_id)

    if ref and ref != user_id:
        add_referral(ref, user_id)

    await message.reply(
        "👋 **Welcome to Referral Bot**\n\n"
        "💰 Earn ₹5 per referral\n"
        "🎯 5 referrals = Reward unlock",
        reply_markup=main_inline
    )
