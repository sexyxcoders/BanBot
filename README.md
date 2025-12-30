# 🤖 Referral Telegram Bot

A Telegram bot with a **referral reward system** built using **Pyrogram** and **MongoDB**, deployable on **Heroku**.

---

## 🚀 Features

- 💰 ₹5 per referral
- 🎯 Reward unlock at 5 referrals
- 🎁 Reward categories:
  - Telegram Premium
  - Stars ⭐
  - Profile / Gifts
- 🎬 Animated request confirmation
- 👮 Admin approve / reject system
- ⏰ 24-hour warning → @NexaMeetup
- 🧾 MongoDB-based persistent storage
- ☁️ Heroku ready

---

## 📂 Project Structure
ReferralBot/ ├── bot.py ├── config.py ├── Procfile ├── runtime.txt ├── requirements.txt ├── README.md ├── handlers/ ├── keyboards/ ├── database/ ├── utils/ ├── assets/ └── logs/
Copy code

---

## ⚙️ Environment Variables (Heroku)

Set these in **Heroku → Settings → Config Vars**
API_ID        = your_api_id API_HASH      = your_api_hash BOT_TOKEN     = your_bot_token MONGO_URI     = mongodb+srv://... DB_NAME       = ReferralBot ADMINS        = 123456789,987654321 ADMIN_GROUP   = -100xxxxxxxxxx
