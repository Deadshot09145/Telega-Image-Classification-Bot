import telebot
from ai_logic import get_class

token = "7932899940:AAEXCp7hON0NUcUi_kC-JGFy5ga87qDo6JQ"

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(content_types=['photo'])
def ai_class(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image/" +file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = get_class("image/" +file_name)
    bot.reply_to(message, result)

# Запускаем бота
bot.polling()