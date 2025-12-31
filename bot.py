import logging
from pyrogram import Client
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    MONGO_URI,
    DB_NAME
)
from database.mongo import init_db

# ─────────── LOGGING ───────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/bot.log"),
        logging.StreamHandler()
    ]
)

LOGGER = logging.getLogger(__name__)

# ─────────── BOT CLIENT ───────────
app = Client(
    name="ReferralBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    workers=50,
    in_memory=True
)

# ─────────── LOAD HANDLERS ───────────
def load_plugins():
    import handlers.start
    import handlers.menu
    import handlers.profile
    import handlers.refer
    import handlers.reward
    import handlers.request
    import handlers.feedback
    import handlers.admin

# ─────────── STARTUP ───────────
@app.on_startup()
async def startup():
    init_db(MONGO_URI, DB_NAME)
    load_plugins()
    LOGGER.info("✅ Referral Bot Started Successfully")

# ─────────── RUN ───────────
if __name__ == "__main__":
    LOGGER.info("🚀 Starting Referral Bot...")
    app.run()