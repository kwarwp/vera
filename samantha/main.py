# vera.teacher.main.py
from _spy.vitollino.main import Cena,STYLE, Texto,INVENTARIO
from elemento.main import Elemento
STYLE["width"] = 1000
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
LETRA_M = "https://st3.depositphotos.com/1561359/12648/i/950/depositphotos_126487082-stock-photo-silver-letter-m.jpg7"
LETRA_N = "https://2.bp.blogspot.com/-sOuJ1fO6Hxo/VzIz2wmQftI/AAAAAAAAHMg/ZyEAuVjdtg0SeK7l8aHdVMnsOSlZEduLwCPcBGAYYCw/s1600/letra-n.jpg"
LETRA_O = "https://i.pinimg.com/originals/d4/03/ce/d403ce80c7bf56adcf20adc8009a7bb6.jpg"
LETRA_P = "data:image/png;base64,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"
LETRA_Q = "http://oracc.museum.upenn.edu/qcat/images/Q.png"
LETRA_R = "https://3.bp.blogspot.com/-f4OnzUCj1zg/VzI3ccy7XEI/AAAAAAAAHNE/uAUnW6QI2ZUvtspy7Sty_pZXw39tOfBggCPcBGAYYCw/s1600/letra-r.jpg"
LETRA_S = "https://moldesde.com/wp-content/uploads/2012/02/letra_18.png.jpg"
LETRA_T = "https://image.freepik.com/icones-gratis/t-letra-maiuscula_318-966.jpg"
LETRA_U = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRFeB_lFaybGxv_13iOo42xVN2cIWE6hUYLoa7LHyAmP8QogAGn"
LETRA_V = "https://images.casashops.com/Square620NoGrow/22625/alfabet-letra-v-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_W = "https://s3.amazonaws.com/img.cdm/letra-w-decorativa-preta-mdf-223x19-cm-Carro-de-Mola-M-uIBRH.jpg"
LETRA_X = "https://images.casashops.com/square1168/22627/alfabet-letra-x-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_Y = "https://images.casashops.com/Square620NoGrow/22628/alfabet-letra-y-preto-h-17-x-w-18%2C5-x-d-1%2C5-cm.jpg"
LETRA_Z = "https://i.pinimg.com/originals/09/2b/1b/092b1b58139077e41c0b804a61903529.jpg"

CENA_PARQUE = "https://i.imgur.com/bPDwwQO.jpg"
CENA_CRIANCA = "https://i.imgur.com/hKFY2DF.png"
UMTEXTO = "Monte uma palavra, use sua criatividade"

class Crianca: 
    def __init__(self, parque, tit="joana", x=400, y=470):
        tit=input("escreva seu nome")
        self.parque, self.tit = parque, tit
        escolhas = {"letra_a" : self.a, "letra a": self.a}
        crianca = Elemento(CENA_CRIANCA, tit=tit, x=x, y=y, w=100, h=100, drop=escolhas, style={"opacity":0.2})
        crianca.entra(parque)
        crianca.vai = self.a
        
    def a (self, _):
        texto = Texto (self.parque, UMTEXTO)
        texto.vai()
    
