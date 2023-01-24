# Criando a tabela produto no BD
import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "051718", host = "127.0.0.1", port = "5432")
print("Conexão com o banco de dados feita com sucesso!")

cur = conn.cursor()
cur.execute('''
    CREATE TABLE PRODUTO(CODIGO INT PRIMARY KEY NOT NULL,
    NOME TEXT NOT NULL,
    PRECO REAL NOT NULL);
''')
print("Tabela criada com suceso!")
conn.commit()
conn.close()