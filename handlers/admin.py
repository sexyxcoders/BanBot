from pyrogram import filters
from bot import app
from database.requests import approve_request, reject_request
from utils.constants import APPROVED, REJECTED

@app.on_callback_query(filters.regex("^approve_"))
async def approve_handler(_, q):
    user_id = int(q.data.split("_")[1])
    approve_request(user_id)
    await q.message.edit("✅ Request approved.")

@app.on_callback_query(filters.regex("^reject_"))
async def reject_handler(_, q):
    user_id = int(q.data.split("_")[1])
    reject_request(user_id)
    await q.message.edit("❌ Request rejected.")