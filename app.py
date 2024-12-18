import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime, timedelta
import pandas as pd

# Lista para armazenar os dados
dados = []

# Variáveis globais do cronômetro
cronometro_iniciado = False
cronometro_pausado = False
hora_inicial_cronometro = None
tempo_acumulado = timedelta()

# Função para atualizar o cronômetro na interface
def atualizar_cronometro():
    if cronometro_iniciado and not cronometro_pausado:
        global tempo_acumulado
        tempo_decorrido = datetime.now() - hora_inicial_cronometro + tempo_acumulado
        minutos, segundos = divmod(tempo_decorrido.seconds, 60)
        lbl_cronometro.config(text=f"Cronômetro: {minutos:02}:{segundos:02}", fg="blue")
        root.after(1000, atualizar_cronometro)

# Função para iniciar o cronômetro
def iniciar_cronometro():
    global cronometro_iniciado, cronometro_pausado, hora_inicial_cronometro
    if not cronometro_iniciado or cronometro_pausado:
        hora_inicial_cronometro = datetime.now()
        cronometro_iniciado = True
        cronometro_pausado = False
        atualizar_cronometro()
        lbl_cronometro.config(text="Cronômetro iniciado", fg="blue")
        desabilitar_botoes()
    else:
        messagebox.showinfo("Aviso", "O cronômetro já está em andamento.")

# Função para pausar o cronômetro
def pausar_cronometro():
    global cronometro_iniciado, cronometro_pausado, tempo_acumulado
    if cronometro_iniciado and not cronometro_pausado:
        tempo_acumulado += datetime.now() - hora_inicial_cronometro
        cronometro_pausado = True
        lbl_cronometro.config(text="Cronômetro pausado", fg="orange")
    else:
        messagebox.showinfo("Aviso", "O cronômetro não está em andamento ou já está pausado.")

# Função para parar o cronômetro
def parar_cronometro():
    global cronometro_iniciado, cronometro_pausado, tempo_acumulado
    if cronometro_iniciado:
        tempo_acumulado += datetime.now() - hora_inicial_cronometro
        cronometro_iniciado = False
        cronometro_pausado = False
        minutos, segundos = divmod(tempo_acumulado.seconds, 60)
        lbl_cronometro.config(text=f"Cronômetro parado: {minutos:02}:{segundos:02}", fg="green")
        habilitar_botoes()
        entry_solucao.config(state=tk.NORMAL)  # Habilitar campo de solução
    else:
        messagebox.showinfo("Aviso", "O cronômetro ainda não foi iniciado.")

# Função para calcular horas trabalhadas
def calcular_horas():
    global tempo_acumulado
    try:
        ticket = entry_ticket.get()
        descricao = entry_descricao.get("1.0", tk.END).strip()
        solucao = entry_solucao.get("1.0", tk.END).strip()
        hora_inicial = entry_hora_inicial.get()

        if not hora_inicial:
            messagebox.showerror("Erro", "Por favor, insira a hora inicial.")
            return

        hora_ini = datetime.strptime(hora_inicial, "%H:%M")

        # Calculando a hora final com base no cronômetro
        hora_fim = hora_ini + tempo_acumulado
        hora_final = hora_fim.strftime("%H:%M")

        # Calculando horas trabalhadas
        delta = tempo_acumulado.seconds / 3600.0

        # Salvando no formato de lista
        dados.append({
            "Ticket": ticket,
            "Descrição": descricao,
            "Solução": solucao,
            "Hora Inicial": hora_inicial,
            "Hora Final": hora_final,
            "Horas Trabalhadas": round(delta, 2)
        })

        # Atualizando a interface
        lbl_resultado.config(text=f"Ticket {ticket}: {round(delta, 2)} horas")

        # Limpando os campos e variáveis
        entry_ticket.delete(0, tk.END)
        entry_descricao.delete("1.0", tk.END)
        entry_solucao.delete("1.0", tk.END)
        entry_solucao.config(state=tk.DISABLED)  # Desabilitar campo de solução novamente
        entry_hora_inicial.delete(0, tk.END)
        tempo_acumulado = timedelta()

    except Exception as e:
        messagebox.showerror("Erro", f"Verifique os campos inseridos.\nDetalhes: {e}")

