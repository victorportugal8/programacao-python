from random import randint

sorteado = randint(1, 100)
erros = 0
chute = 0

while(chute != sorteado):
    chute = int(input("Digite um número entre 1 e 100 "))
    if(chute > sorteado):
        print("Você errou, o número é menor!")
        erros = erros + 1
    if(chute < sorteado):
        print("Você errou, o número é maior!")
        erros = erros + 1

print("Você acertou, mas errou", erros, "vezes.")