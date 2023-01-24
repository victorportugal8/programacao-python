from random import randint

arquivo = open("arquivo.txt", "w")

for i in range(1000000):
    letra = chr(randint(65, 90))
    arquivo.write(letra)

    if(randint(1, 100) < 30):
        arquivo.write(" ")
    
    if(randint(1, 100) > 95):
        arquivo.write("\n")

arquivo.close()