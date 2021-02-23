class Playlist():

    def __init__(self, nome, programas):
        self.__nome = nome
        self.__programas = programas

    @property
    def nome(self):
        return self.__nome.title()

    @property
    def programas(self):
        return self.__programas

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @programas.setter
    def programas(self, programas):
        self.__programas = programas

    def __len__(self):
        return len(self.programas)

    def __getitem__(self, item):
        return self.programas[item]