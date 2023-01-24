import socket

porta = 65000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
origem = ("", porta)
udp.bind(origem)
print("\nServidor iniciado, aguardando clientes\n")

msg = ""
while(msg.upper() != "SAIR"):
    msg, cliente = udp.recvfrom(1024)
    print("O cliente ", cliente, "enviou: ", msg)
print("Conexão encerrada\n")
udp.close()