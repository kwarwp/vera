# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto, INVENTARIO
# from amanda.main import FlorestaFaca
FLORESTA = "https://i.imgur.com/VHaolvA.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"
TEXTO_BANANA= "O macaquinho pode ficar com fome! Coloque na bolsa!"
BANANA_FOI= "Hummm, que delícia!"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_faca = None
    def vai(self):
        from amanda.main import FlorestaFaca
        self.floresta_faca = FlorestaFaca()
        self.floresta_faca.esquerda = self.aqui
        self.floresta_faca.vai()


class Banana:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_BANANA)
        self.falou = Texto(self.floresta_inicio, BANANA_FOI)
        self.banana = Elemento(BANANA, style=dict(left="230px", width="50px"), vai=self.pega)
        self.longe = Cena()
        self.banana.entra(self.floresta_inicio)
        
    def pega(self, _):
        self.fala.vai()
        self.banana.vai = self.guarda
        
    def guarda(self, _):
        INVENTARIO.bota(self.banana)
        self.falou.vai()
        
    def come(self, _):
        self.banana.entra(self.longe)
        self.falou.vai()
        
        
class FlorestaBanana:
    def __init__(self):
        # floresta_faca = FlorestaFaca() -XX- ERRO!
        self.floresta_inicio = None
        floresta_faca = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_faca)
        banana = Banana(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
                
if __name__ == "__main__":
    a_floresta = FlorestaBanana()
    a_floresta.vai()