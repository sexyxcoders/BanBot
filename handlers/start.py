from pyrogram import filters
from pyrogram.types import Message

from bot import app
from database.users import add_user, add_referral
from keyboards.main import main_menu


@app.on_message(filters.private & filters.command("start"))
async def start_cmd(_, message: Message):
    user_id = message.from_user.id
    add_user(user_id)

    # referral handling
    if len(message.command) > 1:
        try:
            ref_id = int(message.command[1])
            if ref_id != user_id:
                add_referral(ref_id)
        except:
            pass

    await message.reply_text(
        "👋 **Welcome to Referral Bot**\n\n"
        "💰 Earn ₹5 per referral\n"
        "🎁 Get rewards after 5 referrals",
        reply_markup=main_menu()
    )