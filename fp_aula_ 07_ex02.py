# autor:Marcelo
#  Aula 07 desafio 02


# criar uma lista de filmes
filmes = ["star wars", "irmãos grimm", "vingadores", "indiana jones"]
# imprimir o terceiro filme da lista
print(filmes[2])
# imprimir a lista completa de filmes
# adicionar um filme ao final da lista
filmes.append("Jurassic Park")
# imprimir a lista completa de filmes
print(filmes)
# inserir um filme na posição 2
filmes.insert(2, "John Wick")
# imprimir a lista completa de filmes
print(filmes)
# listar os filmes em ordem alfabética
filmes.sort()
# imprimir os filmes separados por |
print(*filmes, sep='|')

