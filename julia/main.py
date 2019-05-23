# vera.julia.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento #permite a movimentacao

JARRA = "https://i.imgur.com/y2YyMOM.jpg"
PEIXE = "https://i.imgur.com/4tDY3hD.png"
CENA_PESCARIA = "https://imgur.com/GX8p3JC.jpg"

class Peixe:
    def __init__(self, pescaria):
        peixe = Elemento(PEIXE, x=70, y=200, w=60, h=40)
        peixe.entra(pescaria)
        
class Jarra:
    def __init__(self, pescaria)
        jarra = Elemento(JARRA, x=150, y=230, w=60, h=40)
        jarra.entra(pescaria)

class jogoPescaria:
    def __init__(self):
        pescaria = Cena(CENA_PESCARIA)
        peixe = Elemento(PEIXE, x=70, y=200, w=60, h=40)
        peixe.entra(pescaria)
        jarra = Elemento(JARRA, x=150, y=230, w=60, h=40)
        jarra.entra(pescaria)
        jarra_b = Elemento(JARRA, x=230, y=230, w=60, h=40)
        jarra_b.entra(pescaria)
        pescaria.vai()

jogoPescaria()