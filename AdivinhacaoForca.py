import forca
import adivinhacao

print("******************************************")
print("************** Vamos Jogar ***************")
print("******************************************")

print("1 - Forca", "2 - Adivinhação")

jogo = int(input("Escolha seu jogo!"))

if jogo == 1:
    forca.jogar()

elif jogo == 2:
    adivinhacao.jogar()


