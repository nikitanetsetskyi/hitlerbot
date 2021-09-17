import telebot
import config
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Хаил Гитлер "+ message.from_user.first_name + ', меня  зовут Адольф Гитлер и я помогу тебе с изучением Германии')
    bot.send_sticker(message.chat.id, config.b)
@bot.message_handler(commands=['day'])
def day(message):
    bot.send_message(message.chat.id, f"Цитата дня: {config.f}")
@bot.message_handler(commands=[])
def evrey(message):
    bot.send_message(message.chat.id, "Скоро произойдет пожар в концлагере,но кто же выживет")
    bot.send_message(message.chat.id, "Но кто выживет,решать только тебе")
    bot.send_message(message.chat.id, "За кого ты?")

bot.polling(none_stop = True)