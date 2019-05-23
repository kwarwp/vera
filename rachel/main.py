# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto, INVENTARIO
# from amanda.main import FlorestaFaca
FLORESTA = "https://i.imgur.com/VHaolvA.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"
TEXTO_BANANA= "O macaquinho pode ficar com fome! Coloque na bolsa!"
BANANA_FOI= "Hummm, que delícia!"
BANANA_USA= "Você segura a banana na mão!"
REDE = "https://i.imgur.com/9Fig2oH.png"
TEXTO_REDE= "Caí na armadilha!"
COBRA = "https://i.imgur.com/nQ0StLK.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_faca = None
    def vai(self):
        from amanda.main import FlorestaFaca
        self.floresta_faca = FlorestaFaca()
        self.floresta_faca.esquerda = self.aqui
        self.floresta_faca.vai()

class CenaProxy2:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_macaco = None
    def vai(self):
        from soraya.main import FlorestaMacaco
        self.floresta_macaco = FlorestaMacaco()
        self.floresta_macaco.esquerda = self.aqui
        self.floresta_macaco.vai()

class Banana:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_BANANA)
        self.falou = Texto(self.floresta_inicio, BANANA_FOI)
        self.banana = Elemento(BANANA, style=dict(left="230px", width="50px"), vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.banana.entra(self.floresta_inicio)
        
    def pega(self, _):
        self.fala.vai()
        self.banana.vai = self.guarda
        
    def guarda(self, _):
        INVENTARIO.bota(self.banana)
        self.falou.vai()
        self.banana.vai = self.usa
        
    def come(self, _):
        self.banana.entra(self.longe)
        self.falou.vai()
        
    def usa(self, _):
        self.na_mao = True
        self.usar.vai()
        
class Rede:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_REDE)
        self.rede = Elemento(REDE, style=dict(left="450px", width="250px"))
        self.rede.entra(floresta_inicio)
        self.rede.vai=self.falarede
        
    def vai(self):
        self.floresta_inicio.vai()
        
    def falarede(self,_):
        self.fala.vai() 
        
class Cobra:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.cobra = Elemento(COBRA, style=dict(left="800px", width="150px"))
        self.cobra.entra(floresta_inicio)
        self.cobra.vai()
        
    def vai(self):
        self.floresta_inicio.vai()
        
class FlorestaBanana:
    def __init__(self):
        # floresta_faca = FlorestaFaca() -XX- ERRO!
        self.floresta_inicio = None
        floresta_faca = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_faca)
        banana = Banana(self.floresta_inicio)
        rede = Rede(self.floresta_inicio)
        cobra = Cobra(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
                
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaBanana()
    a_floresta.vai()