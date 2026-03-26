# Programa para calcular área e valor total de um terreno

# 1. Recebendo as entradas do usuário
# Usamos float() para permitir números decimais (ex: 10.5m)
largura = float(input("Digite a largura do terreno (metros): "))
comprimento = float(input("Digite o comprimento do terreno (metros): "))
valor_m2 = float(input("Digite o valor do metro quadrado (R$): "))

# 2. Calculando a área (largura x comprimento)
area = largura * comprimento

# 3. Calculando o valor total (área x valor por metro quadrado)
valor_total = area * valor_m2

# 4. Exibindo os resultados
print(f"ÁREA DO TERRENO: {area:.2f} m²")
print(f"VALOR TOTAL: R$ {valor_total:.2f}")

