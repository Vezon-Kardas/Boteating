import telebot
import sqlite3
import const
bot = telebot.TeleBot(const.TOKEN)

def dtz(message):
    y=[]
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Завтрак) FROM Завтрак")
    z = cur.fetchone()
    for i in range(1, int(*z)+1):
        cur.execute("SELECT Завтрак FROM Завтрак WHERE id="+str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "\n".join(y))

def dtg(message):
    y = []
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Гарнир) FROM Гарнир")
    z = cur.fetchone()
    for i in range(1, int(*z) + 1):
        cur.execute("SELECT Гарнир FROM Гарнир WHERE id=" + str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "\n".join(y))
def dtm(message):
    y = []
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Мясное) FROM Мясное")
    z = cur.fetchone()
    for i in range(1, int(*z) + 1):
        cur.execute("SELECT Мясное FROM Мясное WHERE id=" + str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "\n".join(y))
def dto(message):
    y = []
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Овощи) FROM Овощи")
    z = cur.fetchone()
    for i in range(1, int(*z) + 1):
        cur.execute("SELECT Овощи FROM Овощи WHERE id=" + str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "\n".join(y))
def dtf(message):
    y = []
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Фрукты) FROM Фрукты")
    z = cur.fetchone()
    for i in range(1, int(*z) + 1):
        cur.execute("SELECT Фрукты FROM еда WHERE id=" + str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "\n".join(y))
def dts(message):
    y = []
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Сладости) FROM Сладости")
    z = cur.fetchone()
    for i in range(1, int(*z) + 1):
        cur.execute("SELECT Сладости FROM Сладости WHERE id=" + str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "\n".join(y))
def dtc(message):
    y = []
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Суп) FROM Суп")
    z = cur.fetchone()
    for i in range(1, int(*z) + 1):
        cur.execute("SELECT Суп FROM Суп WHERE id=" + str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "-\n".join(y))
def dtn(message):
    y = []
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(Напитки) FROM Напитки")
    z = cur.fetchone()
    for i in range(1, int(*z) + 1):
        cur.execute("SELECT Напитки FROM Напитки WHERE id=" + str(i))
        x = cur.fetchone()
        y.append(*x)
    y.sort()
    bot.send_message(message.chat.id, "\n".join(y))