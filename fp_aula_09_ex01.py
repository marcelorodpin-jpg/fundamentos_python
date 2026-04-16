 #Importando a biblioteca requests para fazer requisições HTTP
import requests


# Aqui você pede para o usuário digitar a latitude e longitude
latitude = input("Digite sua latitude: ") 
longitude = input("Digite sua longitude: ") 

# URL open meteo para obter os dados do clima a partir da latitude e longitude
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
# Fazendo a requisição para obter os dados do clima
resposta = requests.get(url)  

# criando uma variável para armazenar os dados do clima em formato JSON 
dados = resposta.json()


# O caminho correto é entrar na chave 'current' primeiro
print(f"Horário: {dados['current']['time']}")   
print(f"Temperatura: {dados['current']['temperature_2m']}°C")
print(f"Velocidade do Vento: {dados['current']['wind_speed_10m']} km/h")
