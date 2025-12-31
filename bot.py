import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# ─── LOGGING ─────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/bot.log"),
        logging.StreamHandler()
    ]
)

LOGGER = logging.getLogger(__name__)

# ─── PYROGRAM APP ────────────────────────────────────
app = Client(
    "ReferralBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# ─── LOAD HANDLERS ───────────────────────────────────
import handlers  # IMPORTANT: loads all handlers

# ─── START BOT ───────────────────────────────────────
if __name__ == "__main__":
    LOGGER.info("🚀 Referral Bot Started Successfully")
    app.run()