import tkinter as tk  # Biblioteca para criar interfaces gráficas

# Função para converter o texto para maiúsculas
def maiuscula():
    # Obtém o texto da caixa de entrada, converte para maiúsculas e insere o resultado de volta
    texto = entrada_texto.get("1.0", "end-1c")  # Obtém todo o texto da caixa, excluindo a nova linha final
    resultado = texto.upper()
    entrada_texto.delete("1.0", "end")  # Remove o texto atual da caixa
    entrada_texto.insert("1.0", resultado)  # Insere o texto convertido em maiúsculas

# Função para converter o texto para minúsculas
def minuscula():
    # Semelhante à função anterior, mas converte para minúsculas
    texto = entrada_texto.get("1.0", "end-1c")
    resultado = texto.lower()
    entrada_texto.delete("1.0", "end")
    entrada_texto.insert("1.0", resultado)

# Função para converter o texto para capitalização do estilo título
def titulo():
    # Converte apenas a primeira letra para maiúscula, as demais para minúsculas
    texto = entrada_texto.get("1.0", "end-1c")
    resultado = texto.capitalize()
    entrada_texto.delete("1.0", "end")
    entrada_texto.insert("1.0", resultado)

# Configura a janela principal e a aparência básica da interface
janela = tk.Tk()
janela.title("Conversor de caso")

fonte_padrao = ("Arial", 15)  # Fonte e tamanho usados nos elementos

# Rótulo e campo de entrada de texto onde o usuário escreve o texto a ser convertido
tk.Label(janela, text="\nTexto:\n", font=fonte_padrao).pack()  # Título do campo de entrada
entrada_texto = tk.Text(janela, font=fonte_padrao, height=5, width=40)  # Caixa de texto com altura e largura ajustáveis
entrada_texto.pack()

# Rótulo e botões que chamam as funções de conversão
tk.Label(janela, text="\nConverter para:\n", font=fonte_padrao).pack()  # Título da seção de botões

# Botões que aplicam as funções de conversão no texto da caixa de entrada
botao_maiuscula = tk.Button(janela, text="MAIÚSCULA", font=fonte_padrao, command=maiuscula)
botao_maiuscula.pack()

botao_minuscula = tk.Button(janela, text="minúscula", font=fonte_padrao, command=minuscula)
botao_minuscula.pack()

botao_titulo = tk.Button(janela, text="Frase", font=fonte_padrao, command=titulo)
botao_titulo.pack()

# Inicia o loop da interface, mantendo a janela e seus elementos visíveis
janela.mainloop()
