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
boia = Elemento(BOIA, cena=ilhamar, x=30, y=140, w=100)
boia2 = Elemento(BOIA, cena=ilhamar, x=100, y=300, w=100)
boia3 = Elemento(BOIA, cena=ilhamar, x=200, y=350, w=100)
boia4 = Elemento(BOIA, cena=ilhamar, x=320, y=400, w=100)
boia5 = Elemento(BOIA, cena=ilhamar, x=440, y=420, w=100)
boia6 = Elemento(BOIA, cena=ilhamar, x=350, y=250, w=100)
boia7 = Elemento(BOIA, cena=ilhamar, x=500, y=290, w=100)
boia8 = Elemento(BOIA, cena=ilhamar, x=650, y=330, w=100)
boia9 = Elemento(BOIA, cena=ilhamar, x=800, y=370, w=100)
boia10 = Elemento(BOIA, cena=ilhamar, x=950, y=400, w=100)