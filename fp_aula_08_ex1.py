# Autor:marcelo
# Projeto: Tuplas
# Tupula de dados: é uma coleção de dados ordenada e imutável, ou seja, não pode ser alterada depois de criada. 
# As tuplas são definidas usando parênteses () e os elementos são separados por vírgulas. 

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')   
print(*meses, sep=' | ')
print()
dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
print(*dias_semana, sep=' | ')


lista_alunos = ('Enzo', 'Marcos', 'Marcelo', 'José')
print(*lista_alunos, sep=' | ')

# Transformando tupla em lista
lista_alunos = list(lista_alunos)
print(lista_alunos) 
# Adicionando um aluno a lista
lista_alunos.append('Maria')
print(lista_alunos)

# Transformando lista em tupla
lista_alunos = tuple(lista_alunos)
print(lista_alunos) 
