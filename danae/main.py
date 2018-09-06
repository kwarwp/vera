# vera.danae.main.py
# evelyn.danae.main.py
# ! /usr/bin/env python
# -*- coding: UTF8 -*-
# Este arquivo é parte do programa SuperPython
# Copyright 2013-2015 Carlo Oliveira <carlo@nce.ufrj.br>,
# `Labase <http://labase.selfip.org/>`__; `GPL <http://is.gd/3Udt>`__.
#
# SuperPython é um software livre; você pode redistribuí-lo e/ou
# modificá-lo dentro dos termos da Licença Pública Geral GNU como
# publicada pela Fundação do Software Livre (FSF); na versão 2 da
# Licença.
#
# Este programa é distribuído na esperança de que possa ser útil,
# mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
# a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
# Licença Pública Geral GNU para maiores detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa, se não, veja em <http://www.gnu.org/licenses/>

"""Módulo principal do Tesouro Inca.
.. moduleauthor:: Carlo Oliveira <carlo@nce.ufrj.br>
"""
from random import shuffle

from browser import timer

#from vitollino.main import Elemento, Cena, Codigo, STYLE

from _spy.vitollino.main import Elemento, Cena, Codigo, STYLE

STYLE["width"] = 800

DESISTE = True
PERIGOS = "aranha mumia desabe fogo cobra".split()
ARTEFATOS = "estatua vaso broche colar adorno".split()
TESOUROS = "1 2 3 3 4 5 7 9 9 11 13 14 14 15 17".split()
JOGADORES = tuple("Roxanne Stacy Libby Sara Kellee Courtney".split())
SPLASH = "https://activufrj.nce.ufrj.br/studio/Introducao_a_Computacao/" \
         "Untitled_20180828_105833-0.jpg?disp=inline&size=G"
ACTIVE = "http://activufrj.nce.ufrj.br/studio/"
POS = "?disp=inline&size=G"
TEMPLOTRAS1 = ACTIVE + "Introducao_a_Computacao/Untitled_20180828_110147.jpg" + POS
IMGS = dict(
    PEDRAS4="Introducao_a_Computacao/Untitled_20180828_102220.jpg",
    PEDRAS1="Introducao_a_Computacao/Untitled_20180828_105412.jpg",
    PEDRAS3="Introducao_a_Computacao/Untitled_20180828_105419.jpg",
    PEDRAS2="Introducao_a_Computacao/Untitled_20180828_105624.jpg",
    TEMPLOTRAS1="Introducao_a_Computacao/Untitled_20180828_110147.jpg",
    TEMPLOTRAS2="Introducao_a_Computacao/Untitled_20180828_110148.jpg",
    TEMPLOTRAS3="Introducao_a_Computacao/Untitled_20180828_110145.jpg",
    CARTASENTRAESAI="Introducao_a_Computacao/Untitled_20180828_105727.jpg",
    CARTASENTRAESAITRAS="Introducao_a_Computacao/Untitled_20180828_105833-0.jpg",
    CARTASTRAS="Introducao_a_Computacao/Untitled_20180828_105833-2.jpg",
    ARTEFATOS1="Introducao_a_Computacao/Untitled_20180828_105529.jpg",
    ARTEFATOS2="Introducao_a_Computacao/Untitled_20180828_105528.jpg",
    MOSTROS="Introducao_a_Computacao/Untitled_20180828_105623.jpg",
    MOSTROS1="Introducao_a_Computacao/Untitled_20180828_105627.jpg"

)
IMGS = {key: ACTIVE + img + POS for key, img in IMGS.items()}
SPRITES = dict(
    desabe=(IMGS["MOSTROS"], 0), aranha=(IMGS["MOSTROS"], 1), cobra=(IMGS["MOSTROS"], 2),
    fogo=(IMGS["MOSTROS1"], 0), mumia=(IMGS["MOSTROS1"], 1),
    estatua=(IMGS["ARTEFATOS1"], 0), vaso=(IMGS["ARTEFATOS1"], 1), broche=(IMGS["ARTEFATOS1"], 2),
    colar=(IMGS["ARTEFATOS2"], 0), adorno=(IMGS["ARTEFATOS2"], 1), decide=(IMGS["CARTASENTRAESAI"], 1),
    t1=(IMGS["PEDRAS1"], 0), t2=(IMGS["PEDRAS1"], 1), t4=(IMGS["PEDRAS1"], 2), t5=(IMGS["PEDRAS2"], 0),
    t7=(IMGS["PEDRAS2"], 1), t3=(IMGS["PEDRAS2"], 2), t9=(IMGS["PEDRAS3"], 0), t11=(IMGS["PEDRAS3"], 1),
    t13=(IMGS["PEDRAS3"], 2), t14=(IMGS["PEDRAS4"], 0), t15=(IMGS["PEDRAS4"], 1), t17=(IMGS["PEDRAS4"], 2),
)
SPRITES = {key: dict(img=img, index=ind, tit=key) for key, (img, ind) in SPRITES.items()}
FASES = dict(f1=(IMGS["TEMPLOTRAS1"], 1), f2=(IMGS["TEMPLOTRAS1"], 0),
             f3=(IMGS["TEMPLOTRAS2"], 1), f4=(IMGS["TEMPLOTRAS2"], 0),
             f5=(IMGS["TEMPLOTRAS3"], 0, 800))


