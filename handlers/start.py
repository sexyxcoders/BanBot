from pyrogram import filters
from pyrogram.types import Message
from bot import app
from database.users import add_user, add_referral, get_user
from keyboards.main import main_menu

@app.on_message(filters.private & filters.command("start"))
async def start_cmd(_, message: Message):
    user_id = message.from_user.id

    # Add user if not exists
    add_user(user_id)

    # Handle referral code if provided
    if len(message.command) > 1:
        try:
            ref_id = int(message.command[1])
            if ref_id != user_id:
                add_referral(ref_id)
        except:
            pass

    user = get_user(user_id)
    referral_count = user.get("referrals", 0)
    balance = user.get("balance", 0)

    # Welcome message
    text = (
        f"👋 **Welcome to Referral Bot!**\n\n"
        f"💰 Earn ₹5 per referral.\n"
        f"🎯 You have **{referral_count} referrals**.\n"
        f"💵 Your balance: ₹{balance}\n\n"
        "🎁 After 5 referrals, request your reward!"
    )

    await message.reply_text(
        text,
        reply_markup=main_menu()
    )