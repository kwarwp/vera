# vera.morgan.main.py
"http://supygirls.pythonanywhere.com"
from _spy.vitollino.main import Cena, Elemento
FLORESTA = "https://i.imgur.com/wBw3Lyl.jpg"
LEAO = "https://i.imgur.com/4gXpvfQ.png"
class FlorestaLeao:
   def __init__(self):
       self.floresta_inicio = cena(FLORESTA)
       leao = Elemento(LEAO, style=dict(left="150px",width="100px"))
       leao.entra(self.floresta_inicio)

   def vai(self):
       self.floresta_inicio.vai()

if __name__ == "__main__":
   a_floresta = FlorestaLeao()
   a_floresta_.vai()