# Função para exportar os dados para Excel
def exportar_planilha():
    try:
        if not dados:
            messagebox.showwarning("Aviso", "Nenhum dado para exportar.")
            return

        # Escolhendo o caminho do arquivo
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", 
                                                 filetypes=[("Arquivos Excel", "*.xlsx")],
                                                 title="Salvar como")
        if not file_path:
            return

        # Criando DataFrame
        df = pd.DataFrame(dados)

        # Salvando em Excel
        df.to_excel(file_path, index=False, engine="openpyxl")

        messagebox.showinfo("Sucesso", f"Dados exportados com sucesso para '{file_path}'")
        dados.clear()
        lbl_resultado.config(text="Exportação concluída.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao exportar planilha.\nDetalhes: {e}")

# Função para habilitar botões
def habilitar_botoes():
    btn_calcular.config(state=tk.NORMAL)
    btn_exportar.config(state=tk.NORMAL)
    btn_parar_cronometro.config(state=tk.NORMAL)
    btn_pausar_cronometro.config(state=tk.NORMAL)

# Função para desabilitar botões
def desabilitar_botoes():
    btn_calcular.config(state=tk.DISABLED)
    btn_exportar.config(state=tk.DISABLED)
    btn_parar_cronometro.config(state=tk.DISABLED)
    btn_pausar_cronometro.config(state=tk.DISABLED)

# Criando a interface gráfica
root = tk.Tk()
root.title("Calculadora de Horas Trabalhadas")
root.resizable(False, False)

# Configurando os campos
tk.Label(root, text="Número do Ticket:").grid(row=0, column=0, padx=10, pady=5)
entry_ticket = tk.Entry(root)
entry_ticket.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Descrição do Ticket:").grid(row=1, column=0, padx=10, pady=5)
entry_descricao = tk.Text(root, height=3, width=30)
entry_descricao.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Solução do Ticket:").grid(row=2, column=0, padx=10, pady=5)
entry_solucao = tk.Text(root, height=3, width=30, state=tk.DISABLED)
entry_solucao.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Hora Inicial (HH:MM):").grid(row=3, column=0, padx=10, pady=5)
entry_hora_inicial = tk.Entry(root)
entry_hora_inicial.grid(row=3, column=1, padx=10, pady=5)

# Botões
btn_iniciar_cronometro = tk.Button(root, text="Iniciar Cronômetro", command=iniciar_cronometro)
btn_iniciar_cronometro.grid(row=4, column=0, padx=10, pady=10)

btn_pausar_cronometro = tk.Button(root, text="Pausar Cronômetro", command=pausar_cronometro, state=tk.DISABLED)
btn_pausar_cronometro.grid(row=4, column=1, padx=10, pady=10)

btn_parar_cronometro = tk.Button(root, text="Parar Cronômetro", command=parar_cronometro, state=tk.DISABLED)
btn_parar_cronometro.grid(row=5, column=0, padx=10, pady=10)

btn_calcular = tk.Button(root, text="Calcular Horas", command=calcular_horas, state=tk.DISABLED)
btn_calcular.grid(row=5, column=1, padx=10, pady=10)

btn_exportar = tk.Button(root, text="Exportar para Planilha", command=exportar_planilha, state=tk.DISABLED)
btn_exportar.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Cronômetro
lbl_cronometro = tk.Label(root, text="Cronômetro: 00:00", fg="blue")
lbl_cronometro.grid(row=7, column=0, columnspan=2, pady=10)

# Resultado
lbl_resultado = tk.Label(root, text="", fg="green")
lbl_resultado.grid(row=8, column=0, columnspan=2, pady=10)

# Iniciar a aplicação
root.mainloop()
