# vera.cavernatesouro.main.py
from _spy.vitollino.main import Cena, STYLE, Codigo, Texto
STYLE["width"], STYLE["height"] = 1200, "650px"
from elemento.main import Elemento
CAVERNATESOURO = "https://i.imgur.com/RgatDJ4.jpg"
TESOURO = "https://i.imgur.com/8YK3cfO.png"
cavernatesouro = Cena(CAVERNATESOURO)
cavernatesouro.vai()
codigo = Codigo ("", "",cena = cavernatesouro, style = dict( x= 400, y= 300))
tesouro = Elemento (TESOURO, cena = cavernatesouro, x= 600, y= 320, w= 200, h= 200)codigo = Texto (cavernatesouro, "Opa!! Você achou o tesouro!!",
"Mas, cuidado: ao decidir pegar o tesouro, seu amigo não poderá ser salvo",
style = dict( x= 400, y= 300), foi=tesouro.vai)
cavernatesouro.meio = codigo
