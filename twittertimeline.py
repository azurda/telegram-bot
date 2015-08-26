import tweepy

@bot.message_handler(commands=['gettl'])
def command_gettl(m):
    cid = m.chat.id
    x = tweepy.API(auth)
    for tweets in x.user_timeline(count=2):
        bot.send_message(cid, tweets.text)
