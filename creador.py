@bot.message_handler(commands=['creador'])
def command_iscreador(m):
    autorizado = UID
    cid = m.chat.id
    us = "NOMBRE"
    usermsg = m.from_user.first_name
    if(cid == autorizado or us == usermsg):
        bot.send_message(cid, 'oh gran %s mi creador')
    else:
        bot.send_message(cid, 'no eres mi craedor vete a la mierda')
