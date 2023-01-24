def cadastrarCliente(arquivo, nome):
    cliente = {}
    cliente["nome"] = nome
    cliente["email"] = []
    cliente["telefone"] = []
    arquivo.append(cliente)

def inserirEmail(arquivo, nome, email):
    for cliente in arquivo:
        if(cliente["nome"] == nome):
            cliente["email"] += email.split()
            return
    print("Nome não encontrado.")

def excluirCliente(arquivo, nome):
    for cliente in arquivo:
        if(cliente["nome"] == nome):
            arquivo.remove(cliente)
            return
    print("Nome não encontrado.")

def inserirTelefone(arquivo, nome, telefone):
    for cliente in arquivo:
        if(cliente["nome"] == nome):
            cliente["telefone"] += telefone.split()
            return
    print("Nome não encontrado.")

def listarClientes(arquivo):
    for cliente in arquivo:
        for chave in cliente:
            print(chave, ": ", cliente[chave])
        print("\n___________________________\n")

def menu(arquivo):
    while(True):
        print("Escolha uma opção:\n")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar e-mail")
        print("3 - Cadastrar telefone")
        print("4 - Listar clientes")
        print("5 - SAIR\n")
        opcao = int(input())

        if(opcao == 1):
            nome = input("Qual o nome do cliente?\n")
            cadastrarCliente(arquivo, nome)
        elif(opcao == 2):
            nome = input("Qual o nome do cliente?\n")
            email = input("Digite o(s) e-mail(s):\n")
            inserirEmail(arquivo, nome, email)
        elif(opcao == 3):
            nome = input("Qual o nome do cliente?\n")
            telefone = input("Digite o(s) telefone(s)\n")
            inserirTelefone(arquivo, nome, telefone)
        elif(opcao == 4):
            listarClientes(arquivo)
        elif(opcao == 5):
            return
        else:
            print("\nOpção inválida. Por favor, digite uma opção válida(1 à 5).")
        
import pickle

try:
    arquivo = pickle.load(open("cadastroCliente.dat", "rb"))
    menu(arquivo)
    print("Salvando o arquivo e saindo...")
    pickle.dump(arquivo, open("cadastroCliente.dat", "wb"))
except FileNotFoundError:
    arquivo = []
    menu(arquivo)
    pickle.dump(arquivo, open("cadastroCliente.dat", "wb"))
except IOError:
    print("Erro de entrada/saída!")