import telebot
import config
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Fuck you,leather man')
@bot.message_handler(commands=['day'])
def day(message):
    bot.send_message(message.chat.id, f"Цитата дня: {config.f}")
    bot.send_sticker(message.chat.id, config.b)

bot.polling(none_stop = True)