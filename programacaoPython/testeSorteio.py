"""
Pede ao usuário para escolher uma quantidade X de vezes para serem sorteados números entre 0 e 99. Em seguida, mostra a quantidade de vezes que cada número saiu e sua
representação em porcentagem
"""

from random import randint

vetor = []

for i in range(100):
	vetor.append(0)
n = int(input("Digite a quantidade de elementos a serem sorteados: "))

for i in range(n):
	v = randint(0, 99)
	vetor[v] += 1
for i in range(100):
	print(i, " saiu ", vetor[i], " \tvezes. O que corresponde a {:.2f}%.".format(vetor[i] / (n * 100)))