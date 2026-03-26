# Autor: Nilton Barros
# Projeto Estrutura Condicional

nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
nota4 = float(input('Digite a quarta nota do aluno: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 5:
    print(f'Aluno aprovado!{media:.2f}')
else:
    print(f'Aluno reprovado!:( {media:.2f}')