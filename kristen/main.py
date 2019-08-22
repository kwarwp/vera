# vera.kristen.main.py
from _spy.vitollino.main import Cena
TEMPLO ="https://i.imgur.com/dQqwYul.jpg"
ACAMPAMENTO = "https://i.imgur.com/ba43tjx.jpg"
TESOURO = "https://i.imgur.com/Nq1hCeU.jpg"
FOGO = "https://i.imgur.com/A6Z2zqB.jpg"
ARTEFATO1 = "https://i.imgur.com/1QHNdyI.jpg"
COBRA = "https://i.imgur.com/MydpgBT.jpg"
DESABAMENTO = "https://i.imgur.com/jnxWklS.jpg"
templo = Cena(TEMPLO)
templo.vai()
acampamento = Cena(ACAMPAMENTO, esquerda=templo)
templo.direita = acampamento
acampamento.vai()
tesouro = Cena(TESOURO, esquerda=acampamento)
acampamento.direita = tesouro
tesouro.vai()
fogo = Cena(FOGO, esquerda=tesouro)
tesouro.direita = fogo
fogo.vai()
artefato = Cena(ARTEFATO1, esquerda=fogo)
fogo.direita = artefato
artefato.vai()
cobra = Cena(COBRA, esquerda=artefato)
artefato.direita = cobra
cobra.vai()
tesouro = Cena(TESOURO, esquerda=cobra)
cobra.direita = tesouro
tesouro,vai()
desabamento = Cena(DESABAMENTO, esquerda=tesouro)
tesouro.direita = desabamento
desabamento.vai()
