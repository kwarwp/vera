# vera.ruzwana.main.py
from callie.main import Perigo
"""
kathryn - Baralho - Joias - Rodada
callie - Perigo - Perder - Tesouro
ruzwana - Ficar - Turno - Sair
natalia - Mesa - Iniciar - Jogador
lisa - Decisao - Morrer - Partida
meredith - universo
"""
class Turno:
    def _init_(self):
        self.perigo = Perigo()
        
    def apresente(self):
        self.perigo.apresente()
        
class Ficar:
    def _init_(self):
        self.Mesa = Mesa()
        
    def apresente(self):
        self.Mesa.apresente()
        
class Sair:
    def _init_(self):
        self.Mesa = Mesa()
        
    def apresente(self):
        self.Mesa.apresente()
        
if __name__ == "_main_":
    mesa = mesa()
    mesa.apresente()
    