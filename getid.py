@bot.message_handler(commands=['getid'])
def command_getid(m):
    cid = m.chat.id
    bot.send_message(cid, str(m.chat.id) + " " + m.from_user.username )
