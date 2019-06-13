# vera.mar.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
PRAIA = "https://i.imgur.com/slKTEBc.png"
ILHAMAR = "https://i.imgur.com/YaIP847.jpg"
ilhamar = Cena(ILHAMAR)
praia = Elemento(PRAIA, cena=ilhamar, x=300, y=200, h=500, style=dict(width= 700, height="650px"))
ilhamar.vai()
