
{'date': 'Thu Jun 27 2019 11:34:54.69 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 21
  redemoinho = Elemento(REDEMOINHO, cena=ilhamar, x=30, y=70, w=100
                       ^
SyntaxError: Unbalanced bracket (
'''},
{'date': 'Thu Jun 27 2019 11:46:30.928 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 23
  tubarao = Elemento(TUBARAO, cena=ilhamar, x=700, y= 500, w=150, style={"opacity"=0.2})
                                                                                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Jun 27 2019 11:48:50.83 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 23
    tubarao = Elemento(TUBARAO, cena=ilhamar, x=700, y= 500, w=150, style={"opacity":0.2}, vai=tub)
NameError: name 'tub' is not defined
'''},