#-*- coding: utf8 -*-

from PIL import Image
from pytesseract import pytesseract
import logging
import sys
import time,json,os
from datetime import datetime
import random

import telebot
from telebot import types

API_TOKEN = 'TOKEN'

bot = telebot.TeleBot(API_TOKEN)
fileUsers = open("/test/vagina-bot/usersDB.json",'r+')
users = json.loads(fileUsers.read())
fileMsgs = open("/test/vagina-bot/messages.json",'r', encoding="utf-8")
messages = json.load(fileMsgs)
def info():
    return 'ВАЖНО! Если ты хочешь, чтобы участники твоего чата были в "долбоёбах,красавчиках и парах" дня, то добавь меня в беседу! Я не буду собирать никакой информации, честно! А тебе и участникам твоего чата смогу предоставить честную статистику.\n\nАвтор: @Pomorgite\nГитхаб: https://github.com/MrCheatEugene/vaginasize\nДанные обновляются в 00:00 по МСК.\nВнимание!\nБот создан только в развлекательных целях, все данные генерируются случайным образом. \nАвтор не преследует цели кого-то унизить или оскорбить.\nЛюбые совпадения случайны.';

def foolOfDay():
    return 'Фрик дня - '+open("/test/vagina-bot/foolOfDay",'r').readline()+". Поздравляем его!";

def pairOfDay():
    print("pOd called")
    print(open("/test/vagina-bot/pairOfDay",'r').readline())
    return 'Пара дня - '+(open("/test/vagina-bot/pairOfDay",'r').readline()).replace("{ANDSIGN}","и")+". Поздравляем их!";

def nicestOfDay():
    return 'Красавчик дня - '+open("/test/vagina-bot/nicestOfDay",'r').readline()+". Поздравляем его!";

def getStats(username):
    if(username in users and isinstance(users[username],list) and len(users[username]) >=5):
        updateUsers(fileUsers,users)
        if(len(users[username]) < 5 or str(users[username][4]) == "NONE"):
            symbols = 0
        else:
            symbols = users[username][4]
        if(len(users[username]) < 4 or str(users[username][3]) == "NONE"):
            messages = 0
        else:
            messages = users[username][3]
        if(len(users[username]) < 6 or str(users[username][5]) == "NONE"):
            photosAmount = 0
        else:
            photosAmount = users[username][5]
        if(len(users[username]) < 7 or str(users[username][6]) == "NONE"):
            videos = 0
        else:
            videos = users[username][6]
        if(len(users[username]) < 8 or str(users[username][7]) == "NONE"):
            stickers = 0
        else:
            stickers = users[username][7]
        if(len(users[username]) < 9 or str(users[username][8]) == "NONE"):
            voice = 0
        else:
            voice = users[username][8]
        if(len(users[username]) < 10 or str(users[username][9]) == "NONE"):
            audio = 0
        else:
            audio = users[username][9]
        return 'Настучал(а) символов: '+str(symbols)+'\nНаписал(а) сообщений:'+str(messages)+'\nСкинул(а) изображений: '+str(photosAmount)+'\nСкинул(а) видео: '+str(videos)+'\nСкинул(а) стикеров: '+str(stickers)+'\nЗаписал(а) голосовых сообщений: '+str(voice)+'\nСкинул(а) аудиофайлов: '+str(audio)
    else:
        return 'Статистика недоступна. Недостаточно данных.'

def updateUsers(fileUsers,users):
    fileUsers.close()
    os.remove("/test/vagina-bot/usersDB.json")
    os.mknod("/test/vagina-bot/usersDB.json")
    fileUsers = open("/test/vagina-bot/usersDB.json",'r+')
    fileUsers.write(json.dumps(users))
    fileUsers.close()
    fileUsers = open("/test/vagina-bot/usersDB.json",'r+')
    users = json.loads(fileUsers.read())
    return 0

