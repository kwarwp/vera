# vera.heather.main.py
from _spy.vitollino.main import Cena, STYLE, Texto, Elemento
#from elemento.main import Elemento
STYLE["width"] = 600
STYLE["height"] = "600px"
JARRA = "https://i.imgur.com/gdiuQ9G.jpg"
BICHO = "https://i.imgur.com/7JW6fup.jpg"
CENA_PARQUE = "https://i.imgur.com/woKKIiA.jpg"
CRIANCA = "https://i.imgur.com/siqpEvJ.png"
UMTEXTO = "Eu gosto de geléia de uva!"
TEXTOMEL = "Eu gosto de mel!"

class Crianca:
    def __init__(self, parque, tit="maria", x=0, y=420):
        self.parque, self.tit = parque, tit
        escolhas = {"geleia de uva": self.uva, "jarra de mel": self.mel}
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=140,
        h=280, drop=escolhas, style={"opacity":0.3})
        crianca.entra(parque)
        
    def uva(self, _):
        texto = Texto(self.parque, UMTEXTO)
        texto.vai()
        
    def mel(self, _):
        texto = Texto(self.parque, TEXTOMEL)
        texto.vai()
        

class Esquilo:
    def __init__(self, parque):
        bicho = Elemento(BICHO, tit="esquilo", x=400, y=360, w=120, h=80)
        bicho.entra(parque)

class Jarra:
    def __init__(self, parque, tit="jarra de mel", x=300, y=400):
        jarra = Elemento(JARRA, tit=tit, x=x, y=y, w=120, h=80, drag=True)
        jarra.entra(parque)

class JogoEsquilo:
    def __init__(self):
        parque = Cena(CENA_PARQUE)
        Esquilo(parque)
        Crianca(parque)
        Crianca(parque, tit="julia", y=200)
        Crianca(parque, tit="zeca", x=160, y=200)
        Jarra(parque)
        Jarra(parque, tit="geleia de uva", x=460, y=460)
        parque.vai()
        
JogoEsquilo()

