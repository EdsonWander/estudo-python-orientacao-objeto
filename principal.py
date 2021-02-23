import filme
import serie
import playlist
import random

arquivo_filme = open("filmes.txt", "r", encoding='utf-8')
arquivo_serie = open("series.txt", "r", encoding='utf-8')

lista_programas = []

linha = ""

for item in arquivo_filme:
    item = item.strip("\n")
    linha = item.split("-")
    lista_programas.append(filme.Filme(linha[0], linha[1], linha[2]))

for item in arquivo_serie:
    item = item.strip("\n")
    linha = item.split("-")
    lista_programas.append(serie.Serie(linha[0], linha[1], linha[2]))

var_numero = random.randrange(1,10)
var_aux1 = var_aux2 = 0

while(var_aux1 < len(lista_programas)):

    while(var_aux2 <= var_numero):
        lista_programas.__getitem__(var_aux1).dar_like()
        var_aux2 += 1

    var_numero = random.randrange(1,20)
    var_aux1 += 1
    var_aux2 = 0

lista = playlist.Playlist("Playlist", lista_programas)

for item in lista:
    print(item)

print("", end="\n")
input("Digite <ENTER> para sair...")