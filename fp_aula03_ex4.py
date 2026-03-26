# Solicitando dados ao usuário
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Cálculo do IMC
imc = peso / (altura ** 2)

# Exibindo o resultado formatado
print(f"Seu IMC é: {imc:.2f}")


if imc <= 18.5:
    print("Classificação: Abaixo do peso")
elif imc <= 25:
    print("Classificação: Peso normal")
elif imc <= 30:
    print("Classificação: Sobrepeso")   
else:
    print("Classificação: Obesidade")