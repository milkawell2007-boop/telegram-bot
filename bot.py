import telebot
import time

TOKEN = '8673666660:AAFz6UelHonz6sMjXbnUnJ8ZVLYx11corLQ'

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
    if message.text and message.text.lower() == "созвать конченных":
        try:
            bot.send_message(message.chat.id, "начинаю созыв конченных")
            mention_text = " ".join(users)
            bot.send_message(message.chat.id, mention_text)
        except Exception as e:
            print(f"Ошибка при отправке: {e}")

while True:
    try:
        print("Бот работает...")
        bot.polling(none_stop=True, interval=1, timeout=20)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