class JogoLetra:
    def __init__(self): 
        parque = Cena (CENA_PARQUE)
        INVENTARIO.inicia()
        self.letra_a = Elemento(LETRA_A,tit="A", x=540, y=470, w=90, h=20, drag=True,vai=self.clicounaletra)
        self.letra_a.entra(parque)
        self.letra_b = Elemento(LETRA_B,tit="B", x=500, y=250, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_b.entra(parque)
        self.letra_c = Elemento(LETRA_C,tit="C", x=400, y=240, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_c.entra(parque)
        self.letra_d = Elemento(LETRA_D,tit="D", x=250, y=250, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_d.entra(parque)
        self.letra_e = Elemento(LETRA_E,tit="E", x=20, y=230, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_e.entra(parque)
        self.letra_f = Elemento(LETRA_F,tit="F", x=50, y=195, w=10, h=30, drag=True,vai=self.clicounaletra)
        self.letra_f.entra(parque)
        self.letra_g = Elemento(LETRA_G,tit="G", x=450, y=255, w=10, h=30, drag=True,vai=self.clicounaletra)
        self.letra_g.entra(parque)
        self.letra_h= Elemento(LETRA_H,tit="H", x=550, y=195, w=10, h=30, drag=True,vai=self.clicounaletra)
        self.letra_h.entra(parque)
        self.letra_i = Elemento(LETRA_I,tit="I", x=320, y=195, w=10, h=30, drag=True,vai=self.clicounaletra)
        self.letra_i.entra(parque)
        self.letra_j = Elemento(LETRA_J,tit="J", x=600, y=195, w=10, h=30, drag=True,vai=self.clicounaletra)
        self.letra_j.entra(parque)
        self.letra_k = Elemento(LETRA_K,tit="K", x=650, y=205, w=10, h=30, drag=True,vai=self.clicounaletra)
        self.letra_k.entra(parque)
        self.letra_l = Elemento(LETRA_L,tit="L", x=350, y=210, w=20, h=30, drag=True,vai=self.clicounaletra)
        self.letra_l.entra(parque)
        self.letra_m = Elemento(LETRA_M,tit="M", x=700, y=180, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_m.entra(parque)
        self.letra_n = Elemento(LETRA_N,tit="N", x=420, y=190, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_n.entra(parque)
        self.letra_o = Elemento(LETRA_O,tit="O", x=90, y=500, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_o.entra(parque)
        self.letra_p = Elemento(LETRA_P,tit="P", x=750, y=555, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_p.entra(parque)
        self.letra_q = Elemento(LETRA_Q,tit="Q", x=500, y=100, w=35, h=30, drag=True,vai=self.clicounaletra)
        self.letra_q.entra(parque)
        self.letra_r = Elemento(LETRA_R,tit="R", x=650, y=400, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_r.entra(parque)
        self.letra_s = Elemento(LETRA_S,tit="S", x=150, y=410, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_s.entra(parque)
        self.letra_t = Elemento(LETRA_T,tit="T", x=200, y=475, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_t.entra(parque)
        self.letra_u = Elemento(LETRA_U,tit="U", x=110, y=225, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_u.entra(parque)
        self.letra_v = Elemento(LETRA_V,tit="V", x=555, y=400, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_v.entra(parque)
        self.letra_w = Elemento(LETRA_W,tit="W", x=225, y=200, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_w.entra(parque)
        self.letra_x = Elemento(LETRA_X,tit="X", x=700, y=450, w=30, h=30, drag=True,vai=self.clicounaletra)
        self.letra_x.entra(parque)
        self.letra_y = Elemento(LETRA_Y,tit="Y", x=200, y=100, w=10, h=30, drag=True,vai=self.clicounaletra)
        self.letra_y.entra(parque)
        self.letra_z = Elemento(LETRA_Z,tit="Z", x=250, y=105, w=35, h=30, drag=True,vai=self.clicounaletra)
        self.letra_z.entra(parque)
        Crianca(parque, tit="joana")
        self.mapa=dict(A=self.letra_a,B=self.letra_b,C=self.letra_c,D=self.letra_d,E=self.letra_e,F=self.letra_f,
          G=self.letra_g,H=self.letra_h,I=self.letra_i,J=self.letra_j,K=self.letra_k,L=self.letra_l,
          M=self.letra_m,N=self.letra_n,O=self.letra_o,P=self.letra_p,Q=self.letra_q,R=self.letra_r,
          S=self.letra_s,T=self.letra_t,U=self.letra_u,V=self.letra_v,W=self.letra_w,X=self.letra_x,Y=self.letra_y,Z=self.letra_z)
        parque.vai()
    def clicounaletra(self,ev):
        INVENTARIO.bota(self.mapa[ev.target.id])
JogoLetra()
