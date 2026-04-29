numero = int(input('digite um numero:'))
fatorial = 1

# O range vai de 1 até o número + 1 (para incluir o próprio número)
for i in range(1,numero+1):

    fatorial = fatorial * i
    print(f'O fatorial de {numero} é: {fatorial}')