# vera.alexa.main.py
from _spy.vitollino.main import Cena,STYLE,Codigo, INVENTARIO
from elemento.main import Elemento 
STYLE["width"] = 600
STYLE["heigth"] = "600px"

LARANJA = "https://i.imgur.com/XXi1abd.png"
MACA = "https://i.imgur.com/8aCEBLc.png"
COELHO = "https://i.imgur.com/Tm65bCu.png"
PASSARINHO = "https://i.imgur.com/0BfAZQo.png"
PETECA = "https://i.imgur.com/bYAo3kt.png"
BOLA = "https://i.imgur.com/yUEgszl.png"
CENA_PARQUE = "https://i.imgur.com/kqWvogN.jpg"
CRIANCA = "https://i.imgur.com/j0ETf5x.jpg"
TENIS = "https://i.imgur.com/nwKWo8x.png"
GALOCHA = "https://i.imgur.com/JlGV4P8.png"

class Fruta:
    def __init__(self, parque,tit="maçã", imagem=MACA, x=200, y=200):
        maca = Elemento(imagem, tit=tit, x=x, y=y, w=50, h=40, drag=True, tipo="100% 100%")
        maca.entra(parque)
        parque.cadastra(tit, maca)
class Esportes:  
    def __init__(self, parque,tit="bola", imagem=BOLA, x=100, y=200): 
        peteca = Elemento(imagem, tit=tit, x=x, y=y, w=50, h=50, drag=True)
        peteca.entra(parque)
        parque.cadastra(tit, peteca)
        #bola = Elemento(BOLA, x=100, y=200, w=80, h=60)
        #bola.entra(parque)
        
class Bicho:
    def __init__(self, parque, tit="coelho", imagem=COELHO, x=40, y=40):
        #coelho = Elemento(COELHO, x=100, y=100, w=60, h=40)
        #coelho.entra(parque)
        passarinho = Elemento(imagem, tit=tit, x=x, y=y, w=70, h=50, drag=True)
        passarinho.entra(parque)
        parque.cadastra(tit, passarinho)
        
class Calcado:
    def __init__(self,parque, tit="tenis", imagem=TENIS, x=300, y=350):
        #tenis = Elemento(TENIS, x=150, y=210, w=50, h=80)
        #tenis.entra(parque)
        galocha = Elemento(imagem, tit=tit, x=x, y=y, w=60, h=50, drag=True)
        galocha.entra(parque)
        parque.cadastra(tit, galocha)
        
class Crianca:
    def __init__(self, parque, tit="crianca", x=0, y=210, gosta=""):
        dragger = {tit: parque.gostou for tit in gosta.split()}
        crianca = Elemento(CRIANCA, tit=tit, x=x-10, y=y-10, w=90, h=140, style={"opacity": 0.3}, drop=dragger)
        crianca.entra(parque)
        
class Conjuntos(Cena):
    def __init__(self):
        super().__init__(CENA_PARQUE)
        self.coisas = {}
        parque = self  # Cena(CENA_PARQUE)
        INVENTARIO.inicia()
        #INVENTARIO.elt.html = "PARQUE"
        nome = Codigo(codigo="", topo="PARQUE", style=dict(left=250, top=220, width=100, height="60px"))
        nome.entra(parque)
        Crianca(parque, tit="gosto de bicho", x=60, y=300, gosta="coelho passarinho")
        Crianca(parque, tit="gosto de esportes", x=150, y=300, gosta="bola peteca")
        Crianca(parque, tit="gosto de frutas", x=400, y=300, gosta="maçã laranja") 
        Crianca(parque, tit="gosto de calçado", x=480, y=300, gosta="tenis galocha")
        Fruta(parque, x=30, y=90)
        Fruta(parque, tit="laranja", imagem=LARANJA, x=330, y=60)
        Esportes(parque, x=100, y=150)
        Esportes(parque, tit="peteca", imagem=PETECA, x=500, y=35) 
        Bicho(parque, x=150, y=80)
        Bicho(parque, tit="passarinho", imagem=PASSARINHO, x=400, y=60)
        Calcado(parque, x=450, y=100) 
        Calcado(parque, tit="galocha", imagem=GALOCHA, x=200, y=50) 
        parque.vai()
        
    def cadastra(self, tit, elm):
        self.coisas[tit] = elm
        
    def gostou(self, ev, tit):
        #INVENTARIO.elt.html = tit
        INVENTARIO.bota(self.coisas[tit])
        
        
Conjuntos()
