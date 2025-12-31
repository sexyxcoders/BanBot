from pyrogram import filters
from bot import app
from database.users import add_user, add_referral
from keyboards.main import main_menu

@app.on_message(filters.private & filters.command("start"))
async def start(_, message):
    user_id = message.from_user.id
    add_user(user_id)
    await message.reply_text(
        "👋 Welcome to Referral Bot\n💰 Earn ₹5 per referral\n🎁 Get rewards after 5 referrals",
        reply_markup=main_menu()
    )