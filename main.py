import logging
import sys
import time
import random

import telebot
from telebot import types

API_TOKEN = 'token'

bot = telebot.TeleBot(API_TOKEN)
telebot.logger.setLevel(logging.DEBUG)

def info():
    return 'Автор: @Pomorgite\nГитхаб: https://github.com/MrCheatEugene/vaginasize'

def size(username):
    print("used by "+username)
    size = ""
    numSize=0
    isMale =1
    if(random.randint(1,100)%2 == 0):
        size+="член длинной "
        numSize=random.randint(3,35)
        isMale = 1
    else:
        size=size+"вагина глубиной "
        numSize=random.randint(10, 30)
        isMale=0
    pass
    size+=str(numSize)
    if(isMale == 0 and numSize < 13):
        size+=' 👍'
    elif(isMale == 0 and numSize > 13):
        size+=' 😳'
    elif(isMale == 0 and numSize > 20):
        size+=' 🤯'
    elif(isMale == 1 and numSize > 30):
        size+=' 🤯'
    elif(isMale == 1 and numSize > 20):
        size+=' 👍😊'
    elif(isMale == 1 and numSize > 15):
        size+=' 👍'
    elif(isMale == 1 and numSize < 15):
        size+=' 😔'
    elif(isMale == 1 and numSize < 10):
        size+=' 😢'
    elif(isMale == 1 and numSize < 5):
        size+=' 😭😭😭😭😭'
    else:
        size+=' 👍'
    pass
    return "У @"+username+" "+size+" см!"
def test(username):
    lines = random.randint(0,3)
    linesMeaning= ""
    strLines = ""
    if(lines == 0):
        strLines="полосок"
        linesMeaning = "У @"+username+" не хватило денег на тест."
    elif(lines == 1):
        strLines="полоска"
        linesMeaning = "@"+username+" скорее всего забеременел(а)."
    elif(lines == 2):
        strLines="полоски"
        linesMeaning = "@"+username+" забеременел(а). Уже "+str(random.randint(1,9))+" месяц! Или если "+"@"+username+" мужик, то вероятнее всего у него рак. F."
    elif(lines== 3):
        strLines="полоски"
        linesMeaning = "@"+username+" случайно обосрал тест. Теперь это сладкий хлебушек."
    #escapedmsg = str("У @"+username+" "+str(lines)+" "+strLines+". "+linesMeaning).replace("_", "\\_").replace("*", "\\*").replace("[", "\\[").replace("`", "\\`").replace(".", "\\.").replace("(", "\\(").replace(")", "\\)")
    escapedmsg = str("У @"+username+" "+str(lines)+" "+strLines+". "+linesMeaning)
    return escapedmsg
@bot.message_handler(commands=['size','test','info'])
def send_welcome(message):
    if(message.content_type == 'text' and message.text =="/size"):
        bot.reply_to(message, size(message.from_user.username))
    elif(message.content_type == 'text' and message.text=="/test"):
        bot.reply_to(message, test(message.from_user.username))
    elif(message.content_type == 'text' and message.text=="/info"):
        bot.reply_to(message, info())
@bot.inline_handler(lambda query: len(query.query) == 0)
@bot.inline_handler(lambda query: query.query == 'size')
def query_text(inline_query):
    commandsize = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'size',types.InputTextMessageContent(message_text = size(inline_query.from_user.username)), description = "Узнать свой размер вагины/члена")
    commandtest = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'test', types.InputTextMessageContent(message_text = test(inline_query.from_user.username)), description = "Тест на беременность")
    commandinfo = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'info', types.InputTextMessageContent(message_text = info()), description = "Немного инфы о ботике")
    bot.answer_inline_query(inline_query.id, [commandsize,commandtest,commandinfo], cache_time=1)
def default_query(inline_query):
    try:
         commandsize = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'size',types.InputTextMessageContent(message_text = size(inline_query.from_user.username)), description = "Узнать свой размер вагины/члена")
         commandtest = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'test', types.InputTextMessageContent(message_text = test(inline_query.from_user.username)), description = "Тест на беременность")
         commandinfo = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'info', types.InputTextMessageContent(message_text = info()), description = "Немного инфы о ботике")
         bot.answer_inline_query(inline_query.id, [commandsize,commandtest,commandinfo], cache_time=1)
    except Exception as e:
        print(e)


def main_loop():
    bot.infinity_polling()
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)