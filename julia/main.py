# vera.julia.main.py
from _spy.vitollino.main import Cena, STYLE
from elemento.main import Elemento #permite a movimentacao
STYLE["width"] = 900
STYLE["heigth"] = "900px"

#JARRA = "https://i.imgur.com/y2YyMOM.jpg"
PEIXE = "https://i.imgur.com/vZe20Rb.png"
PEIXEDOIS = "https://i.imgur.com/f6wJlKr.png"
PEIXETRES = "https://i.imgur.com/fgIlSq6.png"
PEIXEQUATRO = "https://i.imgur.com/Un7iN4l.png"
PEIXECINCO = "https://i.imgur.com/GmFMkTN.png"
PEIXESEIS = "https://i.imgur.com/iNLjvGR.png"
PEIXESETE = "https://i.imgur.com/4S6WTdR.png"
PEIXEOITO = "https://i.imgur.com/BShIuNz.png"
PEIXENOVE ="https://i.imgur.com/6oYFYlc.png"
PEIXEDEZ = "https://i.imgur.com/ykpgYSP.png"
CENA_PESCARIA = "https://i.imgur.com/KQbnPXQ.jpg"
CRIANCA = "https://i.imgur.com/U8kaaKl.jpg" #torna a crianca da imagem clicavel
BALDE = "https://i.imgur.com/U8kaaKl.jpg"

class Peixe:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe2:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXEDOIS, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe3:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXETRES, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe4:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXEQUATRO, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe5:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXECINCO, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe6:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXESEIS, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe7:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXESETE, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe8:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXEOITO, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe9:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXENOVE, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)


class Peixe10:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXEDEZ, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

#class Balde: caso precise de um balde clicavel
#    def __init__(self, pescaria, x=350, y=200): #tit quando arrastar o mouse em cima, surge o nome
#        balde = Elemento(BALDE, x=x, y=y, w=100, h=100, style={"opacity": 0.3})
#        balde.entra(pescaria)
        
class Crianca:
    def __init__(self, pescaria, tit="tiago", x=350, y=200): #tit quando arrastar o mouse em cima, surge o nome
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=100, h=100, style={"opacity": 0})
        crianca.entra(pescaria)
        
#class Jarra:
#    def __init__(self, pescaria, x=150, y=230):
#        jarra = Elemento(JARRA, x=x, y=y, w=60, h=40, drag=True) #drag permite arrastar o objeto para outro
#        jarra.entra(pescaria)

class jogoPescaria:
    def __init__(self):
        pescaria = Cena(CENA_PESCARIA)
        Peixe(pescaria, x=550, y=500)
        Peixe2(pescaria, x=280, y=505)
        Peixe3(pescaria, x=560, y=430)
        Peixe4(pescaria, x=460, y=430)
        Peixe5(pescaria, x=400, y=470)
        Peixe6(pescaria, x=280, y=505)
        Peixe7(pescaria, x=480, y=505)
        Peixe8(pescaria, x=380, y=305)
        Peixe9(pescaria, x=400, y=405)
        Peixe10(pescaria, x=450, y=430)
        #Jarra(pescaria)
        #Jarra(pescaria, x=200, y=230)
        Crianca(pescaria, tit="julia", x=720, y=250)
        Crianca(pescaria, tit="marcos", x=180, y=280)
        pescaria.vai()

jogoPescaria()