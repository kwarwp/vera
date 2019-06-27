# vera.fundodomar.main.py
# vera.perigo1.main.py
# vera.mar.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
FUNDODOMAR = "https://imgur.com/Mc6ktz2.png"
ESMERALDA = "https://imgur.com/SuPb9Wa.png"
fundodomar = Cena(FUNDODOMAR)
fundodomar.vai()
esmeralda = Elemento (ESMERALDA, cena = fundodomar, x= 200, y= 500, w= 50, h= 50)

