import urllib 
import json

@bot.message_handler(commands=['4chan'])
def command_4chan(m):
    cid = m.chat.id
    #msg = m.text[7:]    
    link = urllib.urlopen("http://a.4cdn.org/int/threads.json")
    data = json.loads(link.read())
    # print data 
    get_rnd_post = random.randrange(2,8)
    thread_id = data[0]['threads'][get_rnd_post]['no']
    print thread_id
    print "http://a.4cdn.org/int/thread/" + str(thread_id) + ".json"
    url = "http://a.4cdn.org/int/thread/" + str(thread_id) + ".json"
    thread_lnk = urllib.urlopen(url)
    post_data = json.loads(thread_lnk.read())
    hyperlink = "http://boards.4chan.org/int/thread/" + str(thread_id)
    bot.send_message(cid, post_data['posts'][0]['com'] + "\n" + hyperlink )
