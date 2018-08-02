import sqlite3
import telebot
import time
from telebot import apihelper

apihelper.proxy = {'http':'socks5://195.201.93.4:1080'}

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
     id = bot.send_message(message.from_user.id,
                     "Добро пожаловать, " + message.from_user.first_name+".")
     # Конектимся к БД
     con = sqlite3.connect("C:/Users/mr. Hey/test.db")
     cur = con.cursor()
     # Считаем общее кол-во строк в нашей БД
     cur.execute("SELECT COUNT(id) FROM bot")
     lon = cur.fetchone()
     right = 0
     # Запускаем поиск по нашей базе данных
     for i in range(*lon):
         cur.execute("SELECT id FROM bot Where id={0}".format(i + 1))
         id1 = cur.fetchone()
         id1 = str(*id1)
         if id1 == id:
            right = 1
            break
     if right == 0:
         cur.execute('INSERT INTO bot(id) VALUES("' + id + '"')
         con.commit()
     con.close()

@bot.message_handler(content_types="text")
def use(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=0)
    user_markup.row('Вычесть поездку')


while True:
    try:
        bot.polling(none_stop=True, interval=0)

    except Exception as e:
        print("Ошибка подключения")
        time.sleep(10)

#