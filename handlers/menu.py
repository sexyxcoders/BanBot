from pyrogram import filters
from bot import app

@app.on_callback_query(filters.regex("menu"))
async def menu(_, q):
    await q.answer("Menu loaded")
