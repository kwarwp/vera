# vera.mapa.main.py
from _spy.vitollino.main import Cena, STYLE, Elemento
from elemento.main import Elemento
STYLE["width"] = 900
STYLE["heigth"] = "900px"

CENA_MAPA = "https://i.imgur.com/4d2spVj.jpg"
CLICAR = "https://i.imgur.com/U8kaaKl.jpg"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.mapaSeleciona = None 
    def vai(self, ev):
        from julia.main import jogoPescaria
        jogoPescaria.vai()
        
class CenaProxy2:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.mapaSeleciona = None 
    def vai(self, ev):
        from alexa.main import Conjuntos
        Conjuntos.vai()

class CenaProxy3:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.mapaSeleciona = None 
    def vai(self, ev):
        from samantha.main import JogoLetras
        JogoLetras.vai()

class areaPescaria:
    def __init__(self, mapa, tit="area", x=350, y=200):
        clicar = Elemento(CLICAR, tit=tit, x=x, y=y, w=100,h=100, style={"opacity":0.3})
        clicar.entra(mapa)
        clicar.vai=CenaProxy().vai

class areaConjuntos:
    def __init__(self, mapa, tit="area", x=350, y=200):
        clicar = Elemento(CLICAR, tit=tit, x=x, y=y, w=100,h=100, style={"opacity":0.3})
        clicar.entra(mapa)
        clicar.vai=CenaProxy2().vai

class areaLetras:
    def __init__(self, mapa, tit="area", x=350, y=200):
        clicar = Elemento(CLICAR, tit=tit, x=x, y=y, w=100,h=100, style={"opacity":0.3})
        clicar.entra(mapa)
        clicar.vai=CenaProxy3().vai

class mapaParque:
    def __init__(self):
        mapa = Cena(CENA_MAPA)
        mapa.vai()
        areaPescaria(mapa, tit="pescaria", x=150, y=280)
        areaConjuntos(mapa, tit="tiro ao alvo", x=650, y=205)
        areaLetras(mapa, tit="carrinho bate bate", x=350, y=280)
        
                
mapaParque()
      