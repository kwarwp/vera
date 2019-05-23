# vera.julia.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento #permite a movimentacao

JARRA = "https://i.imgur.com/y2YyMOM.jpg"
PEIXE1 = "https://i.imgur.com/Q1OaRaO.png"
CENA_PESCARIA = "https://imgur.com/GX8p3JC.jpg"
pescaria = Cena(CENA_PESCARIA)
peixe1 = Elemento(PEIXE1, x=100, y=100, w=60, h=40)
peixe1.entra(pescaria)
jarra = Elemento(JARRA, x=100, y=100, w=60, h=40)
jarra.entra(pescaria)
jarra_b = Elemento (JARRA)
jarra_b.entra(pescaria)
pescaria.vai()
