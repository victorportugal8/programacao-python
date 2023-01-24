from itertools import permutations

def permutacao(qtd):
    vet = []
    for i in range(qtd):
        vet.append(i)
    return permutations(vet)

qtd = int(input("Quantos elementos? "))
perm = permutacao(qtd)

for i in perm:
    for j in range(len(i)):
        print(i[j]) #fazer a implementação aqui!
    print("\n")