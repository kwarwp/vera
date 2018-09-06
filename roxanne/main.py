# vera.roxanne.main.py
from random import shuffle


class Jogador:
    def __init__(self):
        self.chance = list(range(20))

    def joga(self):
        desiste = self.chance.pop() < 2 if self.chance else True
        return desiste


def roxanne():
    return Jogador()