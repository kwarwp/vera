# vera.amanda.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento, Texto, INVENTARIO
# from morgan.main import FlorestaLeao
FLORESTA = "https://i.imgur.com/vlJS7Ry.jpg"
FACA = "https://i.imgur.com/H2vMcB4.png"
TEXTO_FACA= "A faca está afiada, me cortei! Faca perigosa, melhor chutar para longe"
FACA_FOI= "Ainda bem que me livrei daquela coisa perigosa!"
TEXTO_FACA= "A faca está afiada, me cortei! Faca perigosa, melhor pegar com cuidado"
FACA_FOI= "Cuidadosamente, você coloca a faca na bolsa!"
FACA_USA= "Você segura a faca na mão!"

class CenaProxy:
    def __init__(self, aqui=None):
        self.aqui = aqui
        self.floresta_leao = None
    def vai(self):
        from morgan.main import FlorestaLeao
        self.floresta_leao = FlorestaLeao()
        self.floresta_leao.esquerda = self.aqui
        self.floresta_leao.vai()


class Faca:
    def __init__(self, floresta_inicio):
        self.floresta_inicio = floresta_inicio
        self.fala = Texto(self.floresta_inicio, TEXTO_FACA)
        self.falou = Texto(self.floresta_inicio, FACA_FOI)
        self.usar = Texto(self.floresta_inicio, FACA_USA)
        self.faca = Elemento(FACA, style=dict(left="200px", width="80px"), vai=self.pega)
        self.longe = Cena()
        self.na_mao = False
        self.faca.entra(self.floresta_inicio)
    
    def pega(self, _):
        self.fala.vai()
        self.faca.vai = self.guarda
    
    def guarda(self, _):
        INVENTARIO.bota(self.faca)
        self.falou.vai()
        self.faca.vai = self.usa
    
    def chuta(self, _):
        self.faca.entra(self.longe)
        self.falou.vai()
    
    def usa(self, _):
        self.na_mao = True
        self.usar.vai()
        
        
        
class FlorestaFaca:
    def __init__(self):
        # floresta_leao = FlorestaLeao() -XX- ERRO!
        self.floresta_inicio = None
        floresta_leao = CenaProxy(self.floresta_inicio)
        self.floresta_inicio = Cena(FLORESTA, direita=floresta_leao)
        faca = Faca(self.floresta_inicio)
        
    def vai(self):
        self.floresta_inicio.vai()
        
if __name__ == "__main__":
    INVENTARIO.inicia()
    a_floresta = FlorestaFaca()
    a_floresta.vai()