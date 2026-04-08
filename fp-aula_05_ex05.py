# Definimos que o loop vai rodar 10vezes
contador = 0
contador2 = 0
for i in range(5):
    numero = int(input('digite um numero:'))
    print(f'o num. digitado :{numero} e o valor de i é: {i}')
    if numero > 0:
        contador = contador + 1
        if numero < 0:
            contador2 = contador2+1
print (f'quantidade de numeros positivos: {contador}')
print (f'quantidade de numeros negativo: {contador2}')

    
    
    
