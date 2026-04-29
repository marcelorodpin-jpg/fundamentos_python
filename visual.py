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
ctk.set_default_color_theme('blue')
janela = ctk.CTk()
janela.geometry('800x600')
janela.title('Calculo do IMC')
def calcular():
    altura = float(entrada_altura.get())
    peso = float(entrada_peso.get())
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = 'Abaixo do peso'
        cor = 'green'
    elif 18.5 <= imc < 25:
        classificacao = 'Peso normal'
        cor = 'yellow'

    elif 25 <= imc < 30:
        classificacao = 'Acima do peso'
        cor = 'orange'
    else:
        classificacao = 'Obeso'
        cor = 'red'
    resultado_label.configure(text=f'Seu IMC é: {imc:.2f}\nSua classificação é:\n {classificacao}',text_color=cor)

#Criação de elementos da tela
entrada_altura = ctk.CTkEntry(janela,                               width=360,
                              height=40,
                              font=('Arial', 12),
                              placeholder_text='digite sua altura em metros:')
entrada_altura.pack(pady=20)
entrada_peso = ctk.CTkEntry(janela, 
                            width=360,
                            height=40,
                            font=('Arial', 12),
                            placeholder_text='digite seu peso em kg:')
entrada_peso.pack(pady=20)

# Botão
resultado_botao = ctk.CTkButton(janela, 
                                width=360,
                                height=40,
                                font=('Arial', 12),
                                text='Calcular',
                                command=calcular,
                                corner_radius=8,
                                fg_color='green',)
                                
                                
resultado_botao.pack(pady=20)

# Label para mostrar o resultado
resultado_label = ctk.CTkLabel(janela,
                                width=360,
                                height=40,
                                font=('Arial', 16),
                                text='')
resultado_label.pack(pady=20)





janela.mainloop()