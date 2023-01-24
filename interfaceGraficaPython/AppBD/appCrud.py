import tkinter as tk
from tkinter import ttk
import crud as crud

class PrincipalBD:
    def __init__(self, win):
        self.objBD = crud.AppBD()
        # Compenentes da GUI
        self.lblCodigo = tk.Label(win, text = "Codigo do Produto")
        self.lblNome = tk.Label(win, text = "Nome do Produto")
        self.lblPreco = tk.Label(win, text = "Preço")

        self.txtCodigo = tk.Entry(bd = 3)
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        self.btnCadastrar = tk.Button(win, text = "Cadastrar", command = self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text = "Atualizar", command = self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text = "Excluir", command = self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text = "Limpar", command = self.fLimparTela)

        # Componentes TreeView
        self.dadosColunas = ("Codigo", "Nome", "Preço")
        
        self.treeProdutos = ttk.Treeview(win, columns = self.dadosColunas, selectmode = "browse")
        
        self.verscrlbar = ttk.Scrollbar(win, orient = "vertical", command = self.treeProdutos.yview)
        
        self.verscrlbar.pack(side = "right", fill = "x")
        
        self.treeProdutos.configure(yscrollcommand = self.verscrlbar.set)
        
        self.treeProdutos.heading("Codigo", text = "Codigo")
        self.treeProdutos.heading("Nome", text = "Nome")
        self.treeProdutos.heading("Preço", text = "Preço")

        self.treeProdutos.column("Codigo", minwidth = 0, width = 100)
        self.treeProdutos.column("Nome", minwidth = 0, width = 100)
        self.treeProdutos.column("Preço", minwidth = 0, width = 100)

        self.treeProdutos.pack(padx = 10, pady = 10)

        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        # Posicionamento dos componentes na janela
        self.lblCodigo.place(x = 100, y = 50)
        self.txtCodigo.place(x = 250, y = 50)

        self.lblNome.place(x = 100, y = 100)
        self.txtNome.place(x = 250, y = 100)

        self.lblPreco.place(x = 100, y = 150)
        self.txtPreco.place(x = 250, y = 150)

        self.btnCadastrar.place(x = 100, y = 200)
        self.btnAtualizar.place(x = 200, y = 200)
        self.btnExcluir.place(x = 300, y = 200)
        self.btnLimpar.place(x = 400, y = 200)

        self.treeProdutos.place(x = 100, y = 300)
        self.verscrlbar.place(x = 805, y = 300, height = 225)
        self.carregarDadosIniciais()
    
# Apresentando os registros selecionandos
    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection():
            item = self.treeProdutos.item(selection)
            codigo, nome, preco = item["values"] [0 : 3]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)

# Carregando os dados iniciais
    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            print("***** Dados disponíveis no BD *****")
            
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                print("Codigo = ", codigo)
                print("Nome = ", nome)
                print("Preço = ", preco, "\n")

                self.treeProdutos.insert("", "end", iid = self.iid, values = (codigo, nome, preco))
                self.iid += 1
                self.id += 1
            print("Dados da base")
        except:
            print("Ainda não existem dados para carregar.")
# Ler dados da tela
    def fLerCampos(self):
        try:
            print("***** Dados disponíveis *****")
            
            codigo = int(self.txtCodigo.get())
            print("Codigo", codigo)

            nome = self.txtNome.get()
            print("Nome", nome)

            preco = float(self.txtPreco.get())
            print("Preço", preco)

            print("Leitura dos dados realizada com sucesso!")
        except:
            print("Não foi possível ler os dados.")
        return codigo, nome, preco
# Cadastrar produtos
    def fCadastrarProduto(self):
        try:
            print("***** Dados disponíveis *****")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.treeProdutos.insert("", "end", iid = self.iid, values = (codigo, nome, preco))
            self.iid += 1
            self.id += 1
            self.fLimparTela()
            print("Produto cadastrado com sucesso!")
        except:
            print("Não foi possível fazer o cadastro do produto.")
# Atualizar produtos
    def fAtualizarProduto(self):
        try:
            print("***** Dados disponíveis *****")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.atualizarDados(codigo, nome, preco)
            # recarregar os dados na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto atualizado com sucesso!")
        except:
            print("Não foi possível fazer a atualização do produto.")
# Excluir produtos
    def fExcluirProduto(self):
        try:
            print("***** Dados disponíveis *****")
            codigo, nome, preco = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            # recarregar os dados na tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
            print("Produto excluído com sucesso!")
        except:
            print("Não foi possível fazer a exclusão do produto.")
# Limpar tela
    def fLimparTela(self):
        try:
            print("***** Dados disponíveis ******")
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print("Campos limpos!")
        except:
            print("Não foi possível limpar os campos.")

# PROGRAMA PRINCIPAL - RESPONSÁVEL POR INICIAR A EXECUÇÃO DO SISTEMA
janela = tk.Tk()
principal = PrincipalBD(janela)
janela.title("Bem vindo a Aplicação de Banco de Dados")
janela.geometry("820x600+10+10")
janela.mainloop()