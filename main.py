import forca
import adivinhacao

print("*********************************")
print("********Escolha um jogo!*********")
print("*********************************")

print("(1) Forca (2) Advinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("jogando forca")
    forca.jogar()
elif(jogo == 2):
    print("jogando advinhação")
    adivinhacao.jogar()
