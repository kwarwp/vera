# vera.fundodomar.main.py
# vera.perigo1.main.py
# vera.mar.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
FUNDODOMAR = "https://imgur.com/Mc6ktz2.png"
ESMERALDA = "https://imgur.com/SuPb9Wa.png"
PERGAMINHO = "https://i.imgur.com/6pz0aHn.png"
AGUAVIVA = "https://i.imgur.com/7aIQZcW.png"
PEIXE = "https://i.imgur.com/toGygPm.gif"
fundodomar = Cena(FUNDODOMAR)
fundodomar.vai()
esmeralda = Elemento (ESMERALDA, cena = fundodomar, x= 600, y= 500, w= 50, h= 50)
pergaminho = Elemento (PERGAMINHO, cena = fundodomar, x= 1000, y= 100, w= 100, h= 100)
aguaviva = Elemento (AGUAVIVA, cena = fundodomar, x= 200, y= 250, w= 300, h= 200)
peixe = Elemento (PEIXE, cena = fundodomar, x= 700, y= 250, w= 200, h= 100)

