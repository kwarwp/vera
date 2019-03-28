# vera.rachel.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
FLORESTA = "https://i.imgur.com/VHaolvA.jpg"
BANANA = "https://i.imgur.com/HnIHJd7.png"
floresta_inicio = Cena(FLORESTA)
banana = Elemento(BANANA, style=dict(left="230px", width="50px"))
banana.entra(floresta_inicio)
floresta_inicio.vai()