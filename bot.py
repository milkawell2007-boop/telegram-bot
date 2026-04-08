import os
import telebot
import time
import threading
from flask import Flask

TOKEN = '8673666660:AAFz6UelHonz6sMjXbnUnJ8ZVLYx11corLQ'

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
    if message.text and message.text.lower() == "созвать конченных":
        try:
            bot.send_message(message.chat.id, "начинаю созыв конченных")
            mention_text = " ".join(users)
            bot.send_message(message.chat.id, mention_text)
        except Exception as e:
            print(f"Ошибка: {e}")

def run_bot():
    print("БОТ ПОШЁЛ В РАБОТУ")
    
    while True:
        try:
            print("Бот запущен")
            bot.polling(none_stop=True, interval=1, timeout=20)
        except Exception as e:
            print(f"Ошибка бота: {e}")
            time.sleep(5)

@app.route('/')
def home():
    return "Bot is alive"

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.start()
port = int(os.environ.get("PORT", 10000))
app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
