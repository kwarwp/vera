# vera.julia.main.py
from _spy.vitollino.main import Cena, STYLE, INVENTARIO, Texto, Elemento
#from elemento.main import Elemento #permite a movimentacao
STYLE["width"] = 900
STYLE["heigth"] = "900px"
def score(casa=[], carta="", move="ID", ponto="OK", valor="", _level=1):
    #INVENTARIO.elt.html = f"casa={casa}, carta={carta}, move={move}, ponto={ponto}, valor={valor}, level={_level}"
    INVENTARIO.score(casa=casa, carta=carta, move=move, ponto=ponto, valor=valor, _level=_level)

#JARRA = "https://i.imgur.com/y2YyMOM.jpg"
PEIXE_INV ="https://i.imgur.com/nZDmsh0.png"
PEIXE_AMARELO ="https://i.imgur.com/kcPdkmq.png"
PEIXE_VERD1 = "https://i.imgur.com/9Q52391.png"
PEIXE_VERD2 = "https://i.imgur.com/uAjOtz2.png"
PEIXEROSA = "https://i.imgur.com/1JMWIAT.png"
PEIXE_AZULROXO = "https://i.imgur.com/8l90Llu.png"
PEIXE_CINZA = "https://i.imgur.com/P75bVuk.png"
PEIXE_SALM = "https://i.imgur.com/AcTCoXY.png"
PEIXE_AZULARANJA ="https://i.imgur.com/ObSSnqI.png"
PEIXE_LARANJINHA = "https://i.imgur.com/pq5Xvav.png"
PEIXE_PRETOLARANJA = "https://i.imgur.com/zTPwzkP.png"
PEIXE_COLOR = "https://i.imgur.com/ikkrZ4G.png"
PEIXE_VERDINHO = "https://i.imgur.com/mJWpSdm.png"
PEIXE_ROSINHA = "https://i.imgur.com/MU3hEl6.png"
PEIXE_VERMELHO = "https://i.imgur.com/RQ9ZgEs.png"
PEIXE_AZULMARINHO = "https://i.imgur.com/tqnZnop.png"
CENA_PESCARIA = "https://i.imgur.com/KQbnPXQ.jpg"
CRIANCA = "https://i.imgur.com/U8kaaKl.jpg" #torna a crianca da imagem clicavel
BALDE = "https://i.imgur.com/H3Hxbz7.png"

class Peixe(Elemento):
    def __init__(self, pescaria, peixe, tit="peixe grande", x=0, y=0, w=60, h=40, drag=True):
        super().__init__(peixe, tit=tit, x=x, y=y, w=60, h=40, drag=True, vai=self.olha)
        peixe = self
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)
        nome = tit
        self.texto = Texto(pescaria, f"Eu sou um {nome}")
        
    def olha(self, ev):
        score(casa=[ev.x, ev.y], carta=self.tit, move="OLHA", ponto=True, valor=0, _level=1)
        self.texto.vai()

class Peixe1(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_AMARELO, tit="peixe grande", x=x, y=y, w=60, h=40, drag=True)

class Peixe2(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_VERD1, tit="peixe pequeno", x=x, y=y, w=60, h=40, drag=True)

class Peixe3(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_VERD2, tit="peixe médio", x=x, y=y, w=60, h=40, drag=True)

class Peixe4(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXEROSA, tit="peixe grande ", x=x, y=y, w=60, h=40, drag=True)

class Peixe5(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_AZULROXO, tit="peixe médio ", x=x, y=y, w=60, h=40, drag=True)

class Peixe6(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_CINZA, tit="peixe grande  ", x=x, y=y, w=60, h=40, drag=True)

class Peixe7(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_SALM, tit=" peixe grande", x=x, y=y, w=60, h=40, drag=True)

class Peixe8(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_AZULARANJA, tit="peixe pequeno ", x=x, y=y, w=60, h=40, drag=True)

class Peixe9(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_LARANJINHA, tit="peixe pequeno  ", x=x, y=y, w=60, h=40, drag=True)


class Peixe10(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_PRETOLARANJA, tit="peixe médio  ", x=x, y=y, w=60, h=40, drag=True)

class Peixe11(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_COLOR, tit=" peixe médio", x=x, y=y, w=60, h=40, drag=True)
        
class Peixe12(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_VERDINHO, tit="peixe pequeno    ", x=x, y=y, w=60, h=40, drag=True)
        
class Peixe13(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_ROSINHA, tit="peixe pequeno     ", x=x, y=y, w=60, h=40, drag=True)

class Peixe14(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_VERMELHO, tit=" peixe grande ", x=x, y=y, w=60, h=40, drag=True)
        
