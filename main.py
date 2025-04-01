import telebot

bot = telebot.TeleBot('7957879322:AAFrjKjK5MNxNnVWlwjEFMHTbGVKhgM0BxY')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Assalawma áleykum! Botimizǵa xosh kelipsiz")

bot.polling()

