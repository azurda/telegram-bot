@bot.message_handler(commands=['google'])
def command_google(m):
    cid = m.chat.id
    token = m.text[8:]
    url = "https://www.googleapis.com/customsearch/v1?q=%s&cx={CX TOKEN}&key={API_KEY}" % token
    link = urllib.urlopen(url)
    data = json.loads(link.read())
    
    results = data['items'][0]['title'] + "\n" + data['items'][0]['link']  + "\n" + data['items'][1]['title'] + "\n" + data['items'][1]['link']  + "\n" +     data['items'][2]['title'] + "\n" + data['items'][2]['link']  + "\n" 
    bot.send_message(cid, results)
