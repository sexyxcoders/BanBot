from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

reward_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⭐ Telegram Premium", callback_data="reward_premium")
        ],
        [
            InlineKeyboardButton("🌟 Stars", callback_data="reward_stars")
        ],
        [
            InlineKeyboardButton("🎁 Profile / Gifts", callback_data="reward_gift")
        ],
        [
            InlineKeyboardButton("🔙 Back", callback_data="menu")
        ]
    ]
)
