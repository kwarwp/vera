# vera.alexa.main.py
from _spy.vitollino.main import Cena,STYLE
from elemento.main import Elemento 
STYLE["width"] = 600
STYLE["heigth"] = "600px"

MACA = "https://i.imgur.com/xzBftDW.jpg"
COELHO = "https://i.imgur.com/yY22qoF.jpg"
PETECA = "https://i.imgur.com/lkby3FK.jpg"
BOLA = "https://i.imgur.com/5KDBA8Z.jpg"
CENA_PARQUE = "https://i.imgur.com/kqWvogN.jpg"
CRIANCA = "https://i.imgur.com/j0ETf5x.jpg"

class Fruta:
    def __init__(self, parque, x=150, y=200):
        maca = Elemento(MACA, x=200, y=200, w=60, h=40)
        maca.entra(parque)
        
class Esportes:  
    def __init__(self, parque): 
        peteca = Elemento(PETECA, x=150, y=100, w=60, h=40)
        peteca.entra(parque)
        bola = Elemento(BOLA, x=100, y=200, w=80, h=60)
        bola.entra(parque)
        
class Bicho:
    def __init__(self, parque):
        coelho = Elemento(COELHO,  x=100, y=100, w=60, h=40)
        coelho.entra(parque)
        
class Crianca:
    def __init__(self, parque, tit="maria", x=0, y=210):
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=70, h=140, style={"opacity": 0.3})
        crianca.entra(parque)
        
class Conjuntos:
    def __init__(self):
        parque = Cena(CENA_PARQUE)
        Bicho(parque)
        Crianca(parque)
        Crianca(parque, tit="esportes", y=100)
        Crianca(parque, tit="frutas", x=80, y=100)       
        Fruta(parque, x=230, y=230)
        parque.vai()
        
Conjuntos()
