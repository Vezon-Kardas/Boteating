import telebot
import sqlite3


TOKEN = "430611930:AAFIVPCEvgbf1paCeifOERGUajggAzSlYuQ"
bot = telebot.TeleBot(TOKEN)

def zavtrak(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Завтрак WHERE Завтрак='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
def garnir(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Гарнир WHERE Гарнир='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
def mico(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Мясное WHERE Мясное='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
def ovoch(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Овощи WHERE Овощи='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
def fruit(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Фрукты WHERE Фрукты='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
def slast(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Сладости WHERE Сладости='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
def sup(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Суп WHERE Суп='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
def napit(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute("DELETE FROM Напитки WHERE Напитки='"+name+"'")
    con.commit()
    bot.send_message(message.chat.id, "Блюдо успешно удалено")
    con.close()
