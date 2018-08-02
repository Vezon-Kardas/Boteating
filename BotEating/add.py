#Функции для добавления блюд
import sqlite3
import telebot
import ssilki
import const

bot = telebot.TeleBot(const.TOKEN)

@bot.message_handler(content_types=["text"])
def x1(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Завтрак(Завтрак) VALUES("'+ name +'")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    print("1")
    bot.register_next_step_handler(answer, ssilki.zavtrak_ss1)
    print("2")

def garnir(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Гарнир(Гарнир) VALUES("' + name + '")')
    con.commit()
    con.close()
    bot.send_message(message.chat.id, "Блюдо добавлено")
def mic(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Мясное(Мясное) VALUES("' + name + '")')
    con.commit()
    con.close()
    bot.send_message(message.chat.id, "Блюдо добавлено")
def freut(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Фрукты(Фрукты) VALUES("' + name + '")')
    con.commit()
    con.close()
    bot.send_message(message.chat.id, "Блюдо добавлено")
def ovoche(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Овощи(Овощи) VALUES("' + name + '")')
    con.commit()
    con.close()
    bot.send_message(message.chat.id, "Блюдо добавлено")
def napit(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Напитки(Напитки) VALUES("' + name + '")')
    con.commit()
    con.close()
    bot.send_message(message.chat.id, "Блюдо добавлено")
def supch(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Суп(Суп) VALUES("' + name + '")')
    con.commit()
    con.close()
    bot.send_message(message.chat.id, "Блюдо добавлено")
def slasti(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Сладости(Сладости) VALUES("' + name + '")')
    con.commit()
    con.close()
    bot.send_message(message.chat.id, "Блюдо добавлено")



