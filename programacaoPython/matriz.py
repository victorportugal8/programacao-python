import numpy as np

matriz = []
linha = []

for i in range(10):
    for j in range(10):
        linha.append(".")
    matriz.append(linha)

for i in range(10):
    for j in range(10):
        print(matriz[i][j], end = "\t")
    print("\n")