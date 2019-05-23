# vera.heather.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento

JARRA = "https://i.imgur.com/gdiuQ9G.jpg"
BICHO = "https://i.imgur.com/7JW6fup.jpg"
CENA_PARQUE = "https://i.imgur.com/woKKIiA.jpg"
CRIANCA = "https://i.imgur.com/siqpEvJ.png"

class Crianca:
    def __init__(self, parque, tit="maria", x=0, y=210):
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=70,
        h=140, style={"opacity":0.3})
        crianca.entra(parque)

class Esquilo:
    def __init__(self, parque):
        bicho = Elemento(BICHO, x=190, y=180, w=60, h=40)
        bicho.entra(parque)

class Jarra:
    def __init__(self, parque, x=150, y=200):
        jarra = Elemento(JARRA, x=x, y=y, w=60, h=40)
        jarra.entra(parque)

class JogoEsquilo:
    def __init__(self):
        parque = Cena(CENA_PARQUE)
        Esquilo(parque)
        Crianca(parque)
        Crianca(parque, tit="julia", y=100)
        Crianca(parque, tit="zeca", x=80, y=100)
        Jarra(parque)
        Jarra(parque, x=230, y=230)
        parque.vai()
        
JogoEsquilo()

