@bot.message_handler(commands=['img'])
def command_img(m):
    cid = m.chat.id
    token = m.text[5:]
    token.encode('utf-8')
    #token = re.sub('[^0-9a-zA-Z]+', ' ', token)
    link = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + token)
    data = json.loads(link.read())
    rnd_no = random.randrange(0,4)
    image = urllib.URLopener()
    image.retrieve(data['responseData']['results'][rnd_no]['unescapedUrl'], "tmp.jpg")
    bot.send_photo(cid, open( 'tmp.jpg', 'rb'))
