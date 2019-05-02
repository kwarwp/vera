# vera.sarah.main.py
from _spy.vitollino.main import Cena, Texto, INVENTARIO, Elemento, STYLE
# from morgan.main import FlorestaLeao
STYLE["width"], STYLE["height"] = 1400, "650px"

FOGUETE = "https://i.imgur.com/Q33m8SY.png"
ESTACAO = "https://i.imgur.com/ybteKID.png"
TERRA = "https://i.imgur.com/rJJHQJj.png"
UNIVERSO = "https://i.imgur.com/tjT0IqM.jpg"


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
        

class Estacao:
    def __init__(self, universo):
        self.universo = universo
        """
        self.fala = Texto(self.universo, TEXTO_FACA)
        self.falou = Texto(self.universo, FACA_FOI)
        self.usar = Texto(self.universo, FACA_USA)
        """
        self.estacao = Elemento(ESTACAO, style=dict(left="300px", width="200px"), vai=self.pega)
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
        
    def vai(self):
        self.universo.vai()
        
if __name__ == "__main__":
    INVENTARIO.inicia()
    o_universo = Universo()
    o_universo.vai()