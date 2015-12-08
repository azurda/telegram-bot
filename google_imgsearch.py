@bot.message_handler(commands=['img'])
def command_img(m):
            cid = m.chat.id
            token = m.text.split(" ", 1)[1]
            token = token.encode('utf-8') 
            url = "https://www.googleapis.com/customsearch/v1?q=%s&cx{CXCODEHERE}&searchType=image&key={APIKEY}" % token
            link = urllib.urlopen(url)
            data = json.loads(link.read())
            rnd_no = random.randrange(0,4)
            image = urllib.URLopener()
            image.retrieve(data['items'][rnd_no]['link'], "tmp.jpg")
            bot.send_photo(cid, open( 'tmp.jpg', 'rb'))
