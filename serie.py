import programa

class Serie(programa.Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.__temporada = temporada

    @property
    def temporada(self):
        return self.__temporada

    @temporada.setter
    def temporada(self, temporada):
        self.__temporada = temporada

    def __str__(self):
        return "A série {0} do ano de {1} tem {2} temporadas e recebeu {3} likes".format(self.nome, self.ano, self.temporada, self.likes)