def size(username):
    updateUsers(fileUsers,users)
    userinfo = users.get(username)

    size = ""
    numSize=0
    isMale =1
    #if (isinstance(userinfo,list) == False or len(userinfo) < 3 or (isinstance(userinfo,list) == True and len(userinfo) >=2 and ((userinfo[0] == 200 or userinfo[0] == "NONE") or (userinfo[1] == 200 or userinfo[1] == "NONE")))):
    #if (((isinstance(userinfo,list) == True and len(userinfo) >=3 and userinfo[1] == 200 or userinfo[0] == 200 or userinfo[1] == "NONE" or userinfo[0] == "NONE") or isinstance(userinfo,list) == True and len(userinfo) <3) or isinstance(userinfo,list) == False):

    if((isinstance(userinfo,list) == True and len(userinfo) >=3 and (userinfo[0] == 200 or userinfo[1] == 200 or userinfo[0] == "NONE" or userinfo[1] == "NONE"))):
        if(userinfo[0] == 200 or userinfo[0] == "NONE"):
            isMale = random.randint(1,100)%2
        if(userinfo[1] == 200 or userinfo[1] == "NONE"):
            if(isMale==1):
                numSize=random.randint(3,35)
            else:
                numSize=random.randint(10, 30)
        users[username][0]=isMale
        users[username][1]=numSize
        updateUsers(fileUsers,users)
    elif(isinstance(userinfo,list) == False):
        users[username]= []
        if(isMale==1):
            numSize=random.randint(3,35)
        else:
            numSize=random.randint(10, 30)
        isMale = random.randint(1,100)%2
        users[username].append(isMale)
        users[username].append(numSize)
        users[username].append(200)
        updateUsers(fileUsers,users)
    elif(isinstance(userinfo,list) == True and len(userinfo)>=3 and userinfo[0] != 200 or "NONE" and userinfo[1] != 200 or "NONE"):
        numSize = userinfo[1]
        isMale = userinfo[0]
    if(isMale == 1):
        size+="член длинной "
    else:
        size=size+"вагина глубиной "
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
def dochoice(array):
    return array[random.randint(0,len(array)-1)]
def test(username):
    updateUsers(fileUsers,users)
    userinfo = users.get(username)
    lines = 0
    if (((isinstance(userinfo,list) == True and len(userinfo) >=3 and userinfo[2] == 200) or isinstance(userinfo,list) == True and len(userinfo) <3) or isinstance(userinfo,list) == False):
        if(isinstance(userinfo,list) == False):
            print("random")
            users[username]= []
            users[username].append(200)
            users[username].append(200)
            users[username].append(lines)
            updateUsers(fileUsers,users)
        else:
            lines = random.randint(0,3)
            users[username][2] = lines
            updateUsers(fileUsers,users)
    if(isinstance(userinfo,list) == False):
        lines = random.randint(0,3)
        print("random")
        users[username]= []
        users[username].append(200)
        users[username].append(200)
        users[username].append(lines)
        updateUsers(fileUsers,users)
    elif(isinstance(userinfo,list) == True and len(userinfo) >=3 and userinfo[2] == 200):
        print("random")
        lines = random.randint(0,3)
        users[username][2] = lines
        updateUsers(fileUsers,users)
    elif(isinstance(userinfo,list)== True and len(userinfo) >= 3  and userinfo[2] < 5):
        lines= userinfo[2]
    linesMeaning= ""
    strLines = ""
    if(lines == 0):
        strLines="полосок"
        linesMeaning = str(dochoice(messages["zero"])).replace("*ник*","@"+username)
        #linesMeaning = "У @"+username+" не хватило денег на тест."
    elif(lines == 1):
        strLines="полоска"
        #linesMeaning = "@"+username+" скорее всего забеременел(а)."
        linesMeaning = str(dochoice(messages["one"])).replace("*ник*","@"+username)
    elif(lines == 2):
        strLines="полоски"
        if(users[username][0] == 1):
            hasCancer = "А блять, это мужик.. Здоровья."
        else:
            hasCancer = ""
        #linesMeaning = "@"+username+" забеременел(а). "+hasCancer
        linesMeaning = str(dochoice(messages["two"])).replace("*ник*","@"+username)+" "+hasCancer
    elif(lines== 3):
        strLines="полоски"
        #linesMeaning = "@"+username+" случайно обосрал тест. Теперь это сладкий хлебушек."
        linesMeaning = str(dochoice(messages["three"])).replace("*ник*","@"+username)
    #escapedmsg = str("У @"+username+" "+str(lines)+" "+strLines+". "+linesMeaning).replace("_", "\\_").replace("*", "\\*").replace("[", "\\[").replace("`", "\\`").replace(".", "\\.").replace("(", "\\(").replace(")", "\\)")
    escapedmsg = str("У @"+username+" "+str(lines)+" "+strLines+". "+linesMeaning)
    return escapedmsg
