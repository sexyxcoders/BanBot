from pyrogram import filters
from bot import app
from keyboards.main import main_inline

@app.on_callback_query(filters.regex("^menu$"))
async def menu_handler(_, q):
    await q.message.edit(
        "🏠 **Main Menu**",
        reply_markup=main_inline
    )