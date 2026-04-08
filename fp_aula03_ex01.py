# Autor: marcelo rodrigues
# Projeto Estrutura Condicional
nota1 = float(input('digita a nota primeira do aluno'))
nota2 = float(input('digita a nota segunda do aluno'))
nota3 = float(input('digita a nota terceira do aluno'))
nota4 = float(input('digita a nota quarta do aluno'))
media = (nota1 + nota2 + nota3 + nota4) /4
print(f'a media do aluno é: {media}')
if media >=5:
    print(f'aluno aprovado!{media: .2f}😊')
else:
    print('aluno reprovado😒')
    