import eel
import telebot

TOKEN = "7192661761:AAE1j1-m4XepTMYP6rdy7Zc12rgC014MqQ8"

bot  = telebot.TeleBot(TOKEN)

@eel.expose
def send_message(chat_id,message):
    bot.send_message(chat_id,message)
    return "Сообщение отправлено"

eel.init("web")
eel.start("index.html", mode="edge")