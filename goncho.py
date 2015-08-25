import telebot
from telebot import types 
import time
import datetime
import random

TOKEN = 'TOKEN' 
 
bot = telebot.TeleBot(TOKEN) 
 
def listener(messages): 
    for m in messages: 
        cid = m.chat.id 
        print "[" + str(cid) + "]: " + m.text 
 
bot.set_update_listener(listener) 
bot.polling(none_stop=True) 

while True: 
    time.sleep(300) 
