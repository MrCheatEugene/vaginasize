# Вагина сайз бот
# Vagina size bot
# Требуется установить pytelegrambotapi 4.6.0.
# На строке 10 вписать вместо TOKEN токен бота.
from socket import NI_MAXHOST
import telebot
import random
import math

bot = telebot.TeleBot("TOKEN", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
@bot.message_handler(commands=['size','test'])
def send_welcome(message):
    if(message.content_type == 'text' and message.json['text']=="/size"):
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
        bot.reply_to(message, "У @"+message.from_user.username+" "+size+" см!")
    elif(message.content_type == 'text' and message.json['text']=="/test"):
        lines = random.randint(0,3)
        linesMeaning= ""
        strLines = ""
        if(lines == 0):
            strLines="полосок"
            linesMeaning = "@"+message.from_user.username+" пока не забеременел(а)."
        elif(lines == 1):
            strLines="полоска"
            linesMeaning = "@"+message.from_user.username+" скорее всего забеременел(а)."
        elif(lines == 2):
            strLines="полоски"
            linesMeaning = "@"+message.from_user.username+" забеременел(а). Уже "+str(random.randint(1,9))+" месяц! Или если "+"@"+message.from_user.username+" мужик, то вероятнее всего у него рак. F."
        elif(lines== 3):
            strLines="полоски"
            linesMeaning = "Что блять."
        bot.reply_to(message, "У @"+message.from_user.username+" "+str(lines)+" полоски. "+linesMeaning)
    pass
bot.infinity_polling()
