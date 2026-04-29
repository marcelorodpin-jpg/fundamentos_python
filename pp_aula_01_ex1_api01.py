

# Importando a biblioteca requests para fazer requisições HTTP
import requests

# URL para obter os dados do câmbio a partir da moeda digitada pelo usuário
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'

# Fazendo a requisição para obter os dados do câmbio
resposta = requests.get(url)  

# criando uma variável para armazenar os dados do câmbio em formato JSON 
dados = resposta.json()

valor_dolar = (dados['USDBRL']['bid']) 
valor_euro = (dados['EURBRL']['bid'])
valor_bitcoin = (dados['BTCBRL']['bid'])

print(f'O valor do dólar é: R$ {valor_dolar}')
print(f'O valor do euro é: R$ {valor_euro}')
print(f'O valor do bitcoin é: R$ {valor_bitcoin}')
