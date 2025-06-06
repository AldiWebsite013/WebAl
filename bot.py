import asyncio
import sqlite3
import time
from telethon import TelegramClient, events

API_ID = 24576633  # <- Ganti
API_HASH = '29931cf620fad738ee7f69442c98e2ee'  # <- Ganti
BOT_TOKEN = '7607348783:AAE8cpofF-xp05tC8tjJtMve_HRlM0cTtyM'  # <- Ganti
YOUR_VPS_IP = "134.209.219.210"

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
