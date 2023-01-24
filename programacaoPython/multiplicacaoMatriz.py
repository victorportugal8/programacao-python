from random import randint

n = 5
matrizA = []
matrizB = []
matrizC = []

for i in range(n):
    linha = []
    linha2 = []
    for j in range(n):
        linha.append(randint(1, 9))
        linha2.append(randint(1, 9))
    matrizA.append(linha)
    matrizB.append(linha2)

print("\nMATRIZ A \n")
for i in range(n):
    for j in range(n):
        print(matrizA[i][j], end = "\t")
    print("\n")

print("\nMATRIZ B \n")
for i in range(n):
    for j in range(n):
        print(matrizB[i][j], end = "\t")
    print("\n")

for i in range(n):
    linha = []
    for j in range(n):
        soma = 0
        for k in range(n):
            soma += matrizA[i][k] * matrizB[k][j]
        linha.append(soma)
    matrizC.append(linha)

print("\nMATRIZ C\n")
for i in range(n):
    for j in range(n):
        print(matrizC[i][j], end = "\t")
    print("\n")