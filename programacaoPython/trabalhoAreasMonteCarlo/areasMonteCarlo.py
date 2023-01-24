from random import uniform
import math

qtd = int(input("Quantos pontos deseja? "))

#Cálculo da área do círculo com raio 1
acertos = 0

for i in range(qtd):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    d = math.sqrt((float(x ** 2)) + (float(y ** 2)))
    if(d <= 1):
        acertos += 1

area = acertos / qtd * 4
print("Área do círculo = {:.3f}".format(area))

#Cálculo da área da função quadrática
A = float(input("Digite o valor de A da função quadrática: "))
B = float(input("Digite o valor de B da função quadrática: "))
C = float(input("Digite o valor de C da função quadrática: "))

delta = math.pow(B, 2) - (4 * A * C)
X1 = (-B + math.sqrt(delta)) / (2 * A)
X2 = (-B - math.sqrt(delta)) / (2 * A)
Vy = -delta / (4 * A)

acertos = 0

if(X1 > X2):
    aux = X1
    X1 = X2
    X2 = aux

print("X1 = ", X1, "\nX2 = ", X2, "\nVértice Y = ", Vy)

if(Vy < 0):
    Vy = Vy * (-1)

for i in range(qtd):
    x = uniform(X1, X2)
    y = uniform(0, Vy)
    Fy = A * x ** 2 + B * x + C
    if(y <= Fy): #se Y está dentro da parábola
        acertos += 1

areaRetangulo = (X2 - X1) * Vy
print("Área do retângulo = {:.3f}".format(areaRetangulo))

area = areaRetangulo * acertos / qtd
print("Área da função quadrática = {:.2f}".format(area))

#Cálculo da área do triângulo
X1 = float(input("Digite a coordenada do ponto X1: "))
X2 = float(input("Digite a coordenada do ponto X2: "))
X3 = float(input("Digite a coordenada do ponto X3: "))
Y = float(input("Digite a altura do triângulo: "))

x = uniform(X1, X3)
y = uniform(0, Y)
acertos = 0

for i in range(qtd):
    if(x >= X2): #para a função decrescente
        a = Y / (X3 - X2)
        b = Y - a * X2
        yF = a * x + b
        if(yF <= Y):
            acertos += 1
    else: #para a função crescente
        a = Y / (X2 - X1)
        b = Y - a * X2
        yF = a * x + b
        if(yF <= Y):
            acertos += 1

areaRetangulo = (X3 - X1) * Y
area = areaRetangulo * acertos / qtd
print("Área do retângulo = {:.3f}".format(areaRetangulo))
print("Área do triângulo = {:.2f}".format(area))