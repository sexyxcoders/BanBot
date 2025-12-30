from pyrogram import filters
from bot import app

@app.on_callback_query(filters.regex("feedback"))
async def feedback(_, q):
    await q.message.reply("📝 Please send your feedback message.")
