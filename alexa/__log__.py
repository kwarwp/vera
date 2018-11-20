
{'date': 'Tue Nov 20 2018 12:57:44.560 GMt-0200 (Horário de Verão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 93
    main(MASMORRA)
  module <module> line 90
    return DesafioA(masmorra)
  module <module> line 40
    self.gamer = Braser(768, 640)
TypeError: 'module' object is not callable
'''},