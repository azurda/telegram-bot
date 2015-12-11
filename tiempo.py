import json, urllib
# usage : /tiempo madrid
@bot.message_handler(commands=['tiempo'])
def command_tiempo(m):
    cid = m.chat.id
    token = m.text.split(" ", 1)[1]
    """This API returns the temperatures in Fahrenheits, so we'll need to change
    them in order to get them displayed in the system we are accustomed to"""
    url = "https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"%s\")&format=json&env=store://datatables.org/alltableswithkeys" % token
    link = urllib.urlopen(url)
    data = json.loads(link.read())
    tmp_min = (int(data['query']['results']['channel']['item']['forecast'][0]['high']) - 32) * 5.0/9.0
    tmp_max = (int(data['query']['results']['channel']['item']['forecast'][0]['low']) - 32) * 5.0/9.0
    custom_chain = """*Lugar*: """ + str(data['query']['results']['channel']['location']['city']) + """\n *Tiempo*: """ + str(data['query']['results']['channel']['item']['forecast'][0]['text']) + """\n *T.MAX*: """ + str(tmp_max) +  "º" + """\n *T.MIN* :""" + str(tmp_min) + "º" + """\n *Humedad*: """ + str(data['query']['results']['channel']['atmosphere']['humidity'] + "%")
    bot.send_message(cid, custom_chain, parse_mode="Markdown")
