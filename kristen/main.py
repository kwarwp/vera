# vera.kristen.main.py
from _spy.vitollino.main import Cena
from random import shuffle

IMAGENS = ["TEMPLO", "TESOURO", "FOGO", "ARTEFATO1", "COBRA", "DESABAMENTO", "MUMIA", "ARANHA"]
DI = DICIONARIO_DE_IMAGENS = {}
DI["TEMPLO"] = "https://i.imgur.com/LXptu0U.jpg"
DI["TESOURO"] = "https://i.imgur.com/Nq1hCeU.jpg"
DI["FOGO"] = "https://i.imgur.com/KRK66bR.jpg"
DI["ARTEFATO1"] = "https://i.imgur.com/1QHNdyI.jpg"
DI["COBRA"] = "https://i.imgur.com/MydpgBT.jpg"
DI["DESABAMENTO"] = "https://i.imgur.com/jnxWklS.jpg"
DI["MUMIA"] = "https://i.imgur.com/HPp1k5T.jpg" 
DI["ARANHA"] = "https://i.imgur.com/w90m1jf.jpg"

class Inca:
    def inicia(self):
        templo = Cena(DI["TEMPLO"])
        tesouro = Cena(DI["TESOURO"])
        fogo = Cena(DI["FOGO"])
        artefato1 = Cena(DI["ARTEFATO1"])
        cobra = Cena(DI["COBRA"])
        desabamento = Cena(DI["DESABAMENTO"])
        mumia = Cena(DI["MUMIA"])
        aranha = Cena(DI["ARANHA"])

inca = Inca()

if __name__ == "__main__":
    inca.inicia()


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

# templo = Cena(TEMPLO)
#templo.vai()
#tesouro = Cena(TESOURO)
#fogo = Cena(FOGO)
#artefato1 = Cena(ARTEFATO1)
#cobra = Cena(COBRA)
#desabamento = Cena(DESABAMENTO)
#mumia = Cena(MUMIA)
#aranha = Cena(ARANHA)

#cartas = [TESOURO(), ARTEFATO1(), FOGO(), MUMIA(), DESABAMENTO(), ARANHA(), COBRA()]
#baralho = cartas[:] # Copy cartas
#shuffle(baralho) # Shuffle baralho
#for elemento in cartas:
 #   elemento.vai()

def decisao (anterior,carta):
    resposta = input ("Você descobriu uma câmara do templo. Você entra nela ou sai?")
    if resposta == "entro": 
        carta.vai() 
    elif resposta == "saio":
        anterior.vai()

# decisao(tesouro, fogo)

