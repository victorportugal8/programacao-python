# Inserir regitro numa tabela a partir do Python

import psycopg2

conn = psycopg2.connect(database = "postgres", user = "postgres", password = "051718", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")

cur = conn.cursor()
cur.execute("""
    INSERT INTO public."AGENDA"("id", "nome", "telefone")
    VALUES (1, 'Gojo Satoru', '11111111111');
""")

conn.commit()
print("Inserção realizada com sucesso!")
conn.close()