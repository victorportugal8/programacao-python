import numpy as np
from random import randint

n = 3
ehMagica = 0

while(ehMagica == 0):
    ehMagica = 1
    valor = 1
    matriz = np.zeros((n, n))
    while(valor <= (n * n)):
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        if(matriz[x][y] == 0):
            matriz[x][y] = valor
            valor += 1
    
    base = 0
    for i in range(n):
        base += matriz[i][i]
    
    for i in range(n):
        linha = 0
        for j in range(n):
            linha += matriz[i][j]
        if(linha != base):
            ehMagica = 0
    
    for i in range(n):
        coluna = 0
        for j in range(n):
            coluna += matriz[j][i]
        if(coluna != base):
            ehMagica = 0
    
    diagSecundaria = 0
    j = n - 1
    for i in range(n):
        diagSecundaria += mat[i][j]
        j -= 1
    
    if(diagSecundaria != base):
        ehMagica = 0

print("\nMATRIZ\n")
for i in range(n):
    for j in range(n):
        print("{:5.0f}".format(mat[i][j], end = "\t")
    print("\n")