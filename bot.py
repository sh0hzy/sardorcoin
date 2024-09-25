import telebot
from telebot import types

bot = telebot.TeleBot("token")

web_app_url = "t.me/hamstercombat_copy_bot/webapp"

text = "Yoyo! Qale bolla ? SardorCoinga xush kelibsila "

button = types.InlineKeyboardButton('Запустить', url=web_app_url)
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button)

@bot.message_handler(commands=['start'])
def send_message(message):
    bot.send_message(message.chat.id, text=text, reply_markup=keyboard)

bot.polling()
