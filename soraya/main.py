# vera.soraya.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
FLORESTA = "https://i.imgur.com/bfO1gCN.jpg"
MACACO = "https://i.imgur.com/dIBkMcG.png"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_faca = None
    def vai(self):
        from amanda.main import FlorestaFaca
        self.floresta_faca = FlorestaFaca()
        self.floresta_faca.esquerda = self.aqui
        self.floresta_faca.vai()


class FlorestaMacaco:
    def __init__(self):
        self.floresta_inicio = None
        floresta_faca = CenaProxy(self.floresta_inicio)

        floresta_inicio = Cena(FLORESTA, direita=floresta_faca)
        macaco = Elemento(MACACO, style=dict(left="200px", width="50px"))
        macaco.entra(floresta_inicio)
        floresta_inicio.vai()
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    a_floresta = FlorestaMacaco()
    a_floresta.vai()        
