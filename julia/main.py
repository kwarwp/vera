# vera.julia.main.py
from _spy.vitollino.main import Cena, STYLE, INVENTARIO
from elemento.main import Elemento #permite a movimentacao
STYLE["width"] = 900
STYLE["heigth"] = "900px"

#JARRA = "https://i.imgur.com/y2YyMOM.jpg"
PEIXE_INV ="https://i.imgur.com/HXmgNzJ.jpg"
PEIXE_SALM = "https://i.imgur.com/AcTCoXY.png"
PEIXE_VERD1 = "https://i.imgur.com/9Q52391.png"
PEIXE_VERD2 = "https://i.imgur.com/uAjOtz2.png"
PEIXEROSA = "https://i.imgur.com/1JMWIAT.png"
PEIXE_AZULROXO = "https://i.imgur.com/8l90Llu.png"
PEIXE_CINZA = "https://i.imgur.com/P75bVuk.png"
PEIXE_ROSINHA = "https://i.imgur.com/MU3hEl6.png"
PEIXE_AZULARANJA ="https://i.imgur.com/ObSSnqI.png"
PEIXE_LARANJINHA = "https://i.imgur.com/pq5Xvav.png"
PEIXE_PRETOLARANJA = "https://i.imgur.com/zTPwzkP.png"
PEIXE_COLOR = "https://i.imgur.com/ikkrZ4G.png"
PEIXE_VERDINHO = "https://i.imgur.com/mJWpSdm.png"
CENA_PESCARIA = "https://i.imgur.com/KQbnPXQ.jpg"
CRIANCA = "https://i.imgur.com/U8kaaKl.jpg" #torna a crianca da imagem clicavel
BALDE = "https://i.imgur.com/U8kaaKl.jpg"

class Peixe:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_SALM, tit="peixe grande", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe2:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_VERD1, tit="peixe grande", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe3:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_VERD2, tit="peixe pequeno", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe4:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXEROSA, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe5:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_AZULROXO, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe6:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_CINZA, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe7:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_ROSINHA, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe8:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_AZULARANJA, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe9:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_LARANJINHA, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)


class Peixe10:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_PRETOLARANJA, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)

class Peixe11:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_COLOR, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        
class Peixe12:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_VERDINHO, x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        
class Balde: #baldes clicáveis
    def __init__(self, pescaria, nome="balde", tipo_peixe="peixe grande", x=350, y=200): #tit quando arrastar o mouse em cima, surge o nome
        balde = Elemento(BALDE, x=x, y=y, tit=nome, w=100, h=100, style={"opacity": 0.3},
        drop = {tipo_peixe: self.pesca})
        self.tipo = tipo_peixe
        balde.entra(pescaria)
        
    def pesca(self, a, b):
        peixe = Elemento(PEIXE_INV, tit=self.tipo)
        INVENTARIO.bota(peixe)
        
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
        INVENTARIO.inicia()
        Peixe(pescaria, x=550, y=500)
        Peixe2(pescaria, x=280, y=505)
        Peixe3(pescaria, x=560, y=430)
        Peixe4(pescaria, x=460, y=430)
        Peixe5(pescaria, x=420, y=470)
        Peixe6(pescaria, x=415, y=405)
        Peixe7(pescaria, x=480, y=505)
        Peixe8(pescaria, x=390, y=505)
        Peixe9(pescaria, x=620, y=465)
        Peixe10(pescaria, x=520, y=455)
        Peixe11(pescaria, x=320, y=490)
        Peixe12(pescaria, x=650, y=440)
        #Jarra(pescaria)
        #Jarra(pescaria, x=200, y=230)
        Balde(pescaria, nome="balde grande", tipo_peixe="peixe grande", x=285, y=380)
        Balde(pescaria, nome="balde pequeno", tipo_peixe="peixe pequeno", x=10, y=410)
        Balde(pescaria, x=720, y=480)
        Balde(pescaria, x=790, y=440)
        Crianca(pescaria, tit="marcos", x=180, y=280)
        Crianca(pescaria, tit="julia", x=720, y=250)
        pescaria.vai()

jogoPescaria()