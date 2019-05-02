
{'date': 'Thu May 02 2019 09:53:23.990 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 100
    o_universo = Universo()
  module <module> line 92
    self.universo = Cena(UNIVERSO, direita=floresta_leao)
NameError: name 'floresta_leao' is not defined
'''},
{'date': 'Thu May 02 2019 09:55:17.788 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 98
    o_universo = Universo()
  module <module> line 91
    terra = Terra(self.universo)
  module <module> line 61
    self.terra = Elemento(FACA, style=dict(left="200px", width="80px"), vai=self.pega)
NameError: name 'FACA' is not defined
'''},