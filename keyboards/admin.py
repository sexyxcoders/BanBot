from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_request_keyboard(user_id: int):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "✅ Approve",
                    callback_data=f"approve_{user_id}"
                ),
                InlineKeyboardButton(
                    "❌ Reject",
                    callback_data=f"reject_{user_id}"
                )
            ]
        ]
    )