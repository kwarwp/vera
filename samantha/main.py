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
LETRA_M = ""
LETRA_N = "https://2.bp.blogspot.com/-sOuJ1fO6Hxo/VzIz2wmQftI/AAAAAAAAHMg/ZyEAuVjdtg0SeK7l8aHdVMnsOSlZEduLwCPcBGAYYCw/s1600/letra-n.jpg"
LETRA_O = ""
LETRA_P = ""
LETRA_Q = ""
LETRA_R = "https://3.bp.blogspot.com/-f4OnzUCj1zg/VzI3ccy7XEI/AAAAAAAAHNE/uAUnW6QI2ZUvtspy7Sty_pZXw39tOfBggCPcBGAYYCw/s1600/letra-r.jpg"
LETRA_S = ""
LETRA_T = ""
LETRA_U = ""
LETRA_V = "https://images.casashops.com/Square620NoGrow/22625/alfabet-letra-v-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_W = ""
LETRA_X = ""
LETRA_Y = "https://images.casashops.com/Square620NoGrow/22628/alfabet-letra-y-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_Z = "https://i.pinimg.com/originals/09/2b/1b/092b1b58139077e41c0b804a61903529.jpg"

CENA_PARQUE = "https://i.imgur.com/bPDwwQO.jpg"
CENA_CRIANCA = "https://i.imgur.com/hKFY2DF.png"
UMTEXTO = "Monte uma palavra, use sua criatividade"

class Crianca: 
    def __init__(self, parque, tit="joana", x=400, y=470):
        self.parque, self.tit = parque, tit
        escolhas = {"letra_a" : self.a, "letra a": self.a}
        crianca = Elemento(CENA_CRIANCA, tit=tit, x=x, y=y, w=100, h=100, drop=escolhas, style={"opacity":0.1})
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
        letra_m = Elemento(LETRA_M, x=150, y=180, w=30, h=30, drag=True)
        letra_m.entra(parque)
        letra_n = Elemento(LETRA_N, x=250, y=190, w=20, h=30, drag=True)
        letra_n.entra(parque)
        letra_o = Elemento(LETRA_O, x=170, y=200, w=30, h=30, drag=True)
        letra_o.entra(parque)
        letra_p = Elemento(LETRA_P, x=240, y=185, w=20, h=30, drag=True)
        letra_p.entra(parque)
        letra_q = Elemento(LETRA_Q, x=200, y=180, w=15, h=30, drag=True)
        letra_q.entra(parque)
        letra_r = Elemento(LETRA_R, x=150, y=180, w=30, h=30, drag=True)
        letra_r.entra(parque)
        letra_s = Elemento(LETRA_S, x=200, y=220, w=20, h=30, drag=True)
        letra_s.entra(parque)
        letra_t = Elemento(LETRA_T, x=190, y=200, w=25, h=30, drag=True)
        letra_t.entra(parque)
        letra_u = Elemento(LETRA_U, x=250, y=175, w=30, h=30, drag=True)
        letra_u.entra(parque)
        letra_v = Elemento(LETRA_V, x=205, y=180, w=15, h=30, drag=True)
        letra_v.entra(parque)
        letra_w = Elemento(LETRA_W, x=185, y=200, w=35, h=30, drag=True)
        letra_w.entra(parque)
        letra_x = Elemento(LETRA_X, x=230, y=205, w=25, h=30, drag=True)
        letra_x.entra(parque)
        letra_y = Elemento(LETRA_Y, x=150, y=180, w=10, h=30, drag=True)
        letra_y.entra(parque)
        letra_z = Elemento(LETRA_Z, x=210, y=195, w=35, h=30, drag=True)
        letra_z.entra(parque)
        Crianca(parque, tit="joana")
        parque.vai()
        
JogoLetra()
