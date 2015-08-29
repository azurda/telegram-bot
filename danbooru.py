@bot.message_handler(commands=['danbooru'])
def command_danbooru(m):
    cid = m.chat.id
    rnd_no_c = random.randrange(0,1)
    if(rnd_no_c == 0):
        link = urllib.urlopen("http://danbooru.donmai.us/explore/posts/popular.json")
    
        data = json.loads(link.read())
        rnd_no = random.randrange(0,18)
        img = urllib.URLopener()
        # bot.send_message(cid, data[rnd_no]['file_url'])
        img.retrieve("http://danbooru.donmai.us/"+ data[rnd_no]['file_url'], "danbooru_tmp.jpg")
        bot.send_photo(cid, open('danbooru_tmp.jpg', 'rb'))
    # tag_string_artist tag_string_character
        bot.send_message(cid, "Artist: " + data[rnd_no]['tag_string_artist'] + "\n Character: " + data[rnd_no]['tag_string_character'])
    else:
        link = urllib.urlopen("http://danbooru.donmai.us/posts.json")
        data = json.loads(link.read())
        rnd_no = random.randrange(0,18)
        img.retrieve("http://danbooru.donmai.us/"+ data[rnd_no]['file_url'], "danbooru_tmp.jpg")
        bot.send_photo(cid, open('danbooru_tmp.jpg', 'rb'))
        bot.send_message(cid, "Artist: " + data[rnd_no]['tag_string_artist'] + "\n Character: " + data[rnd_no]['tag_string_character'])
