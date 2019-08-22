# vera.kristen.main.py
from _spy.vitollino.main import Cena
TEMPLO ="https://i.imgur.com/dQqwYul.jpg"
ACAMPAMENTO = "https://i.imgur.com/ba43tjx.jpg"
MOCHILA = "https://i.imgur.com/sTWdwDV.png"
TESOURO = "https://i.imgur.com/Nq1hCeU.jpg"
FOGO = "https://i.imgur.com/A6Z2zqB.jpg"
ARTEFATO1 = "https://i.imgur.com/1QHNdyI.jpg"
COBRA = "https://i.imgur.com/MydpgBT.jpg"
DESABAMENTO = "https://i.imgur.com/jnxWklS.jpg"
MUMIA = "https://i.imgur.com/3215w01.jpg" 
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
tesouro0 = Cena(TESOURO, esquerda=cobra)
cobra.direita = tesouro0
tesouro0.vai()
desabamento = Cena(DESABAMENTO, esquerda=tesouro0)
tesouro0.direita = desabamento
desabamento.vai()
tesouro1 = Cena(TESOURO, esquerda=desabamento)
desabamento.direita = tesouro1
tesouro1.vai()
tesouro2 = Cena(TESOURO, esquerda=tesouro1)
tesouro1.direita = tesouro2
tesouro2.vai()
mumia = Cena(MUMIA, esquerda=tesouro2)
tesouro2.direita = mumia
mumia.vai()
tesouro3 = Cena(TESOURO, esquerda=mumia)
munia.direita = tesouro3
tesouro3.vai()
fogo = Cena(FOGO, esquerda=tesouro3)
tesouro3.direita = fogo
fogo.vai()

