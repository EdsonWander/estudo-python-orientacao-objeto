class Programa:

    def __init__(self, nome, ano):
        self.__nome = nome
        self.__ano = ano
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome.title()

    @property
    def ano(self):
        return self.__ano

    @property
    def likes(self):
        return self.__likes

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @likes.setter
    def likes(self, likes):
        self.__likes = likes

    def dar_like(self):
        self.__likes += 1

    def __str__(self):
        return "O {0} do ano de {1} recebeu {2} likes".format(self.nome, self.ano, self.likes)