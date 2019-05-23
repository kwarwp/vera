# vera.julia.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento #permite a movimentacao

JARRA = "https://i.imgur.com/y2YyMOM.jpg"
PEIXE = "https://i.imgur.com/4tDY3hD.png"
CENA_PESCARIA = "https://imgur.com/GX8p3JC.jpg"
CRIANCA = "https://i.imgur.com/U8kaaKl.jpg" #aproveitar os elementos da imagem, oval transparente, finge ser a crianca

class Peixe:
    def __init__(self, pescaria):
        peixe = Elemento(PEIXE, x=70, y=200, w=60, h=40)
        peixe.entra(pescaria)

class Crianca:
    def __init__(self, pescaria,x=0, y=230):
        crianca.Elemento(CRIANCA, x=x, y=y, w=70, h=140, style ={"opacity:10"}) #mascara tornando a imagem clicavel
        crianca.entra(pescaria)
        
class Jarra:
    def __init__(self, pescaria, x=150, y=230):
        jarra = Elemento(JARRA, x=x, y=y, w=60, h=40)
        jarra.entra(pescaria)

class jogoPescaria:
    def __init__(self):
        pescaria = Cena(CENA_PESCARIA)
        Peixe(pescaria)
        Jarra(pescaria)
        Jarra(pescaria, x=200, y=230)
        Crianca(pescaria)
        pescaria.vai()

jogoPescaria()