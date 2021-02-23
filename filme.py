import programa

class Filme(programa.Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    @property
    def duracao(self):
        return self.__duracao

    @duracao.setter
    def duracao(self, duracao):
        self.__duracao = duracao

    def __str__(self):
        return "O filme {0} do ano de {1} tem {2} e recebeu {3} likes".format(self.nome, self.ano, self.duracao, self.likes)