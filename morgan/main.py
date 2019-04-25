# vera.morgan.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto
# from morgan.main import FlorestaBanana
FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"
TEXTO_LEAO= "O leão está com fome, tome cuidado!Se você não correr ele vai te comer"
LEAO_COME= "GAME OVER"


class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_banana = None
    def vai(self):
        from rachel.main import FlorestaBanana
        self.floresta_banana = FlorestaBanana()
        self.floresta_banana.esquerda = self.aqui
        self.floresta_banana.vai()

FLORESTA = "https://i.imgur.com/wBw3Lyl.jpg"
LEAO = "https://i.imgur.com/4gXpvfQ.png"


class Leao:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_LEAO)
        self.falou = Texto(self.floresta_inicio, LEAO_COME)
        self.leao = Elemento(LEAO, style=dict(left="150px",width="100px"), vai=self.pega)
        self.leao.entra(self.floresta_inicio)
    
    def pega(self, _): 
       self.fala.vai()
       self.leao.vai = self.morre
    
    def morre(self, _): 
       self.falou.vai()
        
class FlorestaLeao:
    def __init__(self):
        self.floresta_inicio = None
        floresta_banana = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_banana)
        leao = Leao(self.floresta_inicio)
        
        
        
    def vai(self):
        self.floresta_inicio.vai()

if __name__ == "__main__":
    a_floresta = FlorestaLeao()
    a_floresta.vai()

