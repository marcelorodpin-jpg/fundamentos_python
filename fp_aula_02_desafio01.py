# autor:marcelo
#projeto dedafio 01 etanol ou gasolina

print('olá mundo!')
print()
'''
a empresa abc deseja melhorar seu compsumo com os carros
a empresa deseja inicialmente analisar o desempenho dos carros
a empres precisa saber se compensa abastecer com etanol ou gasolina
dados devem ser apresentados da seguinte forma
nome da empresa_carro_combustivel_consumo
formatatos com duas casas decimais
'''
preco_etanol = float(input("Digite o valor do litro do etanol: R$ "))
preco_gasolina = float(input("Digite o valor do litro do gasolina: R$ "))
relacao = preco_etanol/preco_gasolina
litros = float(input('digite litros abastecidos:'))
distancia = float(input('digite a distancia percorrida:'))
consumo = distancia/litros
if relacao > 0.7:
    print("Compensa gasolina")
else:
    print("Compensa álcool")
    print(f'o consumo é:{consumo}kml')
