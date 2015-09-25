@bot.message_handler(commands=['map'])
def command_map(m):
    cid = m.chat.id
    token = m.text.split(" ", 1)[1]
    token = token.encode('utf-8')
    url = "https://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=14&size=400x400&maptype=hybrid&key=AIzaSyBmZVQKUXYXYVpY7l0b2fNso4z82H5tMvE" % token
    urllib.urlretrieve(url, "map.png")
    bot.send_photo(cid, open( 'map.png', 'rb'))
