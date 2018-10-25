# vera.kathryn.main.py
from ruzwana.main import Turno
from callie.main import Perigo
from callie.main import Tesouro
from natalia.main import Jogador
from natalia.main import Mesa
"""
kathryn - Baralho - Joias - Rodada
callie - Perigo - Perder - Tesouro
ruzwana - Ficar - Turno - Sair
natalia - Mesa - Iniciar - Jogador
lisa - Decisao - Morrer - Partida
meredith - Universo
"""


class Baralho:
    def __init__(self) :
        self.turno = Turno()
        self.perigo = Perigo()
        self.tesouro = Tesouro()
        
    def comeca(self):
        self.turno.vire_cartas()
        self.perigo.apresente_a_mesa()
        self.tesouro.apresente_a_mesa()
        
if __name__ == "__main__":
    baralho = Baralho()
    baralho.chame_turno()
    
class Joias:
    def __init__(self):
        self.jogador = Jogador()
        self.mesa = Mesa()
    
    def começa(self):
        self.jogador.decida()
        self.jogador.receba()
        self.mesa.chame_o_turno()
        
class Rodada:
    def __init__(self):
        self.baralho = Baralho()
        
    def comeca(self):
        self.baralho.embaralhe()