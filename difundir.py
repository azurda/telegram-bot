@bot.message_handler(commands=['all'])
def command_all(m):
    cid = m.chat.id
    administrador = ADMINID
    if cid != administrador: # Comprobamos que seamos nosotros quienes ejecutamos el comando
        bot.send_message( administrador, "El usuario con ID: " + str(cid) + " ha intentado utilizar el comando para enviar difundidos") # Si lo ejecuta otro, el bot nos avisará
    else: # Si somos nosotros...
        for ID in usuarios: # Por cada ID alamacenado en usuarios
            try: # Intentamos enviar el mensaje.
                bot.send_message( int(ID), m.text[4:])
            except: # Hacemos control de excepciones porque, si han borrado la conversación del bot o le han expulsado del grupo en el que estaba, se generará una excepción al intentar enviar el mensaje.
                bot.send_message( administrador, "Error enviando mensaje a: " + ID)
            else:
                bot.send_message( administrador, "Éxito enviando mensaje a: " + ID)
