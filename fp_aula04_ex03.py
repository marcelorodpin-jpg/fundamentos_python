#Autor: marcelo rodrigues
# Projeto Estrutura Condicional


cm = (input('possui carteira de motorista: '))
bafometro = (input('consumiu bebida alcolica: '))


# and - ambas as condições são verdadeiras
#para que o resultado seja verdadeiro

if cm == 'sim' and bafometro != 'sim':
     print('acesso liberado, pode seguir viagem')
else:
    print('acesso bloqueado, volta para casa rapaz')
