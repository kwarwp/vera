# vera.cavernaamigo.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
CAVERNAAMIGO = "https://i.imgur.com/rHNPcSh.jpg"
AMIGO = "https://i.imgur.com/T9EbLID.png"
cavernaamigo = Cena(CAVERNAAMIGO)
cavernaamigo.vai()