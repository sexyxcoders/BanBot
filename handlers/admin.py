from pyrogram import filters
from bot import app
from config import ADMINS

@app.on_message(filters.command("approve") & filters.user(ADMINS))
async def approve(_, m):
    await m.reply("✅ Request approved")

@app.on_message(filters.command("reject") & filters.user(ADMINS))
async def reject(_, m):
    await m.reply("❌ Request rejected")
