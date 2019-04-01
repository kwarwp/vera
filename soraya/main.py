# vera.soraya.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento

FLORESTA = "https://i.imgur.com/bfO1gCN.jpg"
macaco = "https://i.imgur.com/dIBkMcG.png"
class florestamacaco:
    def __init__(self):
        self.floresta_inicio = Cena(FLORESTA)
        macaco = Elemento(MACACO, style=dict(left="150px",width="50px"))
        macaco.entra(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    a_florest = Florestamacaco()
    a_floresta.vai()




