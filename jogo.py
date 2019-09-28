import random


def jogar():
    print("*************************************")
    print("Ola mundo. Este é meu primeiro jogo.")
    print("*************************************")

    print("Qual o nivel de dificuldade? 1 - 2 - 3")
    nivel = int(input("=> "))

    if (nivel == 1):
        total_tentativas = 3
    elif (nivel == 2):
        total_tentativas = 8
    elif (nivel == 3):
        total_tentativas = 13

    numero_secreto = random.randrange(1, 101)

    for rodada in range(1, total_tentativas + 1):
        print("Rodada {} de {}".format(rodada, total_tentativas))
        chute = input("Digite seu número secreto => ")
        chute = int(chute)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100")
            continue

        print("Você digitou => ", chute)

        acertou = (numero_secreto == chute)
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(acertou):
            print("Você acertou")
            break
        elif(maior):
            print("Você errou pra mais")
        elif(menor):
            print("Você errou pra menos")
        else:
            print("erro")

    print("O número secreto era {}".format(numero_secreto))
    print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()