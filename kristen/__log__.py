
{'date': 'Tue Nov 13 2018 08:43:25.803 GMt-0200 (Brasilia Summer Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 45
  puz.bind("click", lambda *_: doc["pydiv"].html = "")
                                                 ^
SyntaxError: can't assign to function call 
'''},
{'date': 'Tue Nov 13 2018 08:53:10.803 GMt-0200 (Brasilia Summer Time) -X- SuPyGirls -X-',
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
  module <module> line 43
    re1 = svg.RECTANGLE(x=100, y=100,width=50, height=30, style=dict(fill="#55ff55"))
AttributeError: 'module' object has no attribute 'RECTANGLE'
'''},