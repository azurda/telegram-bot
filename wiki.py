import wikipedia 

@bot.message_handler(commands=['wiki'])
def command_wiki(m):
    cid = m.chat.id 
    msg = m.text[6:]
  
    bot.send_message(cid,wikipedia.summary(msg, sentences=2))
