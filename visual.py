# autor: marcelo rodrigues
# projeto padrão visual
# intalar o pacote do customthinter
# pip istall customthinter

#importação da biblioteca
import customtkinter as ctk

# Configurações visuais
# Modos 'light' or 'dark
ctk.set_appearance_mode('dark')

# Temas 'blue' , dark-blue, green
ctk.set_default_color_theme('bkue')
janela = ctk.CTk()
janela.geometry('800x600')
janela.title('conversor de temperatura')


#Criação de elementos da tela
entrada = ctk.CTkEntry(janela, placeholder_text='digite sua altura em metros:')
entrada.pack(pady=20)
janela.mainloop()