import random

def jogar():

    boas_vindas()

    todas_as_letras = []
    erros = 0
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    for n in palavra_secreta:
        todas_as_letras.append("_")

    print(todas_as_letras)

    se_enforcou = False
    acertou = False

    while(not acertou and not se_enforcou):
        chute = input("Digite uma letra => ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    todas_as_letras[index] = letra

                index += 1
        else:
            erros += 1

        se_enforcou = erros == len(todas_as_letras)
        acertou = "_" not in todas_as_letras

        print(todas_as_letras)

        if acertou:
            print("Voce ganhou!!")

        if se_enforcou:
            print("Fim de jogo!")

if (__name__ == "__main__"):
    jogar()


def boas_vindas():
    print("*************************************")
    print("Ola mundo. Este é meu jogo de forca")
    print("*************************************")
