# Importando a biblioteca requests para fazer requisições HTTP
import customtkinter as ctk
import requests

def buscar_cep():
    # URL via CEP para obter os dados do endereço a partir do CEP
    cep_digitado = cep.get()  # Obtém o valor do campo de entrada
    url = f"https://viacep.com.br/ws/{cep_digitado}/json/"

    # Fazendo a requisição para obter os dados do endereço
    resposta = requests.get(url)  

    # criando uma variável para armazenar os dados do endereço em formato JSON 
    dados = resposta.json()


    print(f'logradouro: {dados["logradouro"]}')   
    print(f'bairro: {dados["bairro"]}')
    print(f'cidade: {dados["localidade"]}')     
    print(f'uf: {dados["uf"]}')

#criação da janela
janela = ctk.CTk()
janela.geometry('800x600')
janela.title('buscador de CEP')

#Criação de elementos da tela
# label tutulo
titulo = ctk.CTkLabel(janela, text="Buscador de CEP")
titulo.pack(pady=20)


# label para o CEP
cep = ctk.CTkEntry(janela, placeholder_text="insira o CEP desejado",
                    justify="center", width=400)
cep.pack(pady=20) 
# Botão para baixar o vídeo

botao = ctk.CTkButton(janela, text="buscar", command = buscar_cep)
botao.pack(pady=20)

status = ctk.CTkLabel(janela, text="")
status.pack(pady=20)




#loop para manter a janela aberta
janela.mainloop()


