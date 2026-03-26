# Programa para calcular área e valor total de um terreno

# 1. Recebendo as entradas do usuário
# Usamos float() para permitir números decimais (ex: 10.5m)
largura = float(input("Digite a largura do terreno (metros): "))
comprimento = float(input("Digite o comprimento do terreno (metros): "))
valor_total = float(input("Digite o valor total do terreno (R$): "))

# 2. Calculando a área (largura x comprimento)
area = largura * comprimento

# 3. Calculando o valor por metro quadrado
valor_m2 = valor_total / area

# 4. Exibindo os resultados
print("-" * 30)
print(f"ÁREA DO TERRENO: {area:.2f} m²")
print(f"VALOR POR METRO QUADRADO: R$ {valor_m2:.2f}")
print("-" * 30)
