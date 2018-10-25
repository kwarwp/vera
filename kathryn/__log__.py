
{'date': 'Thu Oct 25 2018 11:50:53.479 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
'error': '''
 module <string> line 29
  if __name__ == "__main__"
                            ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Oct 25 2018 11:52:53.645 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
'error': '''
 module <string> line 35
  self.jogador = Jogador()
  ^
IndentationError: expected an indented block
'''},
{'date': 'Thu Oct 25 2018 11:54:01.563 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
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
    from ruzwana.main import Turno
  module ruzwana.main line 2
    from ruzwana.main import Perigo
ImportError: cannot import name 'Perigo'

ImportError
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 264
    action()
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 2
    from ruzwana.main import Turno
  module ruzwana.main line 2
    from ruzwana.main import Perigo
'''},
{'date': 'Thu Oct 25 2018 11:56:50.103 GMt-0300 (Hora oficial do Brasil) -X- SuPyGirls -X-',
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
    from ruzwana.main import Turno
ImportError: cannot import name 'Turno'
'''},