from pyrogram import filters
from pyrogram.types import CallbackQuery
from bot import app

@app.on_callback_query()
async def callback_test(_, cq: CallbackQuery):
    await cq.answer("✅ Button clicked!", show_alert=True)