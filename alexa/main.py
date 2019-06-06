# vera.alexa.main.py
from _spy.vitollino.main import Cena,STYLE,Codigo
from elemento.main import Elemento 
STYLE["width"] = 600
STYLE["heigth"] = "600px"

LARANJA = "https://i.imgur.com/XXi1abd.png"
MACA = "https://i.imgur.com/8aCEBLc.png"
COELHO = "https://i.imgur.com/Tm65bCu.png"
PASSARINHO = "https://i.imgur.com/0BfAZQo.png"
PETECA = "https://i.imgur.com/bYAo3kt.png"
BOLA = "https://i.imgur.com/yUEgszl.png"
CENA_PARQUE = "https://i.imgur.com/kqWvogN.jpg"
CRIANCA = "https://i.imgur.com/j0ETf5x.jpg"
TENIS = "https://i.imgur.com/nwKWo8x.png"
GALOCHA = "https://i.imgur.com/JlGV4P8.png"

class Fruta:
    def __init__(self, parque,tit="maçã", imagem=MACA, x=200, y=200):
        maca = Elemento(imagem, tit=tit, x=x, y=y, w=70, h=40)
        maca.entra(parque)
class Esportes:  
    def __init__(self, parque,tit="bola", imagem=BOLA, x=100, y=200): 
        peteca = Elemento(imagem, tit=tit, x=x, y=y, w=50, h=50)
        peteca.entra(parque)
        #bola = Elemento(BOLA, x=100, y=200, w=80, h=60)
        #bola.entra(parque)
        
class Bicho:
    def __init__(self, parque, tit="coelho", imagem=COELHO, x=40, y=40):
        #coelho = Elemento(COELHO, x=100, y=100, w=60, h=40)
        #coelho.entra(parque)
        passarinho = Elemento(imagem, tit=tit, x=x, y=y, w=70, h=50)
        passarinho.entra(parque)
        
class Calcado:
    def __init__(self,parque, tit="tenis", imagem=TENIS, x=300, y=350):
        #tenis = Elemento(TENIS, x=150, y=210, w=50, h=80)
        #tenis.entra(parque)
        galocha = Elemento(imagem, tit=tit, x=x, y=y, w=60, h=50)
        galocha.entra(parque)
        
class Crianca:
    def __init__(self, parque, tit="crianca", x=0, y=210):
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=70, h=140, style={"opacity": 0.3})
        crianca.entra(parque)
        
class Conjuntos:
    def __init__(self):
        parque = Cena(CENA_PARQUE)
        nome = Codigo(codigo="", topo="PARQUE", style=dict(left=250, top=220, width=100, height="60px"))
        nome.entra(parque)
        Crianca(parque, tit="bicho", x=60, y=300)
        Crianca(parque, tit="esportes", x=150, y=300)
        Crianca(parque, tit="frutas", x=400, y=300) 
        Crianca(parque, tit="calcado", x=500, y=300)
        Fruta(parque, x=30, y=90)
        Fruta(parque, tit="laranja", imagem=LARANJA, x=330, y=60)
        Esportes(parque, x=100, y=150)
        Esportes(parque, tit="peteca", imagem=PETECA, x=500, y=35) 
        Bicho(parque, x=150, y=80)
        Bicho(parque, tit="passarinho", imagem=PASSARINHO, x=400, y=60)
        Calcado(parque, x=450, y=100) 
        Calcado(parque, tit="galocha", imagem=GALOCHA, x=200, y=50) 
        parque.vai()
        
Conjuntos()
