# vera.meredith.main.py
from lisa.main import Partida
"""
kathryn - Baralho - Joias - Rodada
callie - Perigo - Perder - Tesouro
ruzwana - Ficar - Turno - Sair
natalia - Mesa - Iniciar - Jogador
lisa - Decisao - Morrer - Partida
meredith - Universo
"""


class Universo:
    def __init__(self):
        self.partida = Partida()
        
    def comeca(self):
        self.partida.inicia()
        
        
if __name__ == "__main__":
    universo = Universo()
    universo.comeca()