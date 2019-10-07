class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano =  ano
        self.duracao = duracao
        self.__likes = 0

    def dar_like(self):
        self.likes = self.likes + 1

    @property
    def nome(self):
        return self.__nome

    @property
    def likes(self):
        return self.__likes

class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano =  ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_like(self):
        self.likes = self.likes + 1

vingadores = Filme("vingadores guerra infinita", 2019, 160)
print(vingadores.nome, vingadores.ano, vingadores.duracao)