from itertools import permutations
import matplotlib.pyplot as plt
from random import randint, uniform
import math
import time

def permutacao(qtd):
    vetor = []
    
    for i in range(qtd):
        vetor.append(i)
    return permutations(vetor)

qtd = int(input("Quantos elementos? "))
t = time.time()
rotas = list(permutacao(qtd))
coordenadaX = []
coordenadaY = []

for i in range(qtd):
    coordenadaX.append(uniform(0, 100))
    coordenadaY.append(uniform(0, 100))

distancia = []

for i in range(qtd):
    linha = []
    
    for j in range(qtd):
        x = coordenadaX[j] - coordenadaX[i]
        y = coordenadaY[j] - coordenadaY[i]
        pitagoras = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
        linha.append(pitagoras)
    distancia.append(linha)

menorCusto = 10000000
menorRota = 0

for i in range(len(rotas)):
    custo = 0
    
    for j in range(qtd - 1):
        custo = custo + distancia[rotas[i][j]][rotas[i][j + 1]]
    
    if(custo < menorCusto):
        menorRota = i
        menorCusto = custo

print("\nMelhor caminho: ", rotas[menorRota], "\n")

t = time.time() - t

print("\nTempo de execução: ", t)

fig, grafico = plt.subplots()
grafico.scatter(coordenadaX, coordenadaY, 100, "red")

vetorX = []
vetorY = []

for i in range(qtd):
    vetorX.append(coordenadaX[rotas[menorRota][i]])
    vetorY.append(coordenadaY[rotas[menorRota][i]])

vetorX.append(vetorX[0])
vetorY.append(vetorY[0])

grafico.plot(vetorX, vetorY)