# vera.lisa.main.py
from kathryn.main import Rodada 
"""
kathryn - Baralho - Joias - Rodada
callie - Perigo - Perder - Tesouro
ruzwana - Ficar - Turno - Sair
natalia - Mesa - Iniciar - Jogador
lisa - Decisão - Morrer - Partida
meredith - Universo
"""


class Partida:
    def __init__(self):
        print("Partida __init__")
        self.rodada = Rodada() 
        
    def inicia(self):     
        self.rodada.comeca()
if __name__ == "__main__":
    partida = Partida()
    partida.inicia()
    
        
        
        
        