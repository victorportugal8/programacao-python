import socket, pickle

host = "127.0.0.1"
porta = 65001
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((host, porta))
matriz = ([0, 1, 2, 3, 4, 5], [9, 8, 7, 6, 5, 4])
dados = pickle.dumps(matriz)
tcp.send(dados) #dados = tcp.recv(1024)
tcp.close()