class Peixe15(Peixe):
    def __init__(self, pescaria, x=350, y=200):
        super().__init__(pescaria, PEIXE_AZULMARINHO, tit=" peixe grande  ", x=x, y=y, w=60, h=40, drag=True)
        
class Balde: #baldes clicáveis
    def __init__(self, pescaria, nome="balde", tipo_peixe="grande", x=350, y=200): #tit quando arrastar o mouse em cima, surge o nome
        self.peixes = pescaria.peixes(tipo_peixe).keys()
        todos = [peixe for tam in "pequno médio grande".split() for peixe in pescaria.peixes(tam).keys()]
        balde = Elemento(BALDE, x=x, y=y, tit=nome, w=100, h=100, style={"opacity": 0},
        drop = {peixe: self.pesca for peixe in todos}, vai=self.olha)
        self.tipo = tipo_peixe
        balde.entra(pescaria)
        self.pescaria = pescaria
        self.texto = Texto(pescaria, f"Eu sou um {nome}")
        
    def olha(self, ev):
        score(casa=[ev.x, ev.y], carta=self.tipo, move="BALDE", ponto=True, valor=0, _level=1)
        self.texto.vai()
        
    def pesca(self, ev, peixe):
        #peixe = Elemento(PEIXE_INV, tit=self.tipo)
        ok = self.tipo in peixe
        #score(casa=[ev.x, ev.y], carta=peixe, move="PESCA", ponto=ok, valor=self.tipo[0], _level=1)
        INVENTARIO.bota(self.pescaria.encontra(peixe)) if ok else None
        
class Crianca:
    def __init__(self, pescaria, tit="tiago", x=350, y=200): #tit quando arrastar o mouse em cima, surge o nome
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=100, h=100, style={"opacity": 0}, vai=self.olha)
        crianca.entra(pescaria)
        self.tit = tit
        self.texto = Texto(pescaria, f"Olá, eu sou {tit}")
        
    def olha(self, ev):
        score(casa=[ev.x, ev.y], carta=self.tit, move="CRIA", ponto=True, valor=0, _level=1)
        self.texto.vai()
        
#class Jarra:
#    def __init__(self, pescaria, x=150, y=230):
#        jarra = Elemento(JARRA, x=x, y=y, w=60, h=40, drag=True) #drag permite arrastar o objeto para outro
#        jarra.entra(pescaria)

class jogoPescaria(Cena):
    def __init__(self):
        super().__init__(CENA_PESCARIA)
        pescaria = self
        self.peixe=[{}]*3
        INVENTARIO.inicia()
        participante = input("diga seu nome")
        score(carta=participante, casa="pescaria", move="JULIA", _level=0)

        Peixe1(pescaria, x=550, y=505)
        Peixe2(pescaria, x=280, y=505)
        Peixe3(pescaria, x=590, y=440)
        Peixe4(pescaria, x=460, y=420)
        Peixe5(pescaria, x=420, y=490)
        Peixe6(pescaria, x=400, y=405)
        Peixe7(pescaria, x=480, y=505)
        Peixe8(pescaria, x=390, y=505)
        Peixe9(pescaria, x=620, y=465)
        Peixe10(pescaria, x=520, y=465)
        Peixe11(pescaria, x=330, y=500)
        Peixe12(pescaria, x=650, y=440)
        Peixe13(pescaria, x=230, y=510)
        Peixe14(pescaria, x=530, y=425)
        Peixe15(pescaria, x=420, y=450)
        #Jarra(pescaria)
        #Jarra(pescaria, x=200, y=230)
        Balde(pescaria, nome="balde grande", tipo_peixe="grande", x=285, y=380)
        Balde(pescaria, nome="balde pequeno", tipo_peixe="pequeno", x=15, y=410)
        Balde(pescaria, nome="balde médio", tipo_peixe="médio", x=720, y=460)
        Balde(pescaria, nome="balde pequeno", tipo_peixe="pequeno", x=800, y=415)
        Crianca(pescaria, tit="marcos", x=180, y=280)
        Crianca(pescaria, tit="julia", x=720, y=250)
        pescaria.vai()
        
    def cadastra(self, nome, peixe):
        tipo = sum(i if j in nome else 0 for i,j in enumerate("pequeno médio grande".split()))
        self.peixe[tipo][nome] = peixe
        
    def encontra(self, nome):
        tipo = sum(i if j in nome else 0 for i,j in enumerate("pequeno médio grande".split()))
        return self.peixe[tipo][nome]
        
    def peixes(self, nome):
        tipo = sum(i if j in nome else 0 for i,j in enumerate("pequeno médio grande".split()))
        return self.peixe[tipo]

jogoPescaria()
#print(Elemento(BALDE, tit="ballde").tit)