@bot.message_handler(commands=['imdb'])
def command_imdb(m):
    cid = m.chat.id
    token = m.text[6:]
    url = "http://www.omdbapi.com/?t=%s&y=&plot=short&r=json" % token
    link = urllib.urlopen(url)
    data = json.loads(link.read())
    image = urllib.URLopener()
    image.retrieve(data['Poster'], "imdb_tmp.jpg")
    bot.send_photo(cid, open( 'imdb_tmp.jpg', 'rb'))
    results = """*Titulo*: """ + data['Title'] + "\n" + """*Rating*: """ + "\n" +data['imdbRating'] + "\n" """*Argumento*: """ + data['Plot']
    bot.send_message(cid, results, parse_mode="Markdown")
