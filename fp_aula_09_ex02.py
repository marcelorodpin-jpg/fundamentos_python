# importação da biblioteca
import customtkinter as ctk

# Configurações visuais
# Modos 'light' or 'dark
ctk.set_appearance_mode('dark')

# Temas 'blue' , dark-blue, green
ctk.set_default_color_theme('blue')
janela = ctk.CTk()
janela.geometry('800x600')
janela.title('buscador de cep')
janela.mainloop()