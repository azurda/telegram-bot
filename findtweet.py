import tweepy 

@bot.message_handler(commands=['find'])
def command_find(m):
    cid = m.chat.id 
    x = tweepy.API(auth)
    msg = m.text[6:]
    for tweets in x.search(q=msg, count=3, result_type='recent'):
        bot.send_message(cid, "$" + tweets.user.screen_name + " $ " + tweets.text)
