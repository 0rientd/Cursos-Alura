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

    def __str__(self):
        return self.nome, self.ano

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome}, {self.ano}, {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome}, {self.ano}, {self.temporadas}'

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

        def tamanho(self):
            return len(self.programas)

vingadores = Filme("vingadores guerra infinita", 2019, 160)
atlanta = Serie("atlanta de donald glover", 2018, 2)
panico = Filme("panico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

filmes_e_series = [vingadores, atlanta, panico, demolidor]
fim_de_semana = Playlist("fim de semana", filmes_e_series)

for programas in filmes_e_series:
    print(f'{programas}')