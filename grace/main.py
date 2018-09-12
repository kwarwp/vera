# vera.grace.main.py
from _spy.tesouro.main import  Gui
from _spy.tesouro.tesouro import  Jogo


def main(jogadores=JOGADORES, gui=GUI):
    class JogadorSimples:
        def __init__(self, joga, nome):
            _chance = list(range(20))
            shuffle(_chance)
            self.joga, self.jogadas, self.nome = joga, _chance, nome
            self._inicia(nome)

        def _inicia(self, jogador):
            get_joga = "from {mod}.main import {mod}; self.joga = {mod}()"
            try:
                exec(get_joga.format(mod=jogador))
                self.nome = self.nome.upper()
            except (ImportError, TypeError):
                self.joga = self._joga

        def _joga(self, _):
            return self.jogadas.pop() < 2

    return Jogo(gui=gui, jogadores=[JogadorSimples(None, jogador) for jogador in jogadores])

#print(main, Gui)
main(gui=Gui()).inicia()
