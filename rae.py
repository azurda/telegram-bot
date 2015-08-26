import json
import urllib

@bot.message_handler(commands=['rae'])
def command_rae(m):
     
      cid = m.chat.id
      msg = m.text[5:]
      link = urllib.urlopen("http://dulcinea.herokuapp.com/api/?query=" + msg)
      data = json.loads(link.read())
      for r in data['response']:
            if 'meanings' in r:
                bot.send_message(cid, data["response"][0]["meanings"][0]["meaning"])
                bot.send_message(cid, data["response"][1]["meanings"][0]["meaning"])
                break;
            else:
                bot.send_message(cid, "Error en la busqueda")
                break;
