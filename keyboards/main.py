from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_inline = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("📝 Feedback", callback_data="feedback"),
            InlineKeyboardButton("🎁 Reward", callback_data="reward")
        ],
        [
            InlineKeyboardButton("👤 Profile", callback_data="profile"),
            InlineKeyboardButton("👥 Refer", callback_data="refer")
        ]
    ]
)