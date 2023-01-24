import numpy as np
from random import randint

n = 3
valor = 1
matriz = np.zeros((n, n))

while(valor <= (n * n)):
    x = randint(0, n - 1)
    y = randint(0, n - 1)
    if(matriz[x][y] == 0):
        matriz[x][y] = valor
        valor += 1
print("\nMATRIZ\n")
for i in range(n):
    for j in range(n):
        print("{:5.0f}".format(matriz[i][j]), end = "\t")
    print("\n")