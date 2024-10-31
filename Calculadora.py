# Importando a biblioteca de criação de janelas
import tkinter as tk

# Criação da janela
janela = tk.Tk()

# Especificar o tamanho da janela em pixels
janela.geometry("700x480")

# Título da janela
janela.title('Conversor de Unidades')

# Nomeando a caixa de entrada de dados
texto = tk.Label(janela, text='Conversor de Temperatura', font=('Arial black', 20), fg='blue')
texto.grid(row=0, column=0, columnspan=3, pady=50)

texto = tk.Label(janela, text='Insira a temperatura que deseja converter', font=('Arial black', 16), fg='purple')
texto.grid(row=1, column=0, columnspan=3, pady=10)

# Caixa de entrada de dados 
campo1 = tk.Entry(janela, width=30)
campo1.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Criando um Label para exibir o resultado
total = tk.Label(janela, text='Selecione o tipo de conversão', font=('Arial black', 16), fg='Red')
total.grid(row=3, columnspan=3, pady=5)

# Funções de conversão (sem alterações)
def C1():
    num1 = float(campo1.get())
    resultado = ((9 * num1) / 5) + 32
    total.config(text=f'O resultado é {resultado:.2f}ºF')

def C2():
    num1 = float(campo1.get())
    resultado = num1 + 273.15
    total.config(text=f'O resultado é {resultado:.2f}ºK')

def F1():
    num1 = float(campo1.get())
    resultado = (num1 - 32) * 5 / 9
    total.config(text=f'O resultado é {resultado:.2f}ºC')

def F2():
    num1 = float(campo1.get())
    resultado = (num1 - 32) * 5 / 9 + 273.15
    total.config(text=f'O resultado é {resultado:.2f}ºK')

def K1():
    num1 = float(campo1.get())
    resultado = num1 - 273.15
    total.config(text=f'O resultado é {resultado:.2f}ºC')

def K2():
    num1 = float(campo1.get())
    resultado = (num1 - 273.15) * 9 / 5 + 32
    total.config(text=f'O resultado é {resultado:.2f}ºF')

# Criando os botões de ação usando grid
botao1 = tk.Button(janela, text="ºC para ºF", command=C1, bg='#90EE90')
botao1.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

botao2 = tk.Button(janela, text="ºC para ºK", command=C2, bg='#90EE90')
botao2.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

botao3 = tk.Button(janela, text="ºF para ºC", command=F1, bg='#90EE90')
botao3.grid(row=4, column=2, padx=10, pady=10, sticky='ew')

botao4 = tk.Button(janela, text="ºF para ºK", command=F2, bg='#90EE90')
botao4.grid(row=5, column=0, padx=10, pady=10, sticky='ew')

botao5 = tk.Button(janela, text="ºK para ºC", command=K1, bg='#90EE90')
botao5.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

botao6 = tk.Button(janela, text="ºK para ºF", command=K2, bg='#90EE90')
botao6.grid(row=5, column=2, padx=10, pady=10, sticky='ew')

# Ajustando as colunas para ocupar espaço igual
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)

# Função para abrir uma nova janela
def abrir_nova_janela():
    nova_janela = tk.Toplevel(janela)  # Cria uma nova janela
    nova_janela.geometry("700x480")    # Tamanho da nova janela
    nova_janela.title('Conversor de Unidades')   # Título da nova janela

    # Adicionando um Label na nova janela (apenas para identificação dos campos)
    texto_nova_janela = tk.Label(nova_janela, text='Conversor de Medidas', font=('Arial black', 20), fg='blue')
    texto_nova_janela.grid(row=0, column=0, columnspan=3, pady=50)

    # Nomeando a caixa de entrada de dados
    texto = tk.Label(nova_janela, text='Insira a medida que deseja converter', font=('Arial black', 16), fg='purple')
    texto.grid(row=1, column=0, columnspan=3, pady=10)

    # Caixa de entrada de dados 
    campo2 = tk.Entry(nova_janela, width=30)
    campo2.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    # Criando um Label para exibir o resultado
    total = tk.Label(nova_janela, text='Selecione o tipo de conversão', font=('Arial black', 16), fg='Red')
    total.grid(row=3, columnspan=3, pady=5)

    def C1():
        num1 = float(campo2.get())
        resultado = num1 / 100
        total.config(text=f'O resultado é {resultado:.2f} Metros')

    def C2():
        num1 = float(campo2.get())
        resultado = num1 / 100000
        total.config(text=f'O resultado é {resultado:.2f} Quilômetros')

    def M1():
        num1 = float(campo2.get())
        resultado = num1 * 100
        total.config(text=f'O resultado é {resultado:.2f}F= Centímetros')

    def M2():
        num1 = float(campo2.get())
        resultado = num1 / 1000
        total.config(text=f'O resultado é {resultado:.2f} Quilômetros')

    def KM1():
        num1 = float(campo2.get())
        resultado = num1 * 100000
        total.config(text=f'O resultado é {resultado:.2f} Centímetros')

    def KM2():
        num1 = float(campo2.get())
        resultado = num1 * 1000
        total.config(text=f'O resultado é {resultado:.2f} Metros')

    # Criando os botões de ação usando grid
    botao1 = tk.Button(nova_janela, text="CM para M", command=C1, bg='#90EE90')
    botao1.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

    botao2 = tk.Button(nova_janela, text="CM para KM", command=C2, bg='#90EE90')
    botao2.grid(row=4, column=1, padx=10, pady=10, sticky='ew')

    botao3 = tk.Button(nova_janela, text="M para CM", command=M1, bg='#90EE90')
    botao3.grid(row=4, column=2, padx=10, pady=10, sticky='ew')

    botao4 = tk.Button(nova_janela, text="M para KM", command=M2, bg='#90EE90')
    botao4.grid(row=5, column=0, padx=10, pady=10, sticky='ew')

    botao5 = tk.Button(nova_janela, text="KM para CM", command=KM1, bg='#90EE90')
    botao5.grid(row=5, column=1, padx=10, pady=10, sticky='ew')

    botao6 = tk.Button(nova_janela, text="KM para M", command=KM2, bg='#90EE90')
    botao6.grid(row=5, column=2, padx=10, pady=10, sticky='ew')

    # Adicionando um botão para fechar a nova janela
    botao_fechar = tk.Button(nova_janela, text='Fechar', command=nova_janela.destroy, bg='red')
    botao_fechar.grid(row=10, column=0, columnspan=3, padx= 10, pady= 10)

    nova_janela.grid_columnconfigure(0, weight=1)
    nova_janela.grid_columnconfigure(1, weight=1)
    nova_janela.grid_columnconfigure(2, weight=1)

# Botão para abrir a nova janela
botao_nova_janela = tk.Button(janela, text="Abrir Conversor de Medidas", command=abrir_nova_janela, bg='#ADD8E6')
botao_nova_janela.grid(row=6, column=0, columnspan=3, pady=30)

# Loop principal da interface gráfica
janela.mainloop()
