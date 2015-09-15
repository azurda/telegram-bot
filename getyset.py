import shelve

@bot.message_handler(commands=['set'])
def command_set(m):
    cid = m.chat.id
    token = m.text[5:]
    vars = shelve.open('variables.dat') # abrimos un archivo para asignar en el variables
    t1 = token.split(" ", 1)[0]
    t2 = token.split(" ", 1)[1]
    if t2 == "":
        bot.send_message(cid, "Uso: /set variable contenido")
    vars[t1.encode("utf-8")] = t2.encode("utf-8") # nos aseguramos de que haya un encoding que admita shelve
    bot.send_message(cid, 'Variable ' + token.split(" ", 1)[0] + ' registrada con exito')
    vars.close() # cerramos el objeto

@bot.message_handler(commands=['get'])
def command_get(m):
    cid = m.chat.id
    token = m.text[5:]
    vars = shelve.open('variables.dat')
    vars.sync() # sincronizamos el contenido 
    # comprobamos que existe el token 
    if token.encode("utf-8") in vars: 
        bot.send_message(cid, vars[token.encode("utf-8")])
    else:
        bot.send_message(cid, 'Variable no asignada')
        
    vars.close()
