# vera.parisa.main.py
# vera.sarah.main.py
from _spy.vitollino.main import Cena, Texto, INVENTARIO, Elemento, STYLE
# from morgan.main import FlorestaLeao
STYLE["width"], STYLE["height"] = 1400, "650px"

FOGUETE = "https://i.imgur.com/Q33m8SY.png"
ESTACAO = "https://i.imgur.com/ybteKID.png"
TERRA = "https://i.imgur.com/rJJHQJj.png"
UNIVERSO = "https://i.imgur.com/tjT0IqM.jpg"
DOCA = "https://i.imgur.com/NMLjvWU.png"


class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_leao = None
    def vai(self):
        from morgan.main import FlorestaLeao
        self.floresta_leao = FlorestaLeao()
        self.floresta_leao.esquerda = self.aqui
        self.floresta_leao.vai()

"""
class Estacao:
    def __init__(self, universo):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_FACA)
        self.falou = Texto(self.floresta_inicio, FACA_FOI)
        self.usar = Texto(self.floresta_inicio, FACA_USA)
        # self.faca = Elemento(FACA, style=dict(left="200px", width="80px"), vai=self.pega)
        self.faca = Elemento(FACA, tit="faca", x=600, y=500, w=80, vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.faca.entra(self.floresta_inicio)
    
    def pega(self, _):
        self.fala.vai()
        self.faca.vai = self.guarda
    
    def guarda(self, _):
        INVENTARIO.bota(self.faca)
        self.falou.vai()
        self.faca.vai = self.usa
    
    def chuta(self, _):
        self.faca.entra(self.longe)
        self.falou.vai()
    
    def usa(self, _):
        self.na_mao = True
        self.usar.vai()
"""

class Terra:
    def __init__(self, universo):
        self.universo = universo
        """
        self.fala = Texto(self.universo, TEXTO_FACA)
        self.falou = Texto(self.universo, FACA_FOI)
        self.usar = Texto(self.universo, FACA_USA)
        """
        self.terra = Elemento(TERRA, style=dict(left="200px", width="80px"), vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.terra.entra(self.universo)
    
    def pega(self, _):
        self.fala.vai()
        self.faca.vai = self.guarda
    
    def guarda(self, _):
        INVENTARIO.bota(self.faca)
        self.falou.vai()
        self.faca.vai = self.usa
    
    def chuta(self, _):
        self.faca.entra(self.longe)
        self.falou.vai()
    
    def usa(self, _):
        self.na_mao = True
        self.usar.vai()
        
class Foguete:
    def __init__(self, universo, left="300px", top="100px"):
        self.universo = universo
        self.foguete = Elemento(FOGUETE, style=dict(left=left, top=top, width="100px", height="250px"), vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.foguete.entra(self.universo)
    
    def pega(self, _):
        self.foguete.vai()
        self.foguete.vai = self.guarda
        
class Doca:
    def __init__(self, universo, left="300px", top="300px"):
        self.universo = universo
        self.doca = Elemento(DOCA, style=dict(left=left, top=top, width="100px", height="250px"), vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.doca.entra(self.universo)
    
    def pega(self, _):
        self.doca.vai()
        self.doca.vai = self.guarda

class Estacao:
    def __init__(self, universo, left="300px", top="300px"):
        self.universo = universo
        """
        self.fala = Texto(self.universo, TEXTO_FACA)
        self.falou = Texto(self.universo, FACA_FOI)
        self.usar = Texto(self.universo, FACA_USA)
        """
        self.estacao = Elemento(ESTACAO, style=dict(left=left, top=top, width="200px"), vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.estacao.entra(self.universo)
    
    def pega(self, _):
        self.fala.vai()
        self.faca.vai = self.guarda
    
    def guarda(self, _):
        INVENTARIO.bota(self.faca)
        self.falou.vai()
        self.faca.vai = self.usa
    
    def chuta(self, _):
        self.faca.entra(self.longe)
        self.falou.vai()
    
    def usa(self, _):
        self.na_mao = True
        self.usar.vai()
        
        
        
class Universo:
    def __init__(self):
        # floresta_leao = FlorestaLeao() -XX- ERRO!
        self.universo = None
        deserto = CenaProxy(self.universo)
        self.universo = Cena(UNIVERSO)
        terra = Terra(self.universo)
        estacao = Estacao(self.universo)
        estacao2 = Estacao(self.universo, left="500px", top="200px")
        estacao3 = Estacao(self.universo, left="800px", top="100px")
        foguete = Foguete(self.universo, left="100px", top="50px")
        doca = Doca(self.universo, left="200px", top="50px")
        
    def vai(self):
        self.universo.vai()
        
if __name__ == "__main__":
    INVENTARIO.inicia()
    o_universo = Universo()
    o_universo.vai()