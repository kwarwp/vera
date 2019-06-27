# vera.perigo1.main.py
# vera.mar.main.py
from _spy.vitollino.main import Cena, STYLE
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
PRAIA = "https://i.imgur.com/slKTEBc.png"
ILHAMAR = "https://i.imgur.com/ifRjzot.png"
BOIA = "https://i.imgur.com/GmzOUTL.png"
ilhamar = Cena(ILHAMAR)
# praia = Elemento(PRAIA, cena=ilhamar, x=700, y=398, h=900, style=dict(width= 500, height="650px"))
ilhamar.vai()
boia = Elemento(BOIA, cena=ilhamar, x=30, y=100, w=100)
boia2 = Elemento(BOIA, cena=ilhamar, x=100, y=250, w=100)
boia3 = Elemento(BOIA, cena=ilhamar, x=200, y=400, w=100)
boia4 = Elemento(BOIA, cena=ilhamar, x=320, y=550, w=100)
boia6 = Elemento(BOIA, cena=ilhamar, x=500, y=80, w=100)
boia7 = Elemento(BOIA, cena=ilhamar, x=700, y=200, w=100)
boia8 = Elemento(BOIA, cena=ilhamar, x=900, y=300, w=100)
boia9 = Elemento(BOIA, cena=ilhamar, x=1100, y=400, w=100)
