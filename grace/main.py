# vera.grace.main.py
from _spy.tesouro.main import  Gui, JOGADORES
from _spy.tesouro.tesouro import  Jogo
from random import shuffle


def main(jogadores=JOGADORES, gui=None):
    class JogadorSimples:
        def __init__(self, joga, nome):
            _chance = list(range(20))
            shuffle(_chance)
            self.joga, self.jogadas, self.nome = joga, _chance, nome
            self._inicia(nome)

        def _inicia(self, jogador):
            get_joga = "from {mod}.main import {mod}; self.joga = {mod}().joga"
            try:
                exec(get_joga.format(mod=jogador))
                self.nome = self.nome.upper()
            except (ImportError, TypeError):
                self.joga = self._joga

        def _joga(self, _):
            return (self.jogadas.pop() < 2) if self.jogadas else True
            
    gui.inicia()
    return Jogo(gui=gui, jogadores=[JogadorSimples(None, jogador) for jogador in jogadores])

#print(main, Gui)
main(gui=Gui()).inicia()
