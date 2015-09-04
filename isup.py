import re
import urlopen from urllib 

@bot.message_handler(commands=['isup'])
def command_isup(m):
    cid = m.chat.id
    domain = m.text[6:]
    resp = urllib.urlopen("http://www.isup.me/%s" % domain).read()
    if re.search("It's just you.", resp, re.DOTALL):
        bot.send_message(cid, "UP")
    else:
        bot.send_message(cid, "DOWN")
