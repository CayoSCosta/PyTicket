import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
import pandas as pd
import os

# Lista para armazenar os dados
dados = []

# Variáveis para o cronômetro
cronometro_iniciado = False
hora_inicial_cronometro = None
cronometro_tempo_decorrido = 0

# Função para atualizar o cronômetro na interface
def atualizar_cronometro():
    if cronometro_iniciado:
        tempo_decorrido = datetime.now() - hora_inicial_cronometro
        minutos, segundos = divmod(tempo_decorrido.seconds, 60)
        lbl_cronometro.config(text=f"Cronômetro: {minutos:02}:{segundos:02}", fg="blue")
        root.after(1000, atualizar_cronometro)

# Função para iniciar o cronômetro
def iniciar_cronometro():
    global cronometro_iniciado, hora_inicial_cronometro
    if not cronometro_iniciado:
        hora_inicial_cronometro = datetime.now()
        entry_hora_inicial.delete(0, tk.END)
        entry_hora_inicial.insert(0, hora_inicial_cronometro.strftime("%H:%M"))
        cronometro_iniciado = True
        lbl_cronometro.config(text="Cronômetro iniciado", fg="blue")
        atualizar_cronometro()
    else:
        messagebox.showinfo("Aviso", "O cronômetro já está em andamento.")

# Função para parar o cronômetro
def parar_cronometro():
    global cronometro_iniciado, cronometro_tempo_decorrido
    if cronometro_iniciado:
        tempo_decorrido = datetime.now() - hora_inicial_cronometro
        cronometro_tempo_decorrido = tempo_decorrido.seconds // 60
        cronometro_iniciado = False
        minutos, segundos = divmod(tempo_decorrido.seconds, 60)
        lbl_cronometro.config(text=f"Cronômetro parado: {minutos:02}:{segundos:02}", fg="green")
    else:
        messagebox.showinfo("Aviso", "O cronômetro ainda não foi iniciado.")

# Função para calcular horas trabalhadas
def calcular_horas():
    try:
        ticket = entry_ticket.get()
        hora_inicial = entry_hora_inicial.get()

        if not hora_inicial:
            messagebox.showerror("Erro", "Por favor, insira a hora inicial.")
            return

        hora_ini = datetime.strptime(hora_inicial, "%H:%M")

        # Calculando a hora final com base no cronômetro
        hora_fim = hora_ini + timedelta(minutes=cronometro_tempo_decorrido)
        hora_final = hora_fim.strftime("%H:%M")

        # Calculando horas trabalhadas
        delta = cronometro_tempo_decorrido / 60.0

        # Salvando no formato de lista
        dados.append({"Ticket": ticket, "Hora Inicial": hora_inicial, "Hora Final": hora_final, "Horas Trabalhadas": round(delta, 2)})

        # Atualizando a interface
        lbl_resultado.config(text=f"Ticket {ticket}: {round(delta, 2)} horas")

        # Limpando os campos
        entry_ticket.delete(0, tk.END)
        entry_hora_inicial.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Erro", f"Verifique os campos inseridos.\nDetalhes: {e}")

# Função para exportar os dados para Excel
def exportar_planilha():
    try:
        if not dados:
            messagebox.showwarning("Aviso", "Nenhum dado para exportar.")
            return

        # Criando DataFrame
        df = pd.DataFrame(dados)

        # Salvando em Excel
        file_name = "horas_tickets.xlsx"
        if os.path.exists(file_name):
            existing_df = pd.read_excel(file_name)
            df = pd.concat([existing_df, df], ignore_index=True)

        df.to_excel(file_name, index=False, engine="openpyxl")

        messagebox.showinfo("Sucesso", f"Dados exportados com sucesso para '{file_name}'")
        dados.clear()
        lbl_resultado.config(text="Exportação concluída.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar planilha.\nDetalhes: {e}")

# Criando a interface gráfica
root = tk.Tk()
root.title("Calculadora de Horas Trabalhadas")
root.resizable(False, False)

# Configurando os campos
tk.Label(root, text="Número do Ticket:").grid(row=0, column=0, padx=10, pady=5)
entry_ticket = tk.Entry(root)
entry_ticket.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Hora Inicial (HH:MM):").grid(row=1, column=0, padx=10, pady=5)
entry_hora_inicial = tk.Entry(root)
entry_hora_inicial.grid(row=1, column=1, padx=10, pady=5)

# Botões do cronômetro
btn_iniciar_cronometro = tk.Button(root, text="Iniciar Cronômetro", command=iniciar_cronometro)
btn_iniciar_cronometro.grid(row=2, column=0, padx=10, pady=5)

btn_parar_cronometro = tk.Button(root, text="Parar Cronômetro", command=parar_cronometro)
btn_parar_cronometro.grid(row=2, column=1, padx=10, pady=5)

lbl_cronometro = tk.Label(root, text="", fg="blue")
lbl_cronometro.grid(row=3, column=0, columnspan=2, pady=10)

# Botões principais
btn_calcular = tk.Button(root, text="Calcular Horas", command=calcular_horas)
btn_calcular.grid(row=4, column=0, padx=10, pady=10)

btn_exportar = tk.Button(root, text="Exportar para Planilha", command=exportar_planilha)
btn_exportar.grid(row=4, column=1, padx=10, pady=10)

# Resultado
lbl_resultado = tk.Label(root, text="", fg="green")
lbl_resultado.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar a aplicação
root.mainloop()
