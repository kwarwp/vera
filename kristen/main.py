# vera.kristen.main.py
from _spy.vitollino.main import Cena
from random import shuffle
TEMPLO = "https://i.imgur.com/dQqwYul.jpg"
ACAMPAMENTO = "https://i.imgur.com/ba43tjx.jpg"
MOCHILA = "https://i.imgur.com/sTWdwDV.png"
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
RODADA = "Primeira Rodada"
templo = Cena(TEMPLO)
acampamento = Cena(ACAMPAMENTO, esquerda=templo)
templo.direita = acampamento
tesouro = Cena(TESOURO, esquerda=acampamento)
acampamento.direita = tesouro
fogo = Cena(FOGO, esquerda=tesouro)
# decisao(tesouro, fogo)
tesouro.direita = fogo
artefato = Cena(ARTEFATO1, esquerda=fogo)
fogo.direita = artefato
cobra = Cena(COBRA, esquerda=artefato)
artefato.direita = cobra
tesouro0 = Cena(TESOURO, esquerda=cobra)
cobra.direita = tesouro0
desabamento = Cena(DESABAMENTO, esquerda=tesouro0)
tesouro0.direita = desabamento
tesouro1 = Cena(TESOURO, esquerda=desabamento)
desabamento.direita = tesouro1
tesouro2 = Cena(TESOURO, esquerda=tesouro1)
tesouro1.direita = tesouro2
mumia = Cena(MUMIA, esquerda=tesouro2)
tesouro2.direita = mumia
tesouro3 = Cena(TESOURO, esquerda=mumia)
mumia.direita = tesouro3
aranha = Cena(ARANHA, esquerda=tesouro3)
tesouro3.direita = aranha
fogo2 = Cena(FOGO, esquerda=aranha)
aranha.direita = fogo2
baralho = [fogo, tesouro, aranha, mumia, artefato, desabamento, cobra]
shuffle(baralho)
umacarta = baralho[0]
umacarta.vai()

