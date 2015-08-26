@bot.message_handler(commands=['fecha'])
def command_fecha(m):
    cid = m.chat.id
    x = datetime.datetime.now()
    switcher = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre"
    }
    mes = switcher[x.month]
    fecha = "Estamos a %s de %s" % (x.day, mes)
    bot.send_message(cid, fecha)
