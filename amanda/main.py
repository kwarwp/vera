# vera.amanda.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"
FACA = "https://i.imgur.com/pC6LXEZ.jpg"
floresta_inicio = Cena(FLORESTA)
faca = Elemento(FACA)
faca.entra(floresta_inicio)
floresta_inicio.vai()