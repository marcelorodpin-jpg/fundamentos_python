#autor :carcelo
# projeto calculo hipotenusa
#potencia

oposto = float(input('digite o valor do cateto oposto: '))
adjacente = float(input('digite o valor do cateto adjacente:'))
hipotenusa = ((oposto ** 2) + (adjacente ** 2)) ** 0.5

#exibir o numero formatado com duas casa decimais
print(f'o valor da hipotenusa é: {hipotenusa: .2f}')

#roud()
hipotenusa = round(hipotenusa, 2)
print(f'o valor da hipotenusa e: {hipotenusa}')
              