# vera.kristen.main.py
from _spy.vitollino.main import Cena
TEMPLO = "https://i.imgur.com/dQqwYul.jpg"
TESOURO = "https://i.imgur.com/Nq1hCeU.jpg"
FOGO = "https://i.imgur.com/A6Z2zqB.jpg"
ARTEFATO1 = "https://i.imgur.com/1QHNdyI.jpg"
COBRA = "https://i.imgur.com/MydpgBT.jpg"
DESABAMENTO = "https://i.imgur.com/jnxWklS.jpg"
MUMIA = "https://i.imgur.com/3215w01.jpg" 
ARANHA = "https://i.imgur.com/JjEFJg0.jpg"
def decisao (anterior,carta):
    resposta = input ("Você descobriu uma câmara do templo. Você entra nela ou sai?")
    if resposta == "entro": 
        carta.vai() 
    elif resposta == "saio":
        anterior.vai()
templo = Cena(TEMPLO)
tesouro = Cena(TESOURO, esquerda=templo)
templo.direita = tesouro
fogo = Cena(FOGO, esquerda=tesouro)
tesouro.direita = fogo
artefato1 = Cena(ARTEFATO1, esquerda=fogo)
fogo.direita = artefato1
cobra = Cena(COBRA, esquerda=artefato1)
artefato1.direita = cobra
desabamento = Cena(DESABAMENTO, esquerda=cobra)
cobra.direita = desabamento
mumia = Cena(MUMIA, esquerda=desabamento)
desabamento.direita = mumia



# decisao(tesouro, fogo)




