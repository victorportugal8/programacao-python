# Classe que possuí os métodos CRUD

import psycopg2

class AppBD:
    def __init__(self):
        print("Método construtor")
    
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connection(user = "postgres", password = "051718", host = "127.0.0.1", port = "5432", database = "postgres")
        except(Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao se conectar ao banco de dados", error)

# Selecionando todos os produtos

    def selecionarDados(self):
        try:
            self.abrirConexao()
            cursor = self.connectior.cursor()
            print("Selecionando todos os produtos")
            sql_select_query = """
                SELECT * FROM public.PRODUTO
            """
            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            print(registros)
        except(Exception, psycopg2.Error) as error:
            print("Erro na operação select", error)
        finally:
            # fechando a conexão com o banco de dados
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexaão com o PostgreSQL foi fechada.")
        return registros

# Inserindo produtos

    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgres_insert_query = """
                INSERT INTO public.PRODUTO(CODIGO, NOME, PRECO)
                VALUES(%s, %s, %s)
            """
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except(Exception, psycopg2.Error) as error:
            if(self.connection):
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            # fechando a conexão com o banco de dados
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

# Atualizar produto

    def atualizarDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            print("Registro antes da atualização")
            sql_select_query = """
                SELECT * FROM public.PRODUTO WHERE CODIGO = %s
            """
            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)
            # Atualizar registro
            sql_update_query = """
                UPDATE public.PRODUTO
                SET NOME = %s, PREECO = %s
                WHERE CODIGO = %s
            """
            cursor.execute(sql_update_query, (nome, preco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro atualizado com sucesso!")
            print("Registro depois da atualização")
            sql_select_query = """
                SELECT * FROM public.PRODUTO
                WHERE CODIGO = %s
            """
            cursor.execute(sql_select_query, (codigo))
            record = cursor.fetchone()
            print(record)
        except(Exception, psycopg2.Error) as error:
            print("Erro na atualização", error)
        finally:
            # fechando a conexão com o banco de dados
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

# Excluir produto
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            # Apagar registro
            sql_delete_query = """
                DELETE FROM public.PRODUTO
                WHERE CODIGO = %s
            """
            cursor.execute(sql_delete_query, (codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro excluído com sucesso!")
        except(Exception, psycopg2.Error) as error:
            print("Erro na exclusão", error)
        finally:
            # fechando conexão com o banco de dados
            if(self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")