class Sprite(Elemento):
    def __init__(self, img, index=0, tit="", w=70, h=120, delta=210):
        super().__init__(img, style=dict(position="relative", float="left", tit=tit,
                                         width=w, height="{}px".format(h), overflow="hidden"))
        self.img.style.marginLeft = "-{}px".format(index * w)
        self.img.style.width = self.img.style.maxWidth = "{}px".format(delta)
        self.nome = "n{}".format(tit)
        "210px"
        self.w = w
        self._mostrador = None
        self._mostra = self._cria_mostra

    def __le__(self, item):
        self.elt <= item.elt

    def _cria_mostra(self, valor):
        self._mostrador = Mostrador(valor, self)
        self._mostra = self._so_mostra

    def _so_mostra(self, valor):
        self._mostrador.mostra(valor)

    def mostra(self, valor):
        self._mostra(valor)

    def face(self, index):
        self.img.style.marginLeft = "-{}px".format(index * self.w)


class Mostrador(Codigo):
    def __init__(self, display, cena):
        super().__init__(display, cena=cena)

    def mostra(self, valor):
        self._code.html = valor


class Cenario(Cena):
    def __init__(self, img, index=0, delta=1600, w=800, h=700):
        super().__init__(img)
        self.elt.style.width = w
        self.elt.style.height = "{}px".format(h)
        self.elt.style.overflow = "hidden"

        self.img.style.marginLeft = "-{}px".format(index * w)
        self.img.style.width = self.img.style.maxWidth = "{}px".format(delta)
        "210px"
        self.w = w

    def face(self, index):
        self.img.style.marginLeft = "-{}px".format(index * self.w)


class Gui:
    def __init__(self):
        self._parte = {}
        self._carta = {}

    def cena(self, imagem):
        self._parte[imagem] = cena = Cenario(**FASES[imagem])
        cena.vai()
        return cena

    def carta(self, imagem, tit=""):
        sprite = SPRITES[imagem if imagem.isalpha() else "t{}".format(imagem)]
        if tit:
            sprite.update(tit=tit)
        self._carta[imagem] = carta = Sprite(**sprite)
        return carta


GUI = Gui()


