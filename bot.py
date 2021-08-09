import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands =['start'])
def displayKeyboard(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard = True)
    
    # display available answers as buttons
    for i in range(len(MOODLIST)):
        markup.row(types.KeyboardButton(MOODLIST[i]))

    bot.send_message(message.chat.id, "How do you feel?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handleUserInput(message):

    log = open("log.txt", 'a')
    log.write(str(len(MOODLIST) - MOODLIST.index(message.text) - 1) + '|')

    bot.send_message(message.chat.id, "Got it!")

bot.polling(none_stop=True)
