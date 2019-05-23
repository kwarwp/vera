# vera.heather.main.py
from _spy.vitollino.main import Cena
from elemento.main import Elemento

JARRA = "https://i.imgur.com/gdiuQ9G.jpg"
BICHO = "https://i.imgur.com/7JW6fup.jpg"
CENA_PARQUE = "https://i.imgur.com/woKKIiA.jpg"
parque = Cena(CENA_PARQUE)
bicho = Elemento(BICHO, x=100, y=100, w=60, h=40)
bicho.entra(parque)
jarra = Elemento(JARRA, x=100, y=200, w=60, h=40)
jarra.entra(parque)
jarra_b = Elemento(JARRA, x=180, y=280, w=60, h=40)
jarra_b.entra(parque)
parque.vai()

