# vera.teacher.main.py
from _spy.vitollino.main import Cena,STYLE
from elemento.main import Elemento
STYLE["width"] = 800
STYLE["height"] = "600px"
LETRA_A = "https://i.imgur.com/sFciRzA.jpg"
LETRA_B = "https://i.imgur.com/IHu7zVe.jpg"
LETRA_C = "https://i.imgur.com/KDkL6Lg.jpg"
LETRA_D = "https://i.imgur.com/UHNmxA1.jpg"
LETRA_E = "https://i.imgur.com/lHMbjdZ.gif"
LETRA_F = "https://i.imgur.com/IcWkooX.jpg"
LETRA_G = ""
LETRA_H = ""
LETRA_I = ""
LETRA_J = ""
LETRA_K = ""
LETRA_L = ""

CENA_PARQUE = "https://i.imgur.com/bPDwwQO.jpg"
CENA_CRIANCA = "https://i.imgur.com/hKFY2DF.png"

class Crianca: 
    def __init__(self, parque, tit="joana", x=0, y=210):
        crianca = Elemento(CENA_CRIANCA, tit=tit, x=x, y=y, w=70, h=140, style={"opacity":0.3})
        crianca.entra(parque)
    
class JogoLetra:
    def __init__(self): 
        parque = Cena (CENA_PARQUE)
        letra_a = Elemento(LETRA_A, x=255, y=210, w=20, h=30)
        letra_a.entra(parque)
        letra_b = Elemento(LETRA_B, x=250, y=250, w=20, h=30)
        letra_b.entra(parque)
        letra_c = Elemento(LETRA_C, x=190, y=240, w=20, h=30)
        letra_c.entra(parque)
        letra_d = Elemento(LETRA_D, x=140, y=250, w=20, h=30)
        letra_d.entra(parque)
        letra_e = Elemento(LETRA_E, x=20, y=230, w=20, h=30)
        letra_e.entra(parque)
        letra_f = Elemento(LETRA_F, x=40, y=195, w=10, h=30)
        letra_f.entra(parque)
        Crianca(parque, tit="joana")
        parque.vai()
        
JogoLetra()
