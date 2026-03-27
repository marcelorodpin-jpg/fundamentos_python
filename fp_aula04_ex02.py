#Autor: marcelo rodrigues
# Projeto Estrutura Condicional


idade = int(input('digita sua idade'))
credencial = (input('digita sua credencial'))


# and - ambas as condições são verdadeiras
#para que o resultado seja verdadeiro
if idade >= 18 and credencial == 'sim':
     print('acesso liberado')
else:
    print('acesso bloqueado')