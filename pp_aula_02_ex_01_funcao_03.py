

def calcular(a, b, op):
    #() -> TUPULAS - IMUTAVEL
    #[] -> LISTAS - MUTAVEL
    operacoes = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b
    }
    return operacoes[op]


n1 = float(input('digite o 1º valor: '))
n2 = float(input('digite o 2º valor: '))
op = input('escolha a operação: [+ - * /] ')
print(f'O resultado é: {calcular(n1, n2, op)}')

