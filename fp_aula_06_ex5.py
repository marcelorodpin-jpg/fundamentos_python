# Autor: Marcelo
#loop for - tabuada

numero = 2
while numero <=4:
    print(f'Tabuada do {numero}')
    contador = 1
    while contador <=10:
        resultado = numero * contador
        print(f'{numero} x {contador} = {resultado}')
        contador = contador + 1

    numero = numero + 1