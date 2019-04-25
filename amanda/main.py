# vera.amanda.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto
# from morgan.main import FlorestaLeao
FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"
FACA = "https://i.imgur.com/H2vMcB4.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_leao = None
    def vai(self):
        from morgan.main import FlorestaLeao
        self.floresta_leao = FlorestaLeao()
        self.floresta_leao.esquerda = self.aqui
        self.floresta_leao.vai()


class Faca:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, "A faca está afiada, me cortei!")
        faca = Elemento(FACA, style=dict(left="200px", width="80px"), vai=self.pega)
        faca.entra(self.floresta_inicio)
    
    def pega(self):
        self.fala.vai()
        
        
        
class FlorestaFaca:
    def __init__(self):
        # floresta_leao = FlorestaLeao() -XX- ERRO!
        self.floresta_inicio = None
        floresta_leao = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_leao)
        faca = Faca(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    a_floresta = FlorestaFaca()
    a_floresta.vai()