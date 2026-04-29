# Autor: Marcelo
# Fatorial com loop while
# Usuario digita um número e o programa calcula o fatorial desse número

num = int(input('digite um numero:'))
fatorial = 1

while num> 0:
    fatorial = fatorial * num
    num = num - 1
    print(f'variavel num vale: {num} e o fatorial vale: {fatorial}')
print('O fatorial é:', fatorial)


    