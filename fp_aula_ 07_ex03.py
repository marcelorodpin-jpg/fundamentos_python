# autor:marcelo
#  desafio 07 aula 03

''' listar 10 alunos onde 2 alunos desistiram 1 aluno entrou ordenar em ordem alfabética 
e imprimir os alunos separados por |'''

alunos = ['Maria', 'Ana', 'Roberto', 'Rita', 'Marcela', 'Joana', 'Carla', 'Kevin', 'Raquel', 'Cleisson']
desistiram = ['Kevin', 'Raquel']    
alunos.remove('Kevin')
alunos.remove('Raquel')
print(f'alunos que desistiram: {desistiram}')
print(f'alunos restantes: {alunos}')
entraram = ['Finn']
print(f'alunos que entraram: {entraram}')
alunos.append('Finn')
print(*alunos, sep='|')
alunos.sort()
print(*alunos, sep='|' )