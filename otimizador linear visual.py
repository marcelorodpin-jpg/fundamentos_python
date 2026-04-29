import tkinter as tk
from tkinter import messagebox, scrolledtext

def calcular_otimizacao():
    try:
        # Pega os dados da interface
        txt_medidas = entry_medidas.get()
        tamanho_barra = 6000
        espessura_lamina = float(entry_lamina.get())
        
        # Converte a entrada de texto para lista de números
        medidas = [float(x.strip()) for x in txt_medidas.split() if x.strip()]
        
        if not medidas:
            messagebox.showwarning("Aviso", "Por favor, digite ao menos uma medida.")
            return

        # Lógica de Otimização (FFD)
        medidas_ordenadas = sorted(medidas, reverse=True)
        barras = []

        for medida in medidas_ordenadas:
            if medida > tamanho_barra:
                messagebox.showerror("Erro", f"A peça de {medida}mm é maior que a barra!")
                return
            
            encaixou = False
            for barra in barras:
                espaco_ocupado = sum(barra) + (len(barra) * espessura_lamina)
                if espaco_ocupado + medida <= tamanho_barra:
                    barra.append(medida)
                    encaixou = True
                    break
            if not encaixou:
                barras.append([medida])

        # Exibir Resultados
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"RESULTADO DA OTIMIZAÇÃO\n")
        output_text.insert(tk.END, f"Total de barras necessárias: {len(barras)}\n")
        output_text.insert(tk.END, "-"*40 + "\n")
        
        perda_total = 0
        for i, barra in enumerate(barras, 1):
            cortes = len(barra) - 1 if len(barra) > 0 else 0
            sobra = tamanho_barra - sum(barra) - (cortes * espessura_lamina)
            perda_total += sobra
            output_text.insert(tk.END, f"BARRA {i}: {barra}\n")
            output_text.insert(tk.END, f"Sobra: {sobra:.1f}mm\n\n")
            
        output_text.insert(tk.END, "-"*40 + "\n")
        output_text.insert(tk.END, f"Total de sobras: {perda_total:.1f}mm")

    except ValueError:
        messagebox.showerror("Erro", "Use apenas números e separe as medidas por espaço.")

# --- Configuração da Janela ---
root = tk.Tk()
root.title("Otimizador de Corte Barras de 6000mm")
root.geometry("500x550")

try:
    root.iconbitmap("equipa.ico")
except Exception as e:
    print(f"Erro ao carregar ícone: {e}")



# Instruções
tk.Label(root, text="Medidas (em mm, separadas por espaço):", font=("Arial", 10, "bold")).pack(pady=5)
entry_medidas = tk.Entry(root, width=60)
entry_medidas.pack(pady=5)
entry_medidas.insert(0, "1500 1500 2000 800 1200") # Exemplo padrão

# Lâmina
tk.Label(root, text="Espessura da Lâmina (mm):", font=("Arial", 10, "bold")).pack(pady=5)
entry_lamina = tk.Entry(root, width=10)
entry_lamina.pack(pady=5)
entry_lamina.insert(0, "3") # Padrão 3mm

# Botão Calcular
btn_calcular = tk.Button(root, text="OTIMIZAR CORTE", command=calcular_otimizacao, bg="green", fg="white", font=("Arial", 10, "bold"))
btn_calcular.pack(pady=20)

# Área de Resultado
tk.Label(root, text="Plano de Corte:").pack()
output_text = scrolledtext.ScrolledText(root, width=55, height=15)
output_text.pack(pady=10)

root.mainloop()
