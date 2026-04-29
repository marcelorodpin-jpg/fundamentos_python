# autor:marcelo
# meu segundo projeto em python

print('olá mundo!')
print('meu segundo programa em python')
print('marcelo')

# criação de variáveis para uma calculadora de somar
# regras basicas para criar variáveis:
# 1. o nome da variavel deve começar ccom uma letra ou um sublinhado
# 2. nunca usar ascentos, espaços ou caracteres especiais
# 3. o nome da variavel deve ser autoexplicativo
# 4. o nome da variável não pode ter espaço
# 5. nunca usar palavras reservada
# 6. variavel do tipo int e relativa a valores inteiros
# 7. a palavra reservada input e usada para receber dados do usuario
# 8. a variavel float e usada para numeros quebrados

valor1 = int (input('digite o primeiro valor'))
valor2 = int (input('digite o segundo valor'))
soma = valor1 + valor2
print(' o resultado da soma é: ',soma)

# 9. para gerar um print com texto, preciso que o texto esteja entre aspas simples ou duplas

# 10. print formatado usando f-string
print(f'o resultado da soma é: {soma}')
