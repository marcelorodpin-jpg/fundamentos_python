# Autor: Marcelo
#loop for - tabuada
num = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {num}:")             
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}") 

num2 = int(input("Digite outro número para ver a tabuada: "))
print(f"Tabuada do {num2}:")
for j in range(1, 11):
    print(num2, "x", j, "=", num2 * j)
    