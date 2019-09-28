import forca
import jogo

def jogar():
    print("*************************************")
    print("Escolha um dos dois jogos.")
    print("*************************************")

    print("(1) - Adivinhação | (2) - Forca")

    escolha = int(input("=> " ))

    if escolha == 1:
        print("Iniciando jogo da adivinhação")
        jogo.jogar()
    elif escolha == 2:
        print("Iniciando jogo da forca")
        forca.jogar()

if (__name__ == "__main__"):
    jogar()