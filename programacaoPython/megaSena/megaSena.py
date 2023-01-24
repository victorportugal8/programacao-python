import pandas as pd
import numpy as np

arquivo = pd.read_excel("megaSena.xlsx")

n1 = arquivo.get("Coluna 1")
n2 = arquivo.get("Coluna 2")
n3 = arquivo.get("Coluna 3")
n4 = arquivo.get("Coluna 4")
n5 = arquivo.get("Coluna 5")
n6 = arquivo.get("Coluna 6")

sena = np.zeros((60, 2), dtype = np.int32)
qtd = len(n1)

for i in range(60):
    sena[i][0] = i + 1

for i in range(qtd):
    v = int(n1[i])
    sena[v - 1][1] += 1
    
    v = int(n2[i])
    sena[v - 1][1] += 1
    
    v = int(n3[i])
    sena[v - 1][1] += 1
    
    v = int(n4[i])
    sena[v - 1][1] += 1
    
    v = int(n5[i])
    sena[v - 1][1] += 1
    
    v = int(n6[i])
    sena[v - 1][1] += 1

for i in range(60):
    for j in range(60):
        if(sena[i][1] > sena[j][1]):
            aux = sena[i][0]
            sena[i][0] = sena[j][0]
            sena[j][0] = aux

            aux = sena[i][1]
            sena[i][1] = sena[j][1]
            sena[j][1] = aux

for i in range(60):
    print("Número ", sena[i][0], " saiu ", sena[i][1], " vezes({:.2f})%.".format(sena[i][1] / qtd / 6 * 100))