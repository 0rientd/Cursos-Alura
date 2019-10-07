class Programa: # Classe mãe
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano =  ano
        self._likes = 0

    def dar_like(self):
        self._likes = self._likes + 1

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


    def dar_like(self):
        self._likes = self.likes + 1

vingadores = Filme("vingadores guerra infinita", 2019, 160)
vingadores.nome = 'teste 123'
print(vingadores.nome, vingadores.ano, vingadores.duracao)