# vera.morgan.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
FLORESTA = "https://i.imgur.com/wBw3Lyl.jpg"
LEAO = "https://i.imgur.com/JXFofUP.jpg"
floresta_inicio = Cena(FLORESTA)
leao = Elemento(LEAO)
floresta_inicio.vai()
leao.entra(floresta_inicio)
floresta_inicio.vai()

