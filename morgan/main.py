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
        from Rachel.main import FlorestaBanana
        self.floresta_banana = FlorestaBanana()
        self.floresta_Banana.esquerda = self.aqui
        self.floresta_banana.vai()

class FlorestaBanana:
    def __init__(self):
        # floresta_banana = FlorestaBanana() -XX- ERRO!
        self.floresta_inicio = None
        floresta_banana = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_banana)
        banana = Elemento(BANANA, style=dict(left="200px", width="80px"))
        banana.entra(self.floresta_inicio)
   def vai(self):
       self.floresta_inicio.vai()

if __name__ == "__main__":
   a_floresta = Florestabanana()
   a_floresta.vai()

