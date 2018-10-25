
{'date': 'Thu Oct 25 2018 11:38:25.898 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
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
  module <module> line 2
    from lisa.main import Partida
  module lisa.main line 19
    if __lisa__ == "__main__":
NameError: name '__lisa__' is not defined
'''},
{'date': 'Thu Oct 25 2018 11:41:05.274 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
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
  module <module> line 22
    universo = Universo()
  module <module> line 15
    self.partida = Partida()
  module lisa.main line 15
    self.rodada = Rodada() 
TypeError: 'module' object is not callable
'''},
{'date': 'Thu Oct 25 2018 11:59:56.560 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
'error': '''Partida __init__
Traceback (most recent call last):
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
  module <module> line 22
    universo = Universo()
  module <module> line 15
    self.partida = Partida()
  module lisa.main line 16
    self.rodada = Rodada() 
  module kathryn.main line 44
    self.baralho = Baralho()
  module kathryn.main line 20
    self.perigo = Perigo()
TypeError: 'module' object is not callable
'''},