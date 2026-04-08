import os
import telebot
import time
import threading
from flask import Flask

TOKEN = '8673666660:AAHoGsYm0R8XENa4Itm9kAroY7jyBjW2AcE'

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

users = [
    "@aukri",
    "@tealavne",
    "@neangeliina",
    "@wintrstrrr",
    "@snxjkks"
]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    print("ПРИШЛО СООБЩЕНИЕ:", message.text)

    if message.text and "созвать конченных" in message.text.lower():
        try:
            bot.send_message(message.chat.id, "начинаю созыв конченных")
            bot.send_message(message.chat.id, " ".join(users))
        except Exception as e:
            print(f"Ошибка: {e}")

def run_bot():
    print("БОТ ЗАПУЩЕН")
    while True:
        try:
            print("Polling start…")
            bot.polling(none_stop=True, interval=1, timeout=20)
        except Exception as e:
            print(f"Ошибка бота: {e}")
            time.sleep(5)
            
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=20)
        except Exception as e:
            print(f"Ошибка бота: {e}")
            time.sleep(5)

@app.route('/')
def home():
    return "Bot is alive"

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)