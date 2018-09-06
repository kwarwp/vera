
{'date': 'Thu Sep 06 2018 07:16:11.614 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 406
    Jogo().inicia()
  module <module> line 399
    self.mesa = Mesa(jogadores)
  module <module> line 329
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 274
    self.jogador = self.inicia(jogador)
  module <module> line 279
    except TypeError:
NameError: name 'GET_JOGADOR' is not defined
'''},
{'date': 'Thu Sep 06 2018 08:08:59.649 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 463
    Jogo().inicia()
  module <module> line 456
    self.mesa = Mesa(jogadores)
  module <module> line 386
    self.jogadores_ativos = self.jogadores = [Jogador(jogador, self) for jogador in jogadores]
  module <module> line 277
    self.inicia()
TypeError: inicia() missing 1 positional argument: jogador
'''},