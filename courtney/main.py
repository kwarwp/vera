# vera.courtney.main.py 
from random import shuffle
"0:roxanne 1:libby 2:sara 3:kellee 4:courtney 5:angie 6:naomi 7:tracy 8:morgan"

class Jogador:
    def __init__(self):
        self.chance = list(range(30))
        self.perigos, self.artefatos, self.cartas, self.rodada_corrente,\
        self.maior_tesouro, self.maior_joias, = [0]*10
        self.jogadores_jogando, self.tesouros_na_tenda, self.cartas_na_mesa,\
        self.tesouros_na_mesa, self.tesouros_jogadores, self.joias_jogadores = [[]]*10

    def joga(self, mesa):
        self.perigos, self.artefatos, self.cartas, self.rodada_corrente,\
        self.maior_tesouro, self.maior_joias,\
        self.jogadores_jogando, self.tesouros_na_tenda, self.cartas_na_mesa,\
        self.tesouros_na_mesa, self.tesouros_jogadores, self.joias_jogadores = mesa.atualiza()
        coragem = self.perigos > 4
        cobica = self.artefatos > 3
        cautela = self.cartas > 10
        ambicao = self.maior_tesouro > self.tesouros_jogadores[7]        
        sorte = self.chance.pop() < 2 if self.chance else True
        #return coragem or cobica or cautela or ambicao or sorte
        return ambicao or coragem


def courtney():
    return Jogador()