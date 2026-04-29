import customtkinter as ctk
from pytubefix import YouTube
# Configurações visuais

# Função para baixar o vídeo
def baixar():

        link_youtube = link.get()
        yt = YouTube(link_youtube)
        
        # Tenta baixar a resolução padrão
        yt.streams.first().download()
        
        # Se chegar aqui, deu certo
        status.configure(text="Download concluído!", fg="green")
        
    

#criação da janela
janela = ctk.CTk()
janela.geometry('800x600')
janela.title('Download de Vídeos do YouTub')
# icone da janela
janela.iconbitmap('youtube.ico')

ctk.set_appearance_mode('dark')


#Criação de elementos da tela
# label tutulo
titulo = ctk.CTkLabel(janela, text="Download de Vídeos do YouTube")
titulo.pack(pady=20)
# label para o link
link = ctk.CTkEntry(janela, placeholder_text="insira o link desejado",
                    justify="center", width=400)
link.pack(pady=20) 

# Botão para baixar o vídeo

download = ctk.CTkButton(janela, text="download", command = baixar)
download.pack(pady=20)

status = ctk.CTkLabel(janela, text="")
status.pack(pady=20)


#loop para manter a janela aberta
janela.mainloop()
