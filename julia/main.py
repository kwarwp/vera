# vera.julia.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento #permite a movimentacao

JARRA = "https://i.imgur.com/y2YyMOM.jpg"
PEIXE1 = "https://i.imgur.com/Q1OaRaO.png"
PEIXE2 = "https://i.imgur.com/SfOAbaS.png"
CENA_PESCARIA = "https://imgur.com/GX8p3JC.jpg"

class jogoPescaria:
    def __init__(self):
        pescaria = Cena(CENA_PESCARIA)
        peixe1 = Elemento(PEIXE1, x=100, y=100, w=60, h=40)
        peixe1.entra(pescaria)
        peixe2=Elemento(PEIXE2, x=200, y=100, w=60, h=40)
        peixe2.entra(pescaria)
        jarra = Elemento(JARRA, x=150, y=200, w=60, h=40)
        jarra.entra(pescaria)
        jarra_b = Elemento(JARRA, x=230, y=230, w=60, h=40)
        jarra_b.entra(pescaria)
        pescaria.vai()

jogoPescaria()