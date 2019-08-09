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
ALL = "coelho passarinho bola peteca maçã laranja tenis galocha".split()
def score(casa=[], carta="", move="DROP", ponto="OK", valor="", _level=1):
        INVENTARIO.elt.html = f"casa={[ev.x, ev.y]}, carta={tit}, move=DROP, ponto={ok}, valor={cria[9]}"


class Coisa:
    def __init__(self):
        pass
    def click(self, ev):
        score(casa=[ev.x, ev.y], carta=self.tit[0], move="CLICK", ponto="OK", valor="COISA", _level=1)

class Fruta(Coisa):
    def __init__(self, parque,tit="maçã", imagem=MACA, x=200, y=200):
        self.tit = tit
        maca = Elemento(imagem, tit=tit, x=x, y=y, w=50, h=40, drag=True, tipo="100% 100%", vai=self.click)
        maca.entra(parque)
        parque.cadastra(tit, maca)
class Esportes(Coisa):  
    def __init__(self, parque,tit="bola", imagem=BOLA, x=100, y=200): 
        self.tit = tit
        peteca = Elemento(imagem, tit=tit, x=x, y=y, w=50, h=50, drag=True, vai=self.click)
        peteca.entra(parque)
        parque.cadastra(tit, peteca)
        #bola = Elemento(BOLA, x=100, y=200, w=80, h=60)
        #bola.entra(parque)
        
class Bicho(Coisa):
    def __init__(self, parque, tit="coelho", imagem=COELHO, x=40, y=40):
        #coelho = Elemento(COELHO, x=100, y=100, w=60, h=40)
        #coelho.entra(parque)
        self.tit = tit
        passarinho = Elemento(imagem, tit=tit, x=x, y=y, w=70, h=50, drag=True, vai=self.click)
        passarinho.entra(parque)
        parque.cadastra(tit, passarinho)
        
class Calcado(Coisa):
    def __init__(self,parque, tit="tenis", imagem=TENIS, x=300, y=350):
        #tenis = Elemento(TENIS, x=150, y=210, w=50, h=80)
        #tenis.entra(parque)
        self.tit = tit
        galocha = Elemento(imagem, tit=tit, x=x, y=y, w=60, h=50, drag=True, vai=self.click)
        galocha.entra(parque)
        parque.cadastra(tit, galocha)
        
class Crianca:
    def __init__(self, parque, tit="crianca", x=0, y=210, gosta=""):
        self.tit = tit
        dragger = {ti: lambda e,t: parque.gostou(e, t, tit, ok=ti in gosta.split()) for ti in ALL}
        crianca = Elemento(CRIANCA, tit=tit, x=x-10, y=y-10, w=90, h=140, style={"opacity": 0.3}, drop=dragger)
        crianca.entra(parque)
        
    def click(self, ev):
        score(casa=[ev.x, ev.y], carta=self.tit[9], move="CLICK", ponto="OK", valor="GENTE", _level=1)
        
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
        
    def gostou(self, ev, tit, cria, ok):
        #INVENTARIO.elt.html = tit
        #INVENTARIO.score(casa=[ev.x, ev.y], carta=[tit], move="DROP", ponto="OK", valor=cria[9], _level=1):
        #INVENTARIO.elt.html = dict(casa=[ev.x, ev.y], carta=tit, move="DROP", ponto=ok, valor=cria[9], _level=1)
        INVENTARIO.elt.html = f"casa={[ev.x, ev.y]}, carta={tit}, move=DROP, ponto={ok}, valor={cria[9]}"
        #INVENTARIO.bota(self.coisas[tit]) if ok else None
        
        
Conjuntos()