class Carta(object):
    PERIGO = []
    VALOR = 2

    def __init__(self, face):
        self.face = face
        self.valor = int(face) if face.isdigit() else 0
        self.elt = GUI.carta(face)

    def premia(self, jogadores, _):
        return True

    def inicia(self):
        self.valor = int(self.face) if self.face.isdigit() else 0

    def mostra(self):
        return True

    def atualiza_saldo(self, divider):
        self.valor %= divider
        self.mostra()

    def divide(self, jogadores, salas):
        for sala in salas:
            self.divide_valor(jogadores, sala)

    def divide_valor(self, jogadores, sala):
        divider = len(jogadores)
        if divider == 0:
            return True
        for jogador in jogadores:
            jogador.recebe(sala.valor // divider)
        sala.valor %= divider
        return True

    def entra(self, cena):
        cena.elt <= self.elt.elt

    def __eq__(self, carta):
        # print("carta.face == self.face", carta.face == self.face, carta.face, self.face)
        return carta.face == self.face


class Perigo(Carta):
    def divide(self, jogadores, salas):
        _ = jogadores
        return self not in salas


class Artefato(Carta):

    def __init__(self, face):
        super().__init__(face)
        self.valor = 10  # // Carta.VALOR
        self.elt.mostra(":{}:".format(self.valor))

    def atualiza_saldo(self, divider):
        pass

    def divide_valor(self, jogadores, salas):
        if len(jogadores) == 1:
            jogadores[0].recebe(self.valor)
            self.valor = 0
            self.mostra()
        return True

    def mostra(self):
        self.elt.mostra(":{}:".format(self.valor))
        return True


class Tesouro(Carta):

    def __init__(self, face):
        super().__init__(face)
        self.elt.mostra(":{}:".format(self.valor))

    def premia(self, jogador, cota):
        jogador.recebe(self.valor // cota)
        # self.valor %= cota
        return True

    def mostra(self):
        self.elt.mostra(":{}:".format(self.valor))
        return True


class Baralho(object):
    def __init__(self):
        self.cartas = []
        self.monta_baralho()

    def embaralha(self, artefato):
        self.cartas.append(Artefato(face=artefato))
        [carta.inicia() for carta in self.cartas]
        shuffle(self.cartas)

    def descarta(self):
        return self.cartas.pop() if self.cartas else None

    def monta_baralho(self):
        self.cartas = []
        for perigo in PERIGOS * 3:
            self.cartas.append(Perigo(face=perigo))
        for tesouro in TESOUROS:
            self.cartas.append(Tesouro(face=tesouro))

    def extend(self, salas):
        self.cartas.extend(salas)


class Jogador(object):
    def __init__(self, jogador, mesa):
        self.sprite = GUI.carta('decide', tit=jogador)
        self.cena = mesa.acampamento
        self.sprite.mostra("0:0")
        self.tesouro = 0
        self.entra(self.cena)
        self.jogador = "from {mod}.main import {mod}, self.jogador = {mod}()".format(mod=jogador)
        self.jogada, self.joias, self.mesa = None, 0, mesa
        self.chance = list(range(20))
        shuffle(self.chance)
        self.jogador = self.inicia(jogador)

    def inicia(self, jogador):
        try:
            exec(GET_JOGADOR.format(mod=jogador))
        except TypeError:
            self.jogador = self

    def entra(self, cena=None):
        # self.chance = list(range(12))
        self.joias = 0
        self.sprite.mostra("{}:{}".format(self.tesouro, self.joias))
        self.sprite.face(1)
        cena = cena if cena else self.cena
        self.sprite.entra(cena)

    def recebe(self, joias):
        self.joias += joias
        self.sprite.mostra("{}:{}".format(self.tesouro, self.joias))

    def joga(self, mesa):
        return self.chance.pop() < 2 if self.chance else True

    def decide(self):
        desiste = self.jogador.joga(self.mesa)
        if desiste:
            self.tesouro += self.joias
            self.joias = 0
            self.sprite.mostra("{}:{}".format(self.tesouro, self.joias))
            self.sprite.face(0)
        return desiste

    def __joga(self):
        try:
            return self.jogada(self.mesa)
        except TypeError:
            exec(self.jogador)
            return self.jogada(self.mesa)


class Mesa(object):
    def __init__(self, jogadores):
        self.rodada_corrente = 0
        self.interval = None
        Cena(SPLASH).vai()
        self.fases = [Cenario(IMGS["TEMPLOTRAS1"], 1), Cenario(IMGS["TEMPLOTRAS1"], 0),
                      Cenario(IMGS["TEMPLOTRAS2"], 1), Cenario(IMGS["TEMPLOTRAS2"], 0),
                      Cenario(IMGS["TEMPLOTRAS3"], 0, 800)]
        self.mesa = self.fases[self.rodada_corrente]
        self.baralho = Baralho()
        # self.mesa = Cena(IMGS["TEMPLOTRAS3"])
        self.acampamento = Elemento("", style=dict(left=0, top=0, width=800, height="130px"))
        self.labirinto = Elemento("", style=dict(left=0, top=140, width=800, height="400px"))
        self.acampamento.nome = "Acampa"
        self.labirinto.nome = "Explora"
        self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
        self.perigo = self.salas = []
        # self.inicia()

    def inicia(self):
        timer.set_timeout(self.rodada, 2000)
        # self.rodada(ARTEFATOS[0])

    def inicia_(self):
        self.mesa.vai()
        for artefato in ARTEFATOS:  # [:1]:
            self.baralho.extend([Artefato(artefato)])
        while self.baralho.cartas:
            self.apresenta(self.baralho.cartas.pop())

    def _inicia(self):
        self.mesa.vai()
        for _ in ARTEFATOS:  # [:1]:
            self.rodada()

    def rodada(self):
        artefato = ARTEFATOS[self.rodada_corrente]
        self.mesa = self.fases[self.rodada_corrente]  # )
        self.mesa.vai()
        self.acampamento.entra(self.mesa)
        self.labirinto.entra(self.mesa)
        self.labirinto.elt.html = ''
        self.jogadores_ativos = self.jogadores[:]
        [jogador.entra() for jogador in self.jogadores]
        self.baralho.extend(self.salas)
        self.baralho.embaralha(artefato)
        self.perigo = self.salas = []
        self.interval = timer.set_interval(self.turno, 500)
        self.rodada_corrente += 1
        return
        # while self.turno():
        #     pass
        # self.salas = [carta for carta in self.salas if not isinstance(carta, Artefato)]

    def apresenta(self, carta):
        self.salas.append(carta)
        carta.entra(self.labirinto)

    def turno(self):
        carta_corrente = self.baralho.descarta()
        if (not carta_corrente) or (carta_corrente in self.salas):
            carta_corrente.entra(self.labirinto)
            timer.clear_interval(self.interval)
            if self.rodada_corrente < 5:
                timer.set_timeout(self.rodada, 2000)
            return False
        jogadores_saindo = []
        self.apresenta(carta_corrente)
        ativos = len(self.jogadores_ativos)
        for jogador in self.jogadores_ativos:
            for carta in self.salas:
                carta.premia(jogador, ativos)
            if jogador.decide() == DESISTE:
                self.jogadores_ativos.remove(jogador)
                jogadores_saindo.append(jogador)
        carta_corrente.atualiza_saldo(ativos)
        carta_corrente.divide(jogadores_saindo, self.salas)
        if not self.jogadores_ativos:
            timer.clear_interval(self.interval)
            if self.rodada_corrente < 5:
                timer.set_timeout(self.rodada, 2000)


class Jogo:
    def __init__(self, jogadores=JOGADORES):
        self.mesa = Mesa(jogadores)

    def inicia(self):
        self.mesa.inicia()


if __name__ == '__main__':
    Jogo().inicia()
