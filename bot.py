from pyrogram import Client, filters

API_ID = int("YOUR_API_ID")
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

app = Client("testbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.command("start"))
async def start(_, message):
    await message.reply_text("✅ Minimal bot is working!")

app.run()