@bot.message_handler(commands=['size','test','info','nicestofday','foolofday','pairofday','stats','arctica'])
def send_welcome(message):
    updateUsers(fileUsers,users)
    if(message.from_user.is_bot == True):
        if not(message.from_user.username in users):
            users[message.from_user.username] = "unknown"
            updateUsers(fileUsers,users)
            print("NEW USER!")
    if(message.content_type == 'text' and message.text  == "/arctica"):
        if(message.chat.id == -1001696718262):
            bot.reply_to(message,text= "Последнее фото \"Кому мстить за арктику?\" ("+str(datetime.fromtimestamp(os.path.getmtime('/test/vagina-bot/arktica.jpg')).strftime("%d.%m.%Y %H:%M:%S"))+")")
            bot.send_photo(reply_to_message_id = message.id,photo=open('/test/vagina-bot/arktica.jpg','rb'),chat_id = -1001696718262)
        else:
            bot.reply_to(message,"Это локальная команда. Её нельзя использовать в других чатах. Сорян.")
    if(message.content_type == 'text' and message.text =="/size" or message.text =="/size@vagina_size_bot"):
        bot.reply_to(message, size(message.from_user.username))
    elif(message.content_type == 'text' and message.text=="/test" or message.text =="/test@vagina_size_bot"):
        bot.reply_to(message, test(message.from_user.username))
    elif(message.content_type == 'text' and message.text=="/info" or message.text =="/info@vagina_size_bot"):
        bot.reply_to(message, info())
    elif(message.content_type == 'text' and message.text=="/foolofday" or message.text =="/foolofday@vagina_size_bot"):
        bot.reply_to(message, foolOfDay())
    elif(message.content_type == 'text' and message.text=="/pairofday" or message.text =="/pairofday@vagina_size_bot"):
        bot.reply_to(message, pairOfDay())
    elif(message.content_type == 'text' and message.text=="/nicestofday" or message.text =="/nicestofday@vagina_size_bot"):
        bot.reply_to(message, nicestOfDay())
    elif(message.content_type == 'text' and message.text=="/stats" or message.text =="/stats@vagina_size_bot"):
        bot.reply_to(message, getStats(message.from_user.username))
@bot.inline_handler(lambda query: len(query.query) == 0)
@bot.inline_handler(lambda query: query.query == 'size')
def query_text(inline_query):
    updateUsers(fileUsers,users)
    if not(inline_query.from_user.username in users):
        users[inline_query.from_user.username] = "unknown"
        updateUsers(fileUsers,users)
        print("NEW USER!")
    commandsize = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'size',types.InputTextMessageContent(message_text = size(inline_query.from_user.username)), description = "Узнать свой размер вагины/члена")
    commandtest = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'test', types.InputTextMessageContent(message_text = test(inline_query.from_user.username)), description = "Тест на беременность")
    commandinfo = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'info', types.InputTextMessageContent(message_text = info()), description = "Немного инфы о ботике")
    commandnice = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'nicestOfDay',types.InputTextMessageContent(message_text = nicestOfDay()), description = "Красавчик дня")
    commandfool = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'foolOfDay',types.InputTextMessageContent(message_text = foolOfDay()), description = "Долбоёб дня")
    commandpair = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'pairOfDay',types.InputTextMessageContent(message_text = pairOfDay()), description = "Пара дня")
    commandstats = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'stats',types.InputTextMessageContent(message_text = getStats(inline_query.from_user.username)), description = "Срать подробно")
    bot.answer_inline_query(inline_query.id, [commandsize,commandtest,commandinfo,commandnice,commandfool,commandpair,commandstats], cache_time=1)
def default_query(inline_query):
    try:
         updateUsers(fileUsers,users)
         if not(inline_query.from_user.username in users):
             users[inline_query.from_user.username] = "unknown"
             updateUsers(fileUsers,users)
             print("NEW USER!")
         commandsize = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'size',types.InputTextMessageContent(message_text = size(inline_query.from_user.username)), description = "Узнать свой размер вагины/члена")
         commandtest = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'test', types.InputTextMessageContent(message_text = test(inline_query.from_user.username)), description = "Тест на беременность")
         commandinfo = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)), 'info', types.InputTextMessageContent(message_text = info()), description = "Немного инфы о ботике")
         commandnice = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'nicestOfDay',types.InputTextMessageContent(message_text = nicestOfDay()), description = "Красавчик дня")
         commandfool = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'foolOfDay',types.InputTextMessageContent(message_text = foolOfDay()), description = "Долбоёб дня")
         commandpair = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'pairOfDay',types.InputTextMessageContent(message_text = pairOfDay()), description = "Пара дня")
         commandstats = types.InlineQueryResultArticle(str(int(inline_query.id)+random.randint(0,999)),'stats',types.InputTextMessageContent(message_text = getStats(inline_query.from_user.username)), description = "Срать подробно")
         bot.answer_inline_query(inline_query.id, [commandsize,commandtest,commandinfo,commandnice,commandfool,commandpair,commandstats], cache_time=1)
    except Exception as e:
        print(e)

