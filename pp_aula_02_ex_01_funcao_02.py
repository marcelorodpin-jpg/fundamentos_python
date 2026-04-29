# opala = primeiro valor
# chevete = segundo valor
# mecamico = operação matematica

def calcular (opala, chevete, mecanico ):
    # cuidado!!!
    # eval - executa expressão em um texto (string)
   return eval (f'{opala}{mecanico}{chevete}')

n1 = float(input('digite o 1º valor: '))
n2 = float(input('digite o 2º valor: '))
op = input('escolha a operação: [+ - * /] ')

print(f'O resultado é: {calcular(n1, n2, op)}')

