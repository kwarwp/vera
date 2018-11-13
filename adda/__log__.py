
{'date': 'Tue Nov 13 2018 10:26:03.994 GMt-0200 (Brasilia Summer Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  def preload (self)
                     ^
SyntaxError: invalid syntax
'''},
{'date': 'Tue Nov 13 2018 10:27:47.100 GMt-0200 (Brasilia Summer Time) -X- SuPyGirls -X-',
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
  module <module> line 52
    Main()
  module <module> line 6
    self.config = {
NameError: name 'width' is not defined
'''},