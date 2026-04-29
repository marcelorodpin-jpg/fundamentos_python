# solicitação dados do usuario
peso = float(input('digite seu peso'))
altura = float(input('digite sua altura'))

# Calculo do Imc

imc = peso / (altura ** 2)

# Exibindo o resultado formatado
print(f'seu imc é: {imc: .f}')


if imc <= 18.5:
     print("classificacao Abaixo do peso")
elif imc <= 25:
     print("classificacao normal")
elif 25 <= imc < 30:
     print("classificacao sobre peso")
elif 30 <= imc < 35:
     print("classificacao obesidade grau 1")
elif 35 <= imc < 40:
    print("classificacao obesidade grau 2")
else:
     print("classificacao obesidade morbida")
            
print(f"Classificação: {imc}")
