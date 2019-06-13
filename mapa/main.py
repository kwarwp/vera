# vera.mapa.main.py
from _spy.vitollino.main import Cena, STYLE
from elemento.main import Elemento
STYLE["width"] = 900
STYLE["heigth"] = "900px"

CENA_MAPA = "https://i.imgur.com/4d2spVj.jpg"
CLICAR = "https://i.imgur.com/U8kaaKl.jpg"


class mapaParque:
    def __init__(self):
        mapa = Cena(CENA_MAPA)
        mapa.vai()
        
mapaParque()
      