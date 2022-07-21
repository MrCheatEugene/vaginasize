import logging
import sys
import time,json,os
from datetime import datetime
import random

import telebot
from telebot import types

#img = Image. open(path_to_image)
#text = pytesseract. image_to_string(img)
#print(text)
API_TOKEN = 'ТОКЕН'

bot = telebot.TeleBot(API_TOKEN)
#telebot.logger.setLevel(logging.DEBUG)
fileUsers = open("usersDB.json",'r+')
users = json.loads(fileUsers.read())
# bot.download_file(bot.get_file(message.photo[-1].file_id).file_path)
def info():
    return 'ВАЖНО! Если ты хочешь, чтобы участники твоего чата были в "долбоёбах,красавчиках и парах" дня, то добавь меня в беседу! Я не буду собирать никакой информации, честно! А тебе и участникам твоего чата смогу предоставить честную статистику.\n\nАвтор: @Pomorgite\nГитхаб: https://github.com/MrCheatEugene/vaginasize\nДанные обновляются в 00:00 по МСК.\nВнимание!\nБот создан только в развлекательных целях, все данные генерируются случайным образом. \nАвтор не преследует цели кого-то унизить или оскорбить.\nЛюбые совпадения случайны.';

def foolOfDay():
    return 'Долбоёб дня - '+open("foolOfDay",'r').readline()+". Поздравляем его!";

def pairOfDay():
    return 'Пара дня - '+(open("pairOfDay",'r').readline()).replace("{ANDSIGN}","и")+". Поздравляем их!";

def nicestOfDay():
    return 'Красавчик дня - '+open("nicestOfDay",'r').readline()+". Поздравляем его!";

def getStats(username):
    if(username in users and len(users[username]) >=5):
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
    os.remove("usersDB.json")
    os.mknod("usersDB.json")
    fileUsers = open("usersDB.json",'r+')
    fileUsers.write(json.dumps(users))
    fileUsers.close()
    fileUsers = open("usersDB.json",'r+')
    users = json.loads(fileUsers.read())
    return 0

def size(username):
    print("used by "+username)
    userinfo = users.get(username)
    print(userinfo)

    size = ""
    numSize=0
    isMale =1
    if (isinstance(userinfo,list) == False or len(userinfo) < 3 or userinfo[0] == 200 or userinfo[1] == 200 ):
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
        users[username] = [];
        users[username].append(isMale)
        users[username].append(numSize)
        users[username].append(200)
        updateUsers(fileUsers,users)
    elif(isinstance(userinfo,list) and len(userinfo) >=3):
        numSize = userinfo[1]
        isMale = userinfo[0]
        if(isMale == 1):
            size+="член длинной "
        else:
            size=size+"вагина глубиной "
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
    userinfo = users.get(username)
    lines = 0
    if (isinstance(userinfo,list) == False or len(userinfo) < 3):
        lines = random.randint(0,3)
        if(isinstance(userinfo,list) == False):
            users[username]= []
        users[username].append(200)
        users[username].append(200)
        users[username].append(lines)
        updateUsers(fileUsers,users)
    elif(isinstance(userinfo,list) and len(userinfo) == 3  and userinfo[2] != 200):
        lines= userinfo[2]
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
@bot.message_handler(commands=['size','test','info','nicestofday','foolofday','pairofday','stats'])
def send_welcome(message):
    if not(message.from_user.username in users):
        users[message.from_user.username] = "unknown"
        updateUsers(fileUsers,users)
        print("NEW USER!")
    if(message.content_type == 'text' and message.text =="/size"):
        bot.reply_to(message, size(message.from_user.username))
    elif(message.content_type == 'text' and message.text=="/test"):
        bot.reply_to(message, test(message.from_user.username))
    elif(message.content_type == 'text' and message.text=="/info"):
        bot.reply_to(message, info())
    elif(message.content_type == 'text' and message.text=="/foolofday"):
        bot.reply_to(message, foolOfDay())
    elif(message.content_type == 'text' and message.text=="/pairofday"):
        bot.reply_to(message, pairOfDay())
    elif(message.content_type == 'text' and message.text=="/nicestofday"):
        bot.reply_to(message, nicestOfDay())
    elif(message.content_type == 'text' and message.text=="/stats"):
        bot.reply_to(message, getStats(message.from_user.username))
@bot.inline_handler(lambda query: len(query.query) == 0)
@bot.inline_handler(lambda query: query.query == 'size')
def query_text(inline_query):
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
    if not(message.from_user.username in users):
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
@bot.message_handler(func=lambda message: True,content_types =['sticker'] )
def processStickers(message):
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