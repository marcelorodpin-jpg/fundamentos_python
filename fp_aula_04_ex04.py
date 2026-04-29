#Autor: marcelo rodrigues
# Projeto Estrutura Condicional


idade = int(input('digita sua idade: '))
bebida = (input('consumiu alcool?: '))


# and - ambas as condições são verdadeiras
#para que o resultado seja verdadeiro
if idade >=18 and bebida !='sim':
     print('voce pode dirigir')
else:
    print('voce não pode dirigir')