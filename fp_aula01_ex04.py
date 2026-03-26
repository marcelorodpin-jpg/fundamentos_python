# Autor: Nilton Barros
# Desafio: Conversor de Temperatura

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 1.8) + 32
kelvin = celsius + 273.15
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
print(f"A temperatura em Kelvin é: {kelvin}")

# print formatado usando f-string para exibir as temperaturas em Fahrenheit e Kelvin
print(f"A temperatura em Fahrenheit é: {fahrenheit} e a temperatura em Kelvin é: {kelvin}")