# Autor :Marcelo
# Variaveis globais do sistema
# Pode ser ultilizada em todo sistema

valor1 = float(input('digite o 1º valor: '))
valor2 = float(input('digite o 2º valor: '))

# Função para relalizar os cálculos e impressão

def calcular (valor1, valor2):
    # Variáveis locais, ultilizadas dentro da função
    soma = valor1+valor2
    subtração = valor1-valor2
    multiplicação = valor1*valor2
    divisao = valor1/valor2

    print(f'a soma é {soma}')
    print(f'a subtração é: {subtração}')
    print(f'a multiplicação é: {multiplicação}')
    print(f'a divisão é: {divisao}')

# Chamada da função
calcular(valor1, valor2)

