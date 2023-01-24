"""
Lê um número entre 1 e 1000 e sorteia indefinidos números até que o seu número tenha sido sorteado. Em seguida, mostra a quantidade de simulações feitas.
"""

from random import randint

n = int(input("Digite um número entre 1 e 1000: "))
nSorteado = randint(1, 1000)
qtdSimulacao = 0

while(n != nSorteado):
	nSorteado = randint(1, 1000)
	qtdSimulacao += 1

print("\nO número foi sorteado depois de ", qtdSimulacao, " sorteios.")

"""
Solicitar 6 números da mega sena e sortear N 'sorteios', até que o usuário tenha ganhado o jogo.
"""

jogo = []

for i in range(6):
	jogo.append(int(input("Digite o {:d}º número: ".format(i + 1))))

sena = []
qtdSimulacao = 0
qtdAcertos = 0
acertos = 0

while(acertos < 6):
	sena = []
	acertos = 0
	qtdSimulacao += 1
	for i in range(6):
		sena.append(randint(1, 60))
	for i in range(6):
		for j in range(6):
			if(sena[i] == jogo[j]):
				acertos += 1

print("\nVocê ganhará na mega sena depois de ", qtdSimulacao, " sorteios.")
print("\nO resultado foi ", sena, ".")