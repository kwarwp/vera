# vera.morgan.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
from rachel.main import Florestabanana

FLORESTA = "https://i.imgur.com/wBw3Lyl.jpg"
LEAO = "https://i.imgur.com/4gXpvfQ.png"
class FlorestaLeao:
   def __init__(self):
       floresta_banana = Florestabanana()
       self.floresta_inicio = Cena(FLORESTA, direita=floresta_banana)
       leao = Elemento(LEAO, style=dict(left="150px",width="100px"))
       leao.entra(self.floresta_inicio)

   def vai(self):
       self.floresta_inicio.vai()

if __name__ == "__main__":
   a_floresta = FlorestaLeao()
   a_floresta.vai()

