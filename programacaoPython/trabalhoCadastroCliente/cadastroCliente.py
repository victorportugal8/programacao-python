def cadastrarCliente(arquivo, identificador):
    cliente = {}
    cliente["identificador"] = identificador #criando o campo ID no objeto cliente
    cliente["nome"] = []
    cliente["sobrenome"] = [] #criando o campo sobrenome no objeto cliente
    cliente["email"] = []
    cliente["telefone"] = []
    cliente["endereco"] = [] #criando o campo endereço no objeto cliente
    arquivo.append(cliente)

def inserirNome(arquivo, identificador, nome): #adicionando a função para cadastrar nome
    for cliente in arquivo:
        if(cliente["identificador"] == identificador):
            cliente["nome"] += nome.split()
            return
    print("ID não encontrado.")

def inserirSobrenome(arquivo, identificador, sobrenome): #adicionando a função para cadastrar sobrenome
    for cliente in arquivo:
        if(cliente["identificador"] == identificador):
            cliente["sobrenome"] += sobrenome.split()
            return
    print("ID não encontrado.")

def inserirEmail(arquivo, identificador, email):
    for cliente in arquivo:
        if(cliente["identificador"] == identificador):
            cliente["email"] += email.split()
            return
    print("ID não encontrado.")

def excluirCliente(arquivo, identificador):
    for cliente in arquivo:
        if(cliente["identificador"] == identificador):
            arquivo.remove(cliente)
            return
    print("ID não encontrado.")

def inserirTelefone(arquivo, identificador, telefone):
    for cliente in arquivo:
        if(cliente["identificador"] == identificador):
            cliente["telefone"] += telefone.split()
            return
    print("ID não encontrado.")

def listarClientes(arquivo):
    for cliente in arquivo:
        for chave in cliente:
            print(chave, ": ", cliente[chave])
        print("\n___________________________\n")

def inserirEndereco(arquivo, identificador, endereco): #adicionando a função para cadastrar endereço
    for cliente in arquivo:
        if(cliente["identificador"] == identificador):
            cliente["endereco"] += endereco.split()
            return
    print("ID não encontrado.")

def menu(arquivo):
    while(True):
        print("Escolha uma opção:\n")
        print("1 - Cadastrar cliente")
        print("2 - Cadastrar nome") #adicionando a opção de cadastrar nome
        print("3 - Cadastrar sobrenome") #adicionando a opção de cadastrar sobrenome
        print("4 - Cadastrar endereço") #adicionando a opção de cadastrar endereço
        print("5 - Cadastrar telefone")
        print("6 - Cadastrar e-mail")
        print("7 - Listar clientes")
        print("8 - SAIR\n")
        opcao = int(input())

        if(opcao == 1):
            identificador = input("Qual o ID do cliente?\n")
            cadastrarCliente(arquivo, identificador)
        elif(opcao == 2): #adicionando a opção de cadastrar o nome
            identificador = input("Qual o ID do cliente?\n")
            nome = input("Digite o nome do cliente:\n")
            inserirNome(arquivo, identificador, nome)
        elif(opcao == 3): #adicionando a opção de cadastrar o sobrenome
            identificador = input("Qual o ID do cliente?\n")
            sobrenome = input("Digite o sobrenome do cliente:\n")
            inserirSobrenome(arquivo, identificador, sobrenome)
        elif(opcao == 4): #adicionando a opção de cadastrar endereço
            identificador = input("Qual o ID do cliente?\n")
            endereco = input("Digite o endereço(logradouro, número, bairro, cidade, estado e CEP):\n")
            inserirEndereco(arquivo, identificador, endereco)
        elif(opcao == 5):
            identificador = input("Qual o ID do cliente?\n")
            telefone = input("Digite o(s) telefone(s) do cliente:\n")
            inserirTelefone(arquivo, identificador, telefone)
        elif(opcao == 6):
            identificador = input("Qual o ID do cliente?\n")
            email = input("Digite o(s) e-mail(s) do cliente:\n")
            inserirEmail(arquivo, identificador, email)
        elif(opcao == 7):
            listarClientes(arquivo)
        elif(opcao == 8):
            return
        else:
            print("\nOpção inválida. Por favor, digite uma opção válida(1 à 8).")
        
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