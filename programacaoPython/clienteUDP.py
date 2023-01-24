import socket

porta = 65000
host = "127.0.0.1" #localhost
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
destino = (host, porta)

msg = ""
while(msg.upper() != "SAIR"):
    msg = input("\nDigite uma mensagem(SAIR PARA ENCERRAR): ")
    udp.sendto(msg.encode(), destino)
udp.close()