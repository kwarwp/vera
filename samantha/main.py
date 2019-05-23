# vera.teacher.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento

LETRA_A = "https://i.imgur.com/sFciRzA.jpg"
LETRA_B = "https://i.imgur.com/IHu7zVe.jpg"
LETRA_C = "https://i.imgur.com/KDkL6Lg.jpg"
LETRA_D = "https://i.imgur.com/RyfJybm.jpg"
LETRA_E = "https://i.imgur.com/lHMbjdZ.gif"
LETRA_F = "https://i.imgur.com/IcWkooX.jpg"

CENA_PARQUE = "https://i.imgur.com/bPDwwQO.jpg"

class JogoLetra:
    def __init__(self): 
        parque = Cena (CENA_PARQUE)
        letra_a = Elemento(LETRA_A, x=100, y=100, w=40, h=30)
        letra_a.entra(parque)
        letra_b = Elemento(LETRA_B, x=120, y=250, w=40, h=30)
        letra_b.entra(parque)
        letra_c = Elemento(LETRA_C, x=130, y=110, w=40, h=30)
        letra_c.entra(parque)
        letra_d = Elemento(LETRA_D, x=140, y=120, w=40, h=30)
        letra_d.entra(parque)
        letra_e = Elemento(LETRA_E, x=150, y=130, w=40, h=30)
        letra_e.entra(parque)
        letra_f = Elemento(LETRA_F, x=160, y=105, w=40, h=30)
        letra_f.entra(parque)
        parque.vai()
        
JogoLetra()