import telebot
import sqlite3
import time
import gen
import log
import dell
import const
import database
import ssilki
import botan

TOKEN = "430611930:AAFIVPCEvgbf1paCeifOERGUajggAzSlYuQ"
bot = telebot.TeleBot(TOKEN)
botan_key = "1098cc40-60cb-4d85-a2f7-5e7f9066da02"

@bot.message_handler(commands=["start"])
def start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
    user_markup.row("Добавить блюдо", "Удалить блюдо")
    user_markup.row("Сгенерировать прием", "База рецептов")
    user_markup.row("Поиск в интернете", "Помощь")
    bot.send_message(message.from_user.id,
                     "Добро пожаловать, " + message.from_user.first_name+". Что нужно сделать?", reply_markup=user_markup)
    botan.track(const.botan_key, message.chat.id, message, "/start")
@bot.message_handler(commands=["help"])
def help(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=0)
    user_markup.row("Кнопка: Сгенерировать прием", "Кнопка: Добавить блюдо")
    user_markup.row("Кнопка: Удалить блюдо", "Кнопка: База данных")
    user_markup.row("To return to the main menu")
    answer = bot.send_message(message.from_user.id, "Правила использования бота. Выберите клавишу..", reply_markup=user_markup)
    bot.register_next_step_handler(answer, help1)


@bot.message_handler(content_types="text")
def gener(message):
    if message.text == "Поиск в интернете":
        keyboard = telebot.types.InlineKeyboardMarkup()
        url_button = telebot.types.InlineKeyboardButton(text="Найти рецепт в интернете", url="https://www.google.ru/")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "Нажмите на кнопку", reply_markup=keyboard)
    if message.text == "Помощь":
        help(message)
    if message.text == "Сгенерировать прием":
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
        user_markup.row("завтрак","перекус №1")
        user_markup.row("обед","перекус №2")
        user_markup.row("ужин","Return")
        bot.send_message(message.from_user.id,
                         "Выберите прием пищи, " + message.from_user.first_name+"...", reply_markup=user_markup)
    if message.text == "завтрак":
        gen.gen_breakfast(message)
    if message.text == "обед":
        gen.gen_lunch(message)
    if message.text == "ужин":
        gen.gen_dinner(message)
    if message.text == "перекус №1":
        gen.gen_per(message)
    if message.text == "перекус №2":
        gen.gen_per(message)
    if message.text == "Return":
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
        user_markup.row("Добавить блюдо", "Удалить блюдо")
        user_markup.row("Сгенерировать прием", "База рецептов")
        user_markup.row("Поиск в интернете", "Помощь")
        bot.send_message(message.from_user.id,
                         "Добро пожаловать, " + message.from_user.first_name+". Что нужно сделать?",
                         reply_markup=user_markup)
#--------------------------------------------------------------
    if message.text == "Добавить блюдо":
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
        user_markup.row("Завтрак", "Гарнир", "Мясо")
        user_markup.row("Фрукты", "Овощи", "Напитки")
        user_markup.row("Сладости", "Суп")
        user_markup.row("Return")
        bot.send_message(message.from_user.id, "Выберите категорию блюда, "+message.from_user.first_name+"...",
                         reply_markup=user_markup)
    if message.text == "Завтрак":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, zavtrak)
    if message.text == "Гарнир":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, garnir)
    if message.text == "Мясо":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, mic)
    if message.text == "Фрукты":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, freut)
    if message.text == "Овощи":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, ovoche)
    if message.text == "Напитки":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, napit)
    if message.text == "Суп":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, supch)
    if message.text == "Сладости":
        sent = bot.send_message(message.chat.id, "Введите название блюда...")
        bot.register_next_step_handler(sent, slasti)
