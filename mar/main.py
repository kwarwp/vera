# vera.mar.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
PRAIA = "https://i.imgur.com/slKTEBc.png"
ILHAMAR = "https://i.imgur.com/3FUDzbn.jpg"
ilhamar = Cena(ILHAMAR)
praia = Elemento(PRAIA, cena=ilhamar, x=700, y=375, h=900, style=dict(width= 500, height="650px"))
ilhamar.vai()
