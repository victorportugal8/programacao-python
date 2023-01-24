import socket, pickle

host = "127.0.0.1"
porta = 65001
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((host, porta))
print("\nServidor iniciado, aguardando clientes\n")
tcp.listen(1)
conexao, cliente = tcp.accept()
dados = conexao.recv(1024)
matriz = pickle.loads(dados)

print(matriz)
tcp.close()