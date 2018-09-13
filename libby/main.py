# vera.libby.main.py
from random import shuffle
"0:roxanne 1:libby 3:sara 4:kellee 5:courtney 6:angie 7:naomi 8:tracy 9:morgan"

class Jogador:
    def __init__(self):
        self.chance = list(range(20))
        self.perigos, self.artefatos, self.cartas, self.rodada_corrente,\
        self.maior_tesouro, self.maior_joias, = [0]*6
        self.jogadores_jogando, self.tesouros_na_tenda, self.cartas_na_mesa,\
        self.tesouros_na_mesa, self.tesouros_jogadores, self.joias_jogadores = [[]]*6

    def joga(self, mesa):
        self.perigos, self.artefatos, self.cartas, self.rodada_corrente,\
        self.maior_tesouro, self.maior_joias,\
        self.jogadores_jogando, self.tesouros_na_tenda, self.cartas_na_mesa,\
        self.tesouros_na_mesa, self.tesouros_jogadores, self.joias_jogadores = mesa.atualiza()
        medo = self.perigos > 4
        cobica = self.artefatos > 2
        cautela = self.cartas > 9
        ambicao = self.maior_tesouro > self.tesouros_jogadores[0]        
        sorte = self.chance.pop() < 2 if self.chance else True
        return medo or cobica or cautela or ambicao or sorte


def libby():
    return Jogador()