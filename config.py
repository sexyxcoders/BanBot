import os

# ─── TELEGRAM BOT CONFIG ─────────────────────────────
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# ─── DATABASE CONFIG ─────────────────────────────────
MONGO_URI = os.getenv("MONGO_URI", "")
DB_NAME = os.getenv("DB_NAME", "ReferralBot")

# ─── ADMIN CONFIG ────────────────────────────────────
# Admin user IDs (comma separated in env)
ADMINS = list(map(int, os.getenv("ADMINS", "").split(","))) if os.getenv("ADMINS") else []

# Telegram group ID where requests are sent
ADMIN_GROUP = int(os.getenv("ADMIN_GROUP", 0))