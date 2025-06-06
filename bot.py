from telegram.ext import Updater, CommandHandler
import requests
import configs  # import file config.py

def start(update, context):
    if len(context.args) != 1:
        update.message.reply_text("Gunakan format: /start HH:MM:SS")
        return

    time_str = context.args[0]
    response = requests.post(f"{config.BACKEND_URL}?time={time_str}")
    
    if response.ok:
        update.message.reply_text(f"⏱️ Timer diset ke {time_str}")
    else:
        update.message.reply_text("Format salah atau terjadi kesalahan.")

def main():
    updater = Updater(config.BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
