# ineedblood
# ver hilos aleatorios de la first peich del general
import json
import urllib

@bot.message_handler(commands=['hilo'])
def command_hilofc(m):
    cid = m.chat.id
    link = urllib.urlopen("https://api.import.io/store/data/6c1e80a9-f46f-4947-ba94-87f734f3ff46/_query?input/webpage/url=http%3A%2F%2Fwww.forocoches.com%2Fforo%2Fforumdisplay.php%3Ff%3D2&_user=f95c0241-c58f-4cda-b57b-e275aaf2baf1&_apikey=f95c0241c58f4cdab57be275aaf2baf1e29290518c5369aee1d731c0cdebd0f3b13fa508f6a80c322dc9ce3332301957d10ace02a4594b189ea1a647375dc23b6472dcb0bdb9c8f0b28c19fb82a2739b")
    data = json.loads(link.read())
    rnd_no = random.randrange(0,30)
    thread_link = data['results'][rnd_no]['alt1td_link']
    thread_author =  data['results'][rnd_no]['smallfont_value']
    thread_title =   data['results'][rnd_no]['alt1td_link/_text']
    bot.send_message(cid, "***" + thread_author + "***\n" + thread_title + "\n" + thread_link)
