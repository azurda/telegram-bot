import urllib
import json

@bot.message_handler(commands=['yt'])
def command_youtube(m):
    cid = m.chat.id
    query = m.text[4:]
    # sustituir CLAVE API por tu API    
    link = urllib.urlopen("https://www.googleapis.com/youtube/v3/search?part=snippet&q=%s&key={CLAVE API}" % query)
    data = json.loads(link.read())
    rnd_no = random.randrange(0,3)
    id = data['items'][rnd_no]['id']['videoId'] 
    bot.send_message(cid, "http://www.youtube.com/watch?v=" + id)
    
