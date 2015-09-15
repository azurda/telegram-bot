@bot.message_handler(commands=['torrent'])
def command_torrent(m):
    cid = m.chat.id
    token = m.text[9:]
    url = "http://kat.cr/json.php?q=" + token
    link = urllib.urlopen(url)
    data = json.loads(link.read())
    print data
    # [0]['title'] ['torrentLink'] ['seeds']
    results = data['list'][0]['title'] + "\n" + 'Seeds:' + str(data['list'][0]['seeds']) + "\n" + data['list'][0]['torrentLink'] + "\n" + data['list'][1]['title'] + "\n" + 'Seeds:' + str(data['list'][1]['seeds']) + "\n" + data['list'][1]['torrentLink'] + "\n" + data['list'][2]['title'] + "\n" + 'Seeds:' + str(data['list'][2]['seeds']) + "\n" + data['list'][2]['torrentLink']
    bot.send_message(cid, results)
