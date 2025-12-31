from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🎁 Reward", callback_data="reward"),
                InlineKeyboardButton("👤 Profile", callback_data="profile")
            ],
            [
                InlineKeyboardButton("🔗 Refer", callback_data="refer"),
                InlineKeyboardButton("💬 Feedback", callback_data="feedback")
            ]
        ]
    )