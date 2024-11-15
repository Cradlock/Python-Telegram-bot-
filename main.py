import telebot
import time
import sqlite3
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup
import requests
from bs4 import BeautifulSoup

Token = "7563115866:AAFYLn8fVp5INjDGVjJ9-QoAK78rYRV8FvI"
bot = telebot.TeleBot(token=Token)

users = []

global turn
turn = False

@bot.message_handler(commands=['activate'])
def start(message):
  global turn
  turn = True
  bot.send_message(message.chat.id,"Бот активен")

@bot.message_handler(commands=['deactivate'])
def deActivate(message):
  global turn
  turn = False
  bot.send_message(message.chat.id,"Бот выключен")

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, "Здраствуйте! Это бот помощник. \n Чем могу помочь?")
    
@bot.message_handler(func= lambda message: True)
def echo(mess):
    global turn
    print(turn)
    if turn:
     try:
       bot.reply_to(mess,eval(mess.text))
     except:
        if mess.text.strip()[0:7] == 'http://' or mess.text.strip()[0:8] == 'https://':
            bot.send_message(mess.chat.id,"ссылка сохранена")
    else:
      pass        
          
bot.polling(none_stop=True)