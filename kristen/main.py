# vera.kristen.main.py
from _spy.vitollino.main import Cena
TEMPLO ="https://i.imgur.com/dQqwYul.jpg"
ACAMPAMENTO = "https://i.imgur.com/ba43tjx.jpg"
TESOURO = "https://i.imgur.com/Nq1hCeU.jpg"
FOGO = "https://i.imgur.com/A6Z2zqB.jpg"
templo = Cena(TEMPLO)
templo.vai()
acampamento = Cena(ACAMPAMENTO, direita=templo)
templo.esquerda = acampamento
acampamento.vai()

