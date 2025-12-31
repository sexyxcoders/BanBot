from pyrogram import Client, filters

API_ID = int("22657083")
API_HASH = "d6186691704bd901bdab275ceaab88f3"
BOT_TOKEN = "8527251945:AAE8Uc7VT_yQbCo0IL_uWWIChdn4nQWPizU"

app = Client("testbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.command("start"))
async def start(_, message):
    await message.reply_text("✅ Minimal bot is working!")

app.run()