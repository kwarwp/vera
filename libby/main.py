# vera.libby.main.py
from random import shuffle


class Jogador:
    def __init__(self):
        self.chance = list(range(30))
        shuffle(self.chance)

    def joga(self, mesa):
        desiste = self.chance.pop() < 2 if self.chance else True
        return desiste


def libby():
    return Jogador()