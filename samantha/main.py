# vera.teacher.main.py
from _spy.vitollino.main import Cena,STYLE, Texto
from elemento.main import Elemento
STYLE["width"] = 800
STYLE["height"] = "600px"
LETRA_A = "https://i.imgur.com/sFciRzA.jpg"
LETRA_B = "https://i.imgur.com/IHu7zVe.jpg"
LETRA_C = "https://i.imgur.com/KDkL6Lg.jpg"
LETRA_D = "https://i.imgur.com/UHNmxA1.jpg"
LETRA_E = "https://i.imgur.com/lHMbjdZ.gif"
LETRA_F = "https://i.imgur.com/IcWkooX.jpg"
LETRA_G = "https://i.imgur.com/zGx2uSc.jpg"
LETRA_H = "https://i.imgur.com/naC6Wq3.jpg"
LETRA_I = "https://i.imgur.com/3X7JyD5.jpg"
LETRA_J = "https://i.imgur.com/N5yr7lF.jpg"
LETRA_K = "https://i.imgur.com/0PyUE7j.jpg"
LETRA_L = "https://i.imgur.com/suMPtAA.jpg"

CENA_PARQUE = "https://i.imgur.com/bPDwwQO.jpg"
CENA_CRIANCA = "https://i.imgur.com/hKFY2DF.png"
UMTEXTO = "Monte uma palavra, use sua criatividade"

class Crianca: 
    def __init__(self, parque, tit="joana", x=0, y=210):
        self.parque, self.tit = parque, tit
        escolhas = {"letra_a" : self.a, "letra a": self.a}
        crianca = Elemento(CENA_CRIANCA, tit=tit, x=x, y=y, w=70, h=140, drop=escolhas, style={"opacity":0.3})
        crianca.entra(parque)
        crianca.vai = self.a
        
    def a (self, _):
        texto = Texto (self.parque, UMTEXTO)
        texto.vai()
    
class JogoLetra:
    def __init__(self): 
        parque = Cena (CENA_PARQUE)
        letra_a = Elemento(LETRA_A, x=540, y=470, w=90, h=20, drag=True)
        letra_a.entra(parque)
        letra_b = Elemento(LETRA_B, x=250, y=250, w=20, h=30, drag=True)
        letra_b.entra(parque)
        letra_c = Elemento(LETRA_C, x=190, y=240, w=20, h=30, drag=True)
        letra_c.entra(parque)
        letra_d = Elemento(LETRA_D, x=140, y=250, w=20, h=30, drag=True)
        letra_d.entra(parque)
        letra_e = Elemento(LETRA_E, x=20, y=230, w=20, h=30, drag=True)
        letra_e.entra(parque)
        letra_f = Elemento(LETRA_F, x=40, y=195, w=10, h=30, drag=True)
        letra_f.entra(parque)
        letra_g = Elemento(LETRA_G, x=200, y=195, w=10, h=30, drag=True)
        letra_g.entra(parque)
        letra_H = Elemento(LETRA_H, x=100, y=195, w=10, h=30, drag=True)
        letra_H.entra(parque)
        letra_i = Elemento(LETRA_I, x=220, y=195, w=10, h=30, drag=True)
        letra_i.entra(parque)
        letra_j = Elemento(LETRA_J, x=240, y=195, w=10, h=30, drag=True)
        letra_j.entra(parque)
        letra_k = Elemento(LETRA_K, x=500, y=205, w=10, h=30, drag=True)
        letra_k.entra(parque)
        letra_l = Elemento(LETRA_L, x=350, y=210, w=20, h=30, drag=True)
        letra_l.entra(parque)
        Crianca(parque, tit="joana")
        parque.vai()
        
JogoLetra()
