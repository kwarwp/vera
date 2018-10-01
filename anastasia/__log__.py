
{'date': 'Mon Oct 01 2018 18:11:52.285 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 34
  inicio():    
           ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Oct 01 2018 18:12:09.691 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 34
    inicio()    
  module <module> line 22
    maxsteel=Elemento(img=MAXSTELL,tit="MaxSteel",style=dict(left=150,top=160,width=160,height=200))
NameError: name 'MAXSTELL' is not defined
'''},