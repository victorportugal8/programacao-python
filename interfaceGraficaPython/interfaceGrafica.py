# Primeiro teste
# import tkinter

# janela = tkinter.Tk()
# janela.mainloop()

# Segundo teste Widget Window- Janela redimensionável
# import tkinter as tk

# janela = tk.Tk()
# janela.title("Aplicação GUI")
# janela.mainloop()

# Teste janela tamanho fixo
# import tkinter as tk

# janela = tk.Tk()
# janela.title("Aplicação GUI NÃO Dimensionável")
# janela.resizable(False, False)
# janela.mainloop()

# Terceiro teste - Widget Label
# import tkinter as tk
# from tkinter import ttk

# janela = tk.Tk()
# janela.title("Aplicação GUI com Widget Label")
# ttk.Label(janela, text = "Componente Label").grid(column = 0, row = 0)
# janela.mainloop()

# Quarto teste - Widget Button
# import tkinter as tk

# contador = 0
# def contador_label(lblRotulo):
#     def funcao_contar():
#         global contador
#         contador += 1
#         lblRotulo.config(text = str(contador))
#         lblRotulo.after(1000, funcao_contar)
#     funcao_contar()
# janela = tk.Tk()
# janela.title("Contagem dos segundos")
# lblRotulo = tk.Label(janela, fg = "green")
# lblRotulo.pack()
# contador_label(lblRotulo)
# btnAcao = tk.Button(janela, text = "Clique aqui para interromper a contagem", width = 50, command = janela.destroy)
# btnAcao.pack()
# janela.mainloop()

# Quinto teste - widget Entry
# import tkinter as tk

# def mostar_nomes():
#     print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))

# janela = tk.Tk()
# janela.title("Aplicação GUI como widget Entry")

# tk.Label(janela, text = "Nome").grid(row = 0)
# tk.Label(janela, text = "Sobrenome").grid(row = 1)

# e1 = tk.Entry(janela)
# e2 = tk.Entry(janela)

# e1.grid(row = 0, column = 1)
# e2.grid(row = 1, column = 1)

# tk.Button(janela, text = "Sair", command = janela.quit).grid(row = 3, column = 0, sticky = tk.W, pady = 4)
# tk.Button(janela, text = "Exibir dados", command = mostar_nomes).grid(row = 3, column = 1, sticky = tk.W, pady = 4)
# janela.mainloop()

# Sexto teste - widget RadioButton
# import tkinter as tk

# janela = tk.Tk()

# v = tk.IntVar()

# tk.Label(janela, text = """Escolha uma linguagem de programação:""", justify = tk.LEFT, padx = 20).pack()
# tk.Radiobutton(janela, text = "Python", padx = 25, variable = v, value = 1).pack(anchor = tk.W)
# tk.Radiobutton(janela, text = "C++", padx = 25, variable = v, value = 2).pack(anchor = tk.W)

# janela.mainloop()

# Sétimo teste - widget Checkbutton
# import tkinter as tk
# from tkinter import ttk

# janela = tk.Tk()

# def escolha_carreira():
#     print("Gerencial: %d, \nTécnica: %d" % (var1.get(), var2.get()))

# ttk.Label(janela, text = "Escolha sua vocação:").grid(row = 0, sticky = tk.W)

# var1 = tk.IntVar()
# ttk.Checkbutton(janela, text = "Gerencial", variable = var1).grid(row = 1, sticky = tk.W)

# var2 = tk.IntVar()
# ttk.Checkbutton(janela, text = "Técnica", variable = var2).grid(row = 2, sticky = tk.W)

# ttk.Button(janela, text = "Sair", command = janela.quit).grid(row = 3, sticky = tk.W, pady = 4)
# ttk.Button(janela, text = "Mostrar", command = escolha_carreira).grid(row = 4, sticky = tk.W, pady = 4)

# janela.mainloop()

# Oitavo teste - widget Text
# import tkinter as tk

# janela = tk.Tk()

# T = tk.Text(janela, height = 2, width = 30)
# T.pack()
# T.insert(tk.END, "Este é um texto\ncom duas linhas\n")

# janela.mainloop()

# Nono teste - widget Message
# import tkinter as tk

# janela = tk.Tk()

# mensagem_para_usuario = "Esta é uma mensagem. \n(Pode ser bastante útil para o usuário)"

# msg = tk.Message(janela, text = mensagem_para_usuario)
# msg.config(bg = "lightgreen", font = ("times", 24, "italic"))
# msg.pack()

# janela.mainloop()

# Décimo teste - widget Slider
# import tkinter as tk
# from tkinter import ttk

# def mostrar_valores():
#     print(w1.get(), w2.get())

# janela = tk.Tk()

# w1 = ttk.Scale(janela, from_ = 0, to = 50)
# w1.pack()

# w2 = ttk.Scale(janela, from_ = 0, to = 100, orient = tk.HORIZONTAL)
# w2.pack()

# ttk.Button(janela, text = "Mostrar a escala", command = mostrar_valores).pack()

# janela.mainloop()

# Décimo primeiro teste - widget Dialog
# import tkinter as tk
# from tkinter import messagebox as mb

# def resposta():
#     mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")
# def verificacao():
#     if mb.askyesno("Veriricar", "Realmente quer sair?"):
#         mb.showwarning("Yes", "Ainda não foi implementado")
#     else:
#         mb.showinfo("No", "A opção de sair foi cancelada")
# tk.Button(text = "Sair", command = verificacao).pack(fill = tk.X)
# tk.Button(text = "Resposta", command = resposta).pack(fill = tk.X)
# tk.mainloop()

# Décimo segundo teste - widget Combobox
import tkinter as tk
from tkinter import ttk

# Criação de uma janela tkinter
janela = tk.Tk()
janela.title("Combobox")
janela.geometry("500x250")

# Componente Label
ttk.Label(janela, text = "Combobox Widget", background = "green", foreground = "white", font = ("Times New Roman", 15)).grid(row = 0, column = 1)

# Componente Label
ttk.Label(janela, text = "Selecione um mês:", font = ("Times New Roman", 10)).grid(column = 0, row = 5, padx = 10, pady = 25)

# Componente Combobox
n = tk.StringVar()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)

# Adição de itens no Combobox
escolha["values"] = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
escolha.grid(column = 1, row = 5)
escolha.current()

janela.mainloop()