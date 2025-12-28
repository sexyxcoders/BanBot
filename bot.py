from pyrogram import Client
import config

app = Client(
    "ReferralBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

# Load handlers
import handlers.start
import handlers.menu
import handlers.profile
import handlers.refer
import handlers.reward
import handlers.request
import handlers.feedback
import handlers.admin

app.run()
