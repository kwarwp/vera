#vera.natalia.main.py

from kathryn.main import Rodada
from kathryn.main import Joias
from ruzwana.main import Ficar
from ruzwana.main import Sair

"""
kathryn - Baralho - Joias - Rodada
callie - Perigo - Perder - Tesouro
ruzwana - Ficar - Turno - Sair
natalia - Mesa - Iniciar - Jogador
lisa - Decisao - Morrer - Partida
meredith - Universo
"""


class Mesa:
    def __init__(self):
        self.rodada = Rodada()
        
    def comeca(self):
        self.rodada.inicia()
          
class Jogador:
    def __init__(self):
        self.jogador = Jogador()
        self.ficar = Ficar()
        self.joias = Joias()
        self.sair = Sair()
    def decida(): 
        self.ficar.apresente()
        self.sair.apresente()
    def __init__(self):
        self.joias = Joias()
    def recebe():
        self.joia.retorna()
    
class Iniciar:
    def __init__(self):
        self.jogador = Jogador()
         
    def comeca(self):
        self.jogador.inicia()
        
if __name__ == "__main__":
    Mesa = Mesa()
    mesa.comeca()
