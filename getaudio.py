""" We will use a listener to check for incoming traffic continuosly,
you can intregrate it into a function instead of grabbing each audio file
received. You will still have to sort the issue of the audio name, that's easy :P"""

import urllib
TOKEN = "" # Token here
def listener(messages):
  for m in messages: 
    if m.audio != None:
      # Retrieve response from Telegram in order to obtain file_path
      link = urllib.urlopen("https://api.telegram.org/bot" + TOKEN + "/getFile?file_id=" + m.audio.file_id)
      data = json.loads(link.read())
      audio = urllib.URLopener()
      # Obtaining the file given the filepath.
      file = "https://api.telegram.org/file/bot" + TOKEN + "/" + data['result']['file_path']
      audio.retrieve(file, "audio.wav")
       
  
