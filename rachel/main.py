# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento

FLORESTA = "https://i.imgur.com/VHaolvA.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"
class Florestabanana:
    def __init__(self):
        self.floresta_inicio = Cena(FLORESTA)
        banana = Elemento(BANANA, style=dict(left="230px", width="50px"))
        banana.entra(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    a_floresta = Florestabanana()
    a_floresta.vai()