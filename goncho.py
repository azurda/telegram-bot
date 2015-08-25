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

@bot.message_handler(commands=['miramacho']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_miramacho(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    numero = random.randrange(10) # Generará un número aleatorio entre 1 y 10
    frases ={1:"Vas to burlao",
    2:"Zumo para prestar",
    3:"Pole",
    4:"me an robado el coche melon destrozado",
    5:"Mira macho vete a la mierda de verdad",
    6:"Contacto gym apuntate al 0",
    7:"Mi novia no es puta me lo ha dicho ella",
    8:"Hilitri paga el wifi primer aviso",
    9:"Ni con tu wifi"
    }
    mensaje = frases[numero]
    bot.send_message( cid, mensaje)



while True: 
    time.sleep(300) 
