from gtts import gTTS

@bot.message_handler(commands=['voice'])
def command_voice(m):
    cid = m.chat.id 
    token = m.text.split(" ", 1)[1]
    tts = gTTS(text=token, lang='es')
    tts.save("tts.mp3")
    audio = open('tts.mp3', 'rb')
    bot.send_audio(cid, audio)
