# Autor: Nilton Barros
# Projeto Calculadora com recebimento de dados do usuário

# variável do tipo int é relativa a valores inteiros 
# a palavra reservada input é usada para receber dados do usuário
valor1 = int (input('Digite o primeiro valor: '))
valor2 = int (input('Digite o segundo valor: '))
soma = valor1 + valor2
print(soma)

# para gerar um print com texto, preciso que o texto esteja entre aspas
print('O resultado da soma é: ', soma)  

# print formatado usando f-string
print(f'O resultado da soma é: {soma}')