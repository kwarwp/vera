# vera.julia.main.py
from _spy.vitollino.main import Cena, STYLE, INVENTARIO
from elemento.main import Elemento #permite a movimentacao
STYLE["width"] = 900
STYLE["heigth"] = "900px"
def score(casa=[], carta="", move="ID", ponto="OK", valor="", _level=1):
    INVENTARIO.elt.html = f"casa={casa}, carta={carta}, move={move}, ponto={ponto}, valor={valor}, level={_level}"
    #INVENTARIO.score(casa=casa, carta=carta, move=move, ponto=ponto, valor=valor, _level=_level)

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

class Peixe:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_AMARELO, tit="peixe grande", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe2:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_VERD1, tit="peixe pequeno", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe3:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_VERD2, tit="peixe médio", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe4:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXEROSA, tit="peixegrande", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe5:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_AZULROXO, tit="peixe médio", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe6:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_CINZA, tit="peixe grande", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe7:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_SALM, tit="peixegrande", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe8:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_AZULARANJA, tit="peixe pequeno", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe9:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_LARANJINHA, tit="peixepequeno", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)


class Peixe10:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_PRETOLARANJA, tit="peixemédio", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe11:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_COLOR, tit="peixe médio", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)
        
class Peixe12:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_VERDINHO, tit="peixepequeno", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)
        
class Peixe13:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_ROSINHA, tit="peixe pequeno", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)

class Peixe14:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_VERMELHO, tit="peixemédio", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)
        
class Peixe15:
    def __init__(self, pescaria, x=350, y=200):
        peixe = Elemento(PEIXE_AZULMARINHO, tit="peixegrande", x=x, y=y, w=60, h=40, drag=True)
        peixe.entra(pescaria)
        pescaria.cadastra(peixe.tit, peixe)
        
class Balde: #baldes clicáveis
    def __init__(self, pescaria, nome="balde", tipo_peixe="grande", x=350, y=200): #tit quando arrastar o mouse em cima, surge o nome
        self.peixes = pescaria.peixes(tipo_peixe).keys()
        todos = [peixe for tam in "pequno médio grande".split() for peixe in pescaria.peixes(tam).keys()]
        balde = Elemento(BALDE, x=x, y=y, tit=nome, w=100, h=100, style={"opacity": 0.3},
        drop = {peixe: self.pesca for peixe in todos})
        self.tipo = tipo_peixe
        balde.entra(pescaria)
        self.pescaria = pescaria
        
    def pesca(self, ev, peixe):
        #peixe = Elemento(PEIXE_INV, tit=self.tipo)
        score(casa=[ev.x, ev.y], carta=peixe, move="PESCA", ponto=ok, valor=self.tipo[0], _level=1)
        INVENTARIO.bota(self.pescaria.encontra(peixe)) if peixe in self.peixes else None
        
class Crianca:
    def __init__(self, pescaria, tit="tiago", x=350, y=200): #tit quando arrastar o mouse em cima, surge o nome
        crianca = Elemento(CRIANCA, tit=tit, x=x, y=y, w=100, h=100, style={"opacity": 0})
        crianca.entra(pescaria)
        
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
        Peixe(pescaria, x=550, y=505)
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