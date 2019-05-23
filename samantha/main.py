# vera.teacher.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento

LETRA_A = "https://i.imgur.com/sFciRzA.jpg"
LETRA_B = "https://i.imgur.com/IHu7zVe.jpg"
CENA_PARQUE = "https://i.imgur.com/bPDwwQO.jpg"

class JogoLetra:
    def __init__(self): 
        parque = Cena (CENA_PARQUE)
        letra_a = Elemento(LETRA_A, x=170, y=130, w=40, h=30)
        letra_a.entra(parque)
        letra_b = Elemento(LETRA_B, x=170, y=250, w=40, h=30)
        letra_b.entra(parque)
        parque.vai()
        
JogoLetra()