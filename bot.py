import os
import telebot
from flask import Flask, request

TOKEN = '8673666660:AAH80TlEhV-gcVZ8jOR_BLUTAepwxd3J9qo'

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
    print("ПРИШЛО:", message.text)

    if message.text and "созвать конченных" in message.text.lower():
        bot.send_message(message.chat.id, "начинаю созыв конченных")
        bot.send_message(message.chat.id, " ".join(users))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/")
def home():
    return "Bot is alive"

if __name__ == "__main__":
    WEBHOOK_URL = f"https://telegram-bot-jcef.onrender.com/{TOKEN}"

    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)