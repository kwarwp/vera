
{'date': 'Thu May 02 2019 08:47:07.143 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 4
    from elemento.main import elemento
ImportError: cannot import name 'elemento'

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
  module <module> line 4
    from elemento.main import elemento
'''},
{'date': 'Thu May 02 2019 08:47:33.805 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 68
    a_floresta = FlorestaFaca()
  module <module> line 61
    faca = Faca(self.floresta_inicio)
  module <module> line 31
    self.faca = Elemento(FACA, style=dict(left="200px", width="80px"), vai=self.pega)
  module elemento.main line 35
    self.elt = html.DIV(Id=tit + drop, title=tit, style=self.style)
TypeError: Can't convert dict to str implicitely
'''},
{'date': 'Thu May 02 2019 08:56:52.160 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 34
  self.faca = Elemento(FACA, x=800, y=600, w=80 vai=self.pega)
                                                 ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu May 02 2019 09:21:29.640 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 33
  self.faca = Elemento(FACA, tit="faca" x=600, y=500, w=80, vai=self.pega)
                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri May 03 2019 16:26:02.622 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 82
    a_floresta = FlorestaFaca()
  module <module> line 75
    faca = Faca(self.floresta_inicio)
  module <module> line 34
    style = {'opacity': "inherited", 'width': 30, 'height': "30px", 'min-height': '30px', 'float': 'left',
AttributeError: 'Faca' object has no attribute 'img'
'''},
{'date': 'Sat May 04 2019 12:26:24.370 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module elemento.main line 27
  self.style.update(**{'position': 'absolute', 'overflow': 'hidden',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Jun 27 2019 10:36:58.991 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 82
    a_floresta = FlorestaFaca()
  module <module> line 71
    esquerda = esquerda or floresta_banana
NameError: name 'floresta_banana' is not defined
'''},
{'date': 'Thu Jun 27 2019 10:53:58.782 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 77
  self.corda = Elemento (CORDA, tit="corda", cena = self.floresta_inicio, x=650, y=350. vai=self.guardacorda)
                                                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Jun 27 2019 10:56:42.412 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 77
  self.corda = Elemento (CORDA, tit="corda", cena = self.floresta_inicio, x=650, y=350 vai=self.guardacorda)
                                                                                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Thu Jul 14 2022 10:37:00.29 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 100
    a_floresta = FlorestaFaca()
  module <module> line 77
    faca = Faca(self.floresta_inicio)
  module <module> line 42
    self.faca = Elemento(FACA, tit="faca", x=600, y=500, w=80, vai=self.pega)
  module elemento.main line 18
    self.img, self.title, self.dropper, self.alt = img, tit, drop, alt
  module _spy.vitollino.main line 668
    self.elt.style.backgroundImage = "url({})".format(value)
AttributeError: 'Elemento' object has no attribute 'elt'
'''},