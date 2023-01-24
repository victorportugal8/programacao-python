from random import uniform
import math

qtd = int(input("Quantos pontos deseja? "))
acertos = 0

for i in range(qtd):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    d = math.sqrt((float(x ** 2)) + (float(y ** 2)))
    
    if(d <= 1):
        acertos += 1
print((acertos / qtd) * 4)