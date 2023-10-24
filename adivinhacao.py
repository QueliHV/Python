import random
def jogar():

    print("***************************************")
    print("** Bem Vindo ao Jogo de Adivinhação ***")
    print("***************************************")


    numero_secreto = random.randrange(1, 101)
    rodada = 1
    limite_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade:", numero_secreto)
    print("(1) Fácil, (2) Médio, (3) - Difícil")

    nivel = int(input("Escolha um nível:"))

    if(nivel == 1):
        limite_tentativas = 20
    elif(nivel == 2):
        limite_tentativas = 10
    else:
        limite_tentativas = 5

    for rodada in range(rodada, limite_tentativas + 1):
        print("Rodada {} de {} ".format(rodada, limite_tentativas))

        chute = int(input("Digite um número entre 1 e 100:"))

        if (chute < 0 or chute > 100):
            continue

        acertou = chute == numero_secreto
        maior = chute < numero_secreto
        menor = chute > numero_secreto

        if(acertou):
            print("Você Acertou e fez {} pontos!".format(pontos))
            break
        elif(menor):
            print("Você errou o número é menor!")
        elif(maior):
            print("Você errou o número é maior")

        pontos_perdidos = abs(numero_secreto - chute)  #número absoluto, independente do sinal
        pontos = pontos - pontos_perdidos


    print("Fim de jogo!")


if(__name__ == "__main__"): #chamado diretamente por programa externo
    jogar()