# vera.cavernatesouro.main.py
from _spy.vitollino.main import Cena, STYLE, Codigo
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
CAVERNATESOURO = "https://i.imgur.com/RgatDJ4.jpg"
TESOURO = "https://i.imgur.com/FqtXDXb.jpg"
cavernatesouro = Cena(CAVERNATESOURO)
cavernatesouro.vai()
codigo = Codigo ("alo", "um texto maior",cena = cavernatesouro, style = dict( x= 400, y= 300))
cavernatesouro.meio = codigo