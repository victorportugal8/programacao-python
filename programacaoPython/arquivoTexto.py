import os
import pandas as pd

caminho = "pasta1/pasta2/"
arq = caminho + "teste.txt"

if(not os.path.exists(caminho)):
    os.makedirs(caminho)

arquivo = open(arq, "w")
arquivo.write("Olá mundo!")
arquivo.close()

arquivo = open(arq, "r")
print(arquivo.read())
arquivo.close()

"""
arqXLS = pd.read_excel("arquivo.xlsx", sheet_name = "pasta1")
print(arqXLS.get("Coluna 1"))
"""