#----------------------------------------------
    if message.text == "База рецептов":
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
        user_markup.row('Категория: Завтрак', "Категория: Гарнир", "Категория: Мясное")
        user_markup.row("Категория: Овощи", "Категория: Фрукты", "Категория: Сладости")
        user_markup.row("Категория: Супы", "Категория: Напитки", "Return")
        answer = bot.send_message(message.chat.id, "Выберите какую категорию вывести...", reply_markup=user_markup)
        log.log(message, answer)
    if message.text == "Категория: Завтрак":
        database.dtz(message)
    if message.text == "Категория: Гарнир":
        database.dtg(message)
    if message.text == "Категория: Мясное":
        database.dtm(message)
    if message.text == "Категория: Овощи":
        database.dto(message)
    if message.text == "Категория: Фрукты":
        database.dtf(message)
    if message.text == "Категория: Сладости":
        database.dts(message)
    if message.text == "Категория: Супы":
        database.dtc(message)
    if message.text == "Категория: Напитки":
        database.dtn(message)
#-------------------------------------------------------------
    if message.text == "Удалить блюдо":
        user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=1)
        user_markup.row(": завтрак", ": гарнир", ": мясное")
        user_markup.row(": напитки", ": суп", ": сладости")
        user_markup.row(": фрукты", ": овощи", "Return")
        bot.send_message(message.chat.id, "Выберете категорию блюда", reply_markup=user_markup)
    if message.text == ": завтрак":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.zavtrak)
    if message.text == ": гарнир":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.garnir)
    if message.text == ": мясное":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.mico)
    if message.text == ": напитки":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.napit)
    if message.text == ": суп":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.sup)
    if message.text == ": сладости":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.slast)
    if message.text == ": фрукты":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.fruit)
    if message.text == ": овощи":
        sent = bot.send_message(message.chat.id, "Введите точное название блюда...")
        bot.register_next_step_handler(sent, dell.ovoch)
#функции add------------------------------------------------------------------------------
def zavtrak(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Завтрак(Завтрак) VALUES("'+ name +'")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.zavtrak_ss1)
def garnir(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Гарнир(Гарнир) VALUES("' + name + '")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.garnir_ss1)
def mic(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Мясное(Мясное) VALUES("' + name + '")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.mic_ss1)
def freut(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Фрукты(Фрукты) VALUES("' + name + '")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.freut_ss1)
def ovoche(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Овощи(Овощи) VALUES("' + name + '")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.ovoche_ss1)
def napit(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Напитки(Напитки) VALUES("' + name + '")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.napit_ss1)
def supch(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Суп(Суп) VALUES("' + name + '")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.supch_ss1)
def slasti(message):
    name = message.text
    con = sqlite3.connect("C:/Users/mr. Hey/Еда.db")
    cur = con.cursor()
    cur.execute('INSERT INTO Сладости(Сладости) VALUES("' + name + '")')
    con.commit()
    con.close()
    answer = bot.send_message(message.chat.id, "Введите ссылку или рецепт...")
    bot.register_next_step_handler(answer, ssilki.slasti_ss1)
#--------------------------------------------------------------------
@bot.message_handler(content_types="text")
def help1(message):
    if message.text == "Кнопка: Сгенерировать прием":
        bot.send_message(message.chat.id, "При нажатии 'Сгенерировать прием', выберите какой прием пищи вам нужно сгенерировать,"
                                          "после этого вы получите от бота сообщение с вариантом блюд.")
        help(message)
    if message.text =="Кнопка: Добавить блюдо":
        bot.send_message(message.chat.id, "При нажатии 'Добавить блюдо', выберите категорию вносимого блюда."
                                          "Далее введите название этого блюда. Следующим шагом вам необходимо ввести рецепт вручную,"
                                          "либо скопировать и отправить боту ссылку на ваше блюдо. После этого"
                                          "блюдо будет успешно добавлено в базу и использовано в будущем")
        help(message)
    if message.text =="Кнопка: Удалить блюдо":
        bot.send_message(message.chat.id, "На данный момент разрешено удалять блюда только администраторам.")
        help(message)
    if message.text =="Кнопка: База данных":
        bot.send_message(message.chat.id, "Чтобы получить список тех или иных блюд в категориях(завтрак, гарнир, мясное"
                                          "и т.д.) нажмите 'База данных' и выберите интересующую вас категорию")
        help(message)
    if message.text =="To return to the main menu":
        start(message)

while True:
    try:
        bot.polling(none_stop=True, interval=0)

    except Exception as e:
        print("Ошибка подключения")
        time.sleep(10)