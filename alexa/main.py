# vera.alexa.main.py
from _spy.vitollino.main import Cena,STYLE
from elemento.main import Elemento 
STYLE["width"] = 600
STYLE["heigth"] = "600px"

LARANJA = "https://i.imgur.com/rrX3OfV.png"
MACA = "https://i.imgur.com/xzBftDW.jpg"
COELHO = "https://i.imgur.com/yY22qoF.jpg"
PASSARINHO = "https://i.imgur.com/HZVP9am.jpg"
PETECA = "https://i.imgur.com/lkby3FK.jpg"
BOLA = "https://i.imgur.com/5KDBA8Z.jpg"
CENA_PARQUE = "https://i.imgur.com/kqWvogN.jpg"
CRIANCA = "https://i.imgur.com/j0ETf5x.jpg"
TENIS = "https://i.imgur.com/CZBRVIk.png"
GALOCHA = "https://i.imgur.com/9JmKVA4.jpg"

class Fruta:
    def __init__(self, parque,tit="maçã", imagem=MACA, x=150, y=200):
        maca = Elemento(imagem, tit=tit, x=x, y=y, w=60, h=40)
        maca.entra(parque)
class Esportes:  
    def __init__(self, parque,tit="bola", imagem=BOLA, x=100, y=200): 
        peteca = Elemento(imagem, tit=tit, x=x, y=y, w=50, h=40)
        peteca.entra(parque)
        bola = Elemento(BOLA, x=100, y=200, w=80, h=60)
        bola.entra(parque)
        
class Bicho:
    def __init__(self, parque, tit="coelho", imagem=COELHO, x=200, y=100):
        coelho = Elemento(COELHO, x=100, y=100, w=60, h=40)
        coelho.entra(parque)
        passarinho = Elemento(imagem, tit=tit, x=x, y=y, w=70, h=70)
        passarinho.entra(parque)
        
class Calcado:
    def __init__(self,parque, tit="tenis", imagem=TENIS, x=300, y=350):
        tenis = Elemento(TENIS, x=150, y=210, w=50, h=80)
        tenis.entra(parque)
        galocha = Elemento(imagem, tit=tit, x=x, y=y, w=80, h=50)
        galocha.entra(parque)
        
class Crianca:
    def __init__(self, parque, tit="crianca", x=0, y=210):
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=70, h=140, style={"opacity": 0.3})
        crianca.entra(parque)
        
class Conjuntos:
    def __init__(self):
        parque = Cena(CENA_PARQUE)
        Crianca(parque, tit="bicho", x=60, y=80)
        Crianca(parque, tit="esportes", y=100)
        Crianca(parque, tit="frutas", x=80, y=100) 
        Crianca(parque, tit="calcado", y=200)
        Fruta(parque, x=230, y=230)
        Fruta(parque, tit="laranja", imagem=LARANJA, x=330, y=230)
        Esportes(parque, x=200, y=150)
        Esportes(parque, tit="peteca", imagem=PETECA, x=250, y=200) 
        Bicho(parque, x=400, y=450)
        Bicho(parque, tit="passarinho", imagem=PASSARINHO, x=280, y=200)
        Calcado(parque, x=250, y=280) 
        Calcado(parque, tit="galocha", imagem=GALOCHA, x=350, y=320) 
        parque.vai()
        
Conjuntos()
