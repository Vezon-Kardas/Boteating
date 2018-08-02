import telebot
import datetime
import logging

TOKEN = "430611930:AAFIVPCEvgbf1paCeifOERGUajggAzSlYuQ"
bot = telebot.TeleBot(TOKEN)

logging.basicConfig(filename="log.log", level=logging.INFO)

def log(message,answer):
    logging.info("\n ---------------\n" + str(
        datetime.datetime.now()) + "\nСообщение от {0} {1}. (username = @{2}, id = {3}) \nCommand - {4}\n{5}".format(
        message.from_user.first_name,
        message.from_user.last_name,
        message.from_user.username,
        str(message.from_user.id),
        message.text,
        answer.text))
