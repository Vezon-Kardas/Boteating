#Добавление ссылок в бд
import sqlite3
import telebot
import const

bot = telebot.TeleBot(const.TOKEN)

def zavtrak_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Завтрак")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Завтрак SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")
def garnir_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Гарнир")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Гарнир SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")
def mic_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Мясное")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Мясное SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")
def freut_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Фрукты")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Фрукты SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")
def ovoche_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Овощи")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Овощи SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")
def napit_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Напитки")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Напитки SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")
def supch_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Суп")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Суп SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")
def slasti_ss1(message):
    print("3")
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("SELECT COUNT(id) FROM Сладости")
    a = cur.fetchone()
    print("4")
    cur.execute("UPDATE Сладости SET Ссылка='" + name + "' WHERE id=" + str(*a))
    con.commit()
    bot.send_message(message.from_user.id, "Блюдо добавлено")