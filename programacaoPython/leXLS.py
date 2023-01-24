import pandas as pd

arqXLS = pd.read_excel("teste.xlsx")
txt = arqXLS.get("Nome")
print(txt)