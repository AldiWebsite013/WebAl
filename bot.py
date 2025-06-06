import asyncio
import sqlite3
import time
import os
from telethon import TelegramClient, events
from dotenv import load_dotenv

load_dotenv()  # Load dari .env

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
YOUR_VPS_IP = os.getenv("YOUR_VPS_IP")

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern=r'^/start\s*(\d+)?'))
async def start(event):
    user_id = event.sender_id
    arg = event.pattern_match.group(1)

    if not arg:
        await event.reply("Gunakan format: /start 30 (detik)")
        return

    duration = int(arg)
    start_time = int(time.time())

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO countdown (user_id, duration, start_time) VALUES (?, ?, ?)",
                (user_id, duration, start_time))
    conn.commit()
    conn.close()

    url = f"http://{YOUR_VPS_IP}:5000/timer/{user_id}"
    await event.reply(f"⏳ Countdown dimulai: {duration} detik\n\nLihat: {url}")

    await asyncio.sleep(duration)
    await bot.send_message(user_id, "⏰ Waktu kamu sudah habis!")

bot.run_until_disconnected()
