# vera.trilhacaverna.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
TRILHACAVERNA = "https://i.imgur.com/bNEzuBs.jpg"
ARANHA = "https://i.imgur.com/xXPifks.png"
trilhacaverna = Cena(TRILHACAVERNA)
trilhacaverna.vai()
aranha = Elemento (ARANHA, cena = trilhacaverna, x= 200, y= 500, w= 50, h= 50)
