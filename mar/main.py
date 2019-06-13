# vera.mar.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1000, "650px"
from elemento.main import Elemento
PRAIA = "https://i.imgur.com/OHqdhyR.png"
ILHAMAR = "https://i.imgur.com/YaIP847.jpg"
ilhamar = Cena(ILHAMAR)
praia = Elemento(PRAIA, cena=ilhamar, x=400, y=300, h=600, style=dict(width= 700, height="650px"))
ilhamar.vai()
