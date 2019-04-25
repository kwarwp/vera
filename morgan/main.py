# vera.morgan.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
# from morgan.main import FlorestaBanana
FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_banana = None
    def vai(self):
        from rachel.main import FlorestaBanana
        self.floresta_banana = FlorestaBanana()
        self.floresta_Banana.esquerda = self.aqui
        self.floresta_banana.vai()

FLORESTA = "https://i.imgur.com/wBw3Lyl.jpg"
LEAO = "https://i.imgur.com/4gXpvfQ.png"
class FlorestaLeao:
    def __init__(self):
        self.floresta_inicio = None
        floresta_banana = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_banana)
        leao = Elemento(LEAO, style=dict(left="150px",width="100px"))
        leao.entra(self.floresta_inicio)
    def vai(self):
        self.floresta_inicio.vai()

if __name__ == "__main__":
    a_floresta = FlorestaLeao()
    a_floresta.vai()

