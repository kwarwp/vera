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
boia = Elemento(BOIA, cena=ilhamar, x=30, y=140, w=50)
boia2 = Elemento(BOIA, cena=ilhamar, x=100, y=200, w=50)
boia3 = Elemento(BOIA, cena=ilhamar, x=200, y=250, w=50)
boia4 = Elemento(BOIA, cena=ilhamar, x=320, y=300, w=50)
boia5 = Elemento(BOIA, cena=ilhamar, x=440, y=320, w=50)
boia6 = Elemento(BOIA, cena=ilhamar, x=150, y=150, w=50)
boia7 = Elemento(BOIA, cena=ilhamar, x=300, y=190, w=50)
boia8 = Elemento(BOIA, cena=ilhamar, x=450, y=230, w=50)
boia9 = Elemento(BOIA, cena=ilhamar, x=600, y=270, w=50)
boia10 = Elemento(BOIA, cena=ilhamar, x=750, y=300, w=50)