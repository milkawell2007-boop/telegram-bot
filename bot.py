import telebot
import time

TOKEN = '8673666660:AAFHnC6rZAHJXUKBFx9sBnkvjZ6_7WbyA2s'

bot = telebot.TeleBot(TOKEN)

users = [
    "@aukri",
    "@tealavne",
    "@neangeliina",
    "@wintrstrrr",
    "@snxjkks"
]

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == "созвать конченных":
        bot.send_message(message.chat.id, "начинаю созыв конченных")
        mention_text = " ".join(users)
        bot.send_message(message.chat.id, mention_text)

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
        time.sleep(5)
