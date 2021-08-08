import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands =['start'])
def displayKeyboard(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
    ans1 = types.KeyboardButton(config.ANSWERS[0])
    ans2 = types.KeyboardButton(config.ANSWERS[1])
    ans3 = types.KeyboardButton(config.ANSWERS[2])

    markup.add(ans1, ans2, ans3)

    bot.send_message(message.chat.id, "How do you feel?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handleUserInput(message):
    if message.text == config.ANSWERS[0]:
         bot.send_message(message.chat.id, "good")
    else:
         bot.send_message(message.chat.id, "also good")

bot.polling(none_stop=True)
