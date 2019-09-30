

class Conta():

    def __init__(self, numero, titular, saldo, limite):
        print("Criando conta... | Objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Titular => {} | Saldo => {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor
        print("Novo saldo => {}".format(self.__saldo))

    def sacar(self, valor):
        self.__saldo -= valor
        print("Novo saldo => {}".format(self.__saldo))

    def transferir(self, valor, destino):
        self.__sacar(valor)
        self.__depositar(destino)
        print("Transferido {} reais para a conta {} de {}".format(valor, destino.numero(), destino.titular()))