@bot.message_handler(commands=['repetir'])
def command_repetir(m):
    cid = m.chat.id
    for i in range(10):
        bot.send_message(cid, m.text[8:])