@bot.message_handler(func=lambda message: True)
def onmessage(message):
    updateUsers(fileUsers,users)
    if not(message.from_user.username in users and message.from_user.is_bot == True):if not(message.from_user.username in users and message.from_user.is_bot == True):
        users[message.from_user.username] = "unknown"
        updateUsers(fileUsers,users)
        print("NEW USER!")
    print(message.content_type)
    if not(isinstance(users[message.from_user.username],list)):
        users[message.from_user.username] = []

    if(len(users[message.from_user.username]) < 3):
        while (len(users[message.from_user.username]) <3):
            users[message.from_user.username].append(200)
            pass
    if(len(users[message.from_user.username]) >= 3):
        if(len(users[message.from_user.username]) >=4 and users[message.from_user.username][3]!= "NONE"):
            users[message.from_user.username][3] =users[message.from_user.username][3]+1;
        else:
            users[message.from_user.username].append(1)
        if(len(users[message.from_user.username]) >=5 and message.content_type == 'text' and users[message.from_user.username][4]!= "NONE"):
            users[message.from_user.username][4] =users[message.from_user.username][4]+len(message.text)
        elif(message.content_type == 'text'):       
            users[message.from_user.username].append(len(message.text))
    updateUsers(fileUsers,users)

@bot.message_handler(func=lambda message: True,content_types =['photo'] )
def processPhotos(message):
    updateUsers(fileUsers,users)
    if(len(users[message.from_user.username]) < 3):
        while (len(users[message.from_user.username]) <3):
            users[message.from_user.username].append(200)
            pass
    if(len(users[message.from_user.username]) >= 6 and users[message.from_user.username][5]!= "NONE"):
        users[message.from_user.username][5] = users[message.from_user.username][5]+1;
        updateUsers(fileUsers,users);
    elif(len(users[message.from_user.username]) < 6):
        while(len(users[message.from_user.username]) < 7):
            users[message.from_user.username].append(0)
        users[message.from_user.username].append(1)
        updateUsers(fileUsers,users);
    print("photo")
@bot.message_handler(func=lambda message: True,content_types =['sticker'] )
def processStickers(message):
    updateUsers(fileUsers,users)
    if(len(users[message.from_user.username]) < 3):
        while (len(users[message.from_user.username]) <3):
            users[message.from_user.username].append(200)
            pass
    if(len(users[message.from_user.username]) >= 8 and users[message.from_user.username][7]!= "NONE" ):
        users[message.from_user.username][7] = users[message.from_user.username][7]+1;
        updateUsers(fileUsers,users);
    elif(len(users[message.from_user.username]) < 8):
        while(len(users[message.from_user.username]) < 7):
            users[message.from_user.username].append(0)
        users[message.from_user.username].append(1)
        updateUsers(fileUsers,users);

@bot.message_handler(func=lambda message: True,content_types =['voice'] )
def processVoice(message):
    updateUsers(fileUsers,users)
    if(len(users[message.from_user.username]) < 3):
        while (len(users[message.from_user.username]) <3):
            users[message.from_user.username].append(200)
            pass
    if(len(users[message.from_user.username]) >= 9 and users[message.from_user.username][8]!= "NONE"):
        users[message.from_user.username][8] = users[message.from_user.username][8]+1;
        updateUsers(fileUsers,users);
    elif(len(users[message.from_user.username]) < 9):
        while(len(users[message.from_user.username]) < 8):
            users[message.from_user.username].append(0)
        users[message.from_user.username].append(1)
        updateUsers(fileUsers,users);

@bot.message_handler(func=lambda message: True,content_types =['audio'] )
def processMusic(message):
    if(len(users[message.from_user.username]) < 3):
        while (len(users[message.from_user.username]) <3):
            users[message.from_user.username].append(200)
            pass
    if(len(users[message.from_user.username]) >= 10 and users[message.from_user.username][9]!= "NONE"):
        users[message.from_user.username][9] = users[message.from_user.username][9]+1;
        updateUsers(fileUsers,users);
    elif(len(users[message.from_user.username]) < 10):
        while(len(users[message.from_user.username]) < 9):
            users[message.from_user.username].append(0)
        users[message.from_user.username].append(1)
        updateUsers(fileUsers,users);


@bot.message_handler(func=lambda message: True,content_types =['video','video_note'] )
def processVideos(message):
    updateUsers(fileUsers,users)
    if(len(users[message.from_user.username]) < 3):
        while (len(users[message.from_user.username]) <3):
            users[message.from_user.username].append(200)
            pass
    if(len(users[message.from_user.username]) >= 7 and users[message.from_user.username][6]!= "NONE"):
        users[message.from_user.username][6] = users[message.from_user.username][6]+1;
        updateUsers(fileUsers,users);
    elif(len(users[message.from_user.username]) < 7):
        while(len(users[message.from_user.username]) < 6):
            users[message.from_user.username].append(0)
        users[message.from_user.username].append(1)
        updateUsers(fileUsers,users);

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