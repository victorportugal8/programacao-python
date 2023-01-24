arquivo = open("arquivo.txt", "r")
linha = arquivo.readline()

while(linha):
    valores = linha.split()
    for i in valores:
        print(i)
    linha = arquivo.readline

arquivo.close()