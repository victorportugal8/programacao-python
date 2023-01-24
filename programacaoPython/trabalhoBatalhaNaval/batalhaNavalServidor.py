import socket, pickle
from random import  randint

host = "127.0.0.1"
porta = 65000

matrizJogo = []
matrizAdversario = []

for i in range(10):
    linha1 = []
    linha2 = []
    for j in range(10):
        linha1.append(".")
        linha2.append(".")
    matrizJogo.append(linha1)
    matrizAdversario.append(linha2)

barcos = 0

while(barcos < 5): #barcos que ocupam uma posição
    x = randint(0, 9)
    y = randint(0, 9)
    if(matrizJogo[x][y] == "."):
        matrizJogo[x][y] = "B"
        barcos += 1

barcos = 0

while(barcos < 5): #submarinos que ocupam duas posições
    x = randint(0, 9)
    y = randint(0, 9)
    if(matrizJogo[x][y] == "."):
        lateral = randint(1, 4)
        if((lateral == 1) and (x + 1 <= 9) and (matrizJogo[x + 1][y] == ".")): #limite da direita
            matrizJogo[x + 1][y] = "S"
            matrizJogo[x][y] = "S"
            barcos += 1
        if((lateral == 2) and (y + 1 <= 9) and (matrizJogo[x][y + 1] == ".")): #limite inferior
            matrizJogo[x][y + 1] = "S"
            matrizJogo[x][y] = "S"
            barcos += 1
        if((lateral == 3) and (x - 1 >= 0) and (matrizJogo[x - 1][y] == ".")): #limite da esquerda
            matrizJogo[x - 1][y] = "S"
            matrizJogo[x][y] = "S"
            barcos += 1
        if((lateral == 4) and (y - 1 >= 0) and (matrizJogo[x][y - 1] == ".")): #limite superior
            matrizJogo[x][y - 1] = "S"
            matrizJogo[x][y] = "S"
            barcos += 1

acertosAdversario = 0
acertosJogador = 0

tcp.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((host, porta))
tcp.listen(1)
print("Servidor iniciado!\nAguardando jogador...\n")
conexao, cliente = tcp.accept()

while(acertosAdversario < 5 and acertosJogador < 5):
    print("\n\n\t\tMATRIZ DE JOGO\n")
    print("\t0   1   2   3   4   5   6   7   8   9\n")
    for i in range(10):
        print("\n", i, end="\t")
        for j in range(10):
            print(matrizAdversario[i][j], end="   ")
        print()
    print("\n\n\t\tSUA MATRIZ\n")
    print("\t0   1   2   3   4   5   6   7   8   9\n")
    for i in range(10):
        print("\n", i, end="\t")
        for j in range(10):
            print(matrizJogo[i][j], end="   ")
        print()
    
    dados = conexao.recv(1024)
    coordenada = pickle.loads(dados)

    print("Jogador atirou em (X = ", coordenada[0], " Y = ", coordenada[1], ")")

    acertou = []

    if(matrizJogo[int(coordenada[0])][int(coordenada[1])] == "B"):
        print("Perigo!\nO adversário acertou um barco.")
        acertou.append("B")
        acertou.append("B")
        matrizJogo[int(coordenada[0])][int(coordenada[1])] = "X"
    elif(matrizJogo[int(coordenada[0])][int(coordenada[1])] == "S"):
        print("Perigo!\nO adversário acertou um submarino.")
        acertou.append("S")
        acertou.append("S")
        matrizJogo[int(coordenada[0])][int(coordenada[1])] = "X"
    else:
        print("Que sorte!\nO adversário acertou na água.")
        acertou.append("A")
        acertou.append("A")
        matrizJogo[int(coordenada[0])][int(coordenada[1])] = "A"
    
    dados = pickle.dumps(acertou)
    conexao.send(dados)

    coordenada = []
    x = input("\nDigite a coordenada X: ")
    coordenada.append(x)
    y = input("\nDigite a coordenada Y: ")
    coordenada.append(y)

    dados = pickle.dumps(coordenada)
    conexao.send(dados)

    dados = conexao.recv(1024)
    acertou = pickle.loads(dados)

    if(acertou[0] == "B"):
        print("Parabéns!\nVocê acertou um barco.")
        matrizAdversario[int(x)][int(y)] = "X"
        acertosJogador += 1
    elif(acertou[0] == "S"):
        print("Parabéns!\nVocê acertou um submarino.")
        matrizAdversario[int(x)][int(y)] = "X"
        acertosJogador += 1
    else:
        print("Que pena!\nVocê acertou na água.")
        matrizAdversario[int(x)][int(y)] = "A"

tcp.close()