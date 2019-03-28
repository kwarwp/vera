# vera.amanda.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
from morgan.main import FlorestaLeao

FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"
FACA = "https://i.imgur.com/H2vMcB4.png"
class FlorestaFaca:
    def __init__(self):
        floresta_leao = FlorestaLeao()
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_leao)
        faca = Elemento(FACA, style=dict(left="200px", width="80px"))
        faca.entra(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    a_floresta = FlorestaFaca()
    a_floresta.vai()