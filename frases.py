@bot.message_handler(commands=['miramacho']) #
def command_miramacho(m):
    cid = m.chat.id 
    numero = random.randrange(10)
    frases ={1:"Vas to burlao",
    2:"Zumo para prestar",
    3:"Pole",
    4:"me an robado el coche melon destrozado",
    5:"Mira macho vete a la mierda de verdad",
    6:"Contacto gym apuntate al 0",
    7:"Mi novia no es puta me lo ha dicho ella",
    8:"Hilitri paga el wifi primer aviso",
    9:"Ni con tu wifi"
    }
    mensaje = frases[numero]
    bot.send_message( cid, mensaje)
