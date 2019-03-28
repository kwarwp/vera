# vera.morgan.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
FLORESTA = "https://i.imgur.com/wBw3Lyl.jpg"
LEAO = "https://i.imgur.com/4gXpvfQ.png"
floresta_inicio = Cena(FLORESTA)
leao = Elemento(LEAO, style=dict(width="150px"))
floresta_inicio.vai()
leao.entra(floresta_inicio)
floresta_inicio.vai()

