import os
os.add_dll_directory(r"C:\\Program Files\\IBM\\SQLLIB\\BIN")  # Ajuste o caminho para o local correto
os.environ["DB2CODEPAGE"] = "1252"

import ibm_db
import csv
import traceback
import pandas as pd
import ibm_db_dbi
import os
from datetime import datetime
from conection.connect_db import conexao_db

conn = conexao_db()


caminho_arquivo_csv = "Dados\\cidades_completas_com_logradouros.csv"
table_name = "CONV.CIDADES_NOVAS_IMPORTAR"




#função que verifica se a tabela existe
def tabela_existe(conn, table_name):
    sql = f"SELECT 1 FROM SYSIBM.SYSTABLES WHERE NAME = '{table_name.split('.')[-1]}'"
    stmt = ibm_db.exec_immediate(conn, sql)
    return ibm_db.fetch_row(stmt)


########## Função que cria a tabela para transformações (CORRIGIDA)
def create_table(conn, table_name):
    if tabela_existe(conn, table_name):
        print(f"Tabela {table_name} já existe, removendo...")
        ibm_db.exec_immediate(conn, f"DROP TABLE {table_name}")
        ibm_db.commit(conn)

    create_sql = f"""
                    CREATE TABLE {table_name} (
                        LOC_NU VARCHAR(100),
                        UF VARCHAR(20),
                        CIDADE VARCHAR(100),
                        CEP VARCHAR(100),
                        SITUACAO VARCHAR(100),
                        COD_IBGE VARCHAR(100),
                        LOC_IN_TIPO_LOC VARCHAR(100),
                        BAI_NU VARCHAR(100),
                        BAI_NO VARCHAR(100),
                        LOG_NU VARCHAR(100),
                        LOG_NO VARCHAR(100),
                        LOG_COMPLEMENTO VARCHAR(100),
                        CEP_LOG VARCHAR(100), 
                        TIPO_LOG VARCHAR(100),
                        BAI_NU_INI VARCHAR(100)
                        )
                  """
    
    try:
        print(f"Executando SQL:\n{create_sql}")  # Debug: mostrar o SQL que será executado
        stmt = ibm_db.exec_immediate(conn, create_sql)
        if stmt:
            #print(f"Tabela {table_name} criada com sucesso.")
            ibm_db.commit(conn)
            return True
        else:
            print("Falha ao executar comando CREATE TABLE")
            return False
    except Exception as e:
        print(f"Erro detalhado ao criar tabela: {str(e)}")
        print(f"SQLSTATE: {ibm_db.stmt_error()}")
        print(f"SQLCODE: {ibm_db.stmt_errormsg()}")
        ibm_db.rollback(conn)
        raise



def importar_csv_para_tabela_pandas(caminho_csv, conn, table_name, batch_size=10000):
    try:
        # Carregar o CSV no Pandas
        df = pd.read_csv(caminho_csv, delimiter=";", encoding="utf-8", dtype=str)
        df.columns = [coluna.strip().upper() for coluna in df.columns]  # Garantir nomes das colunas em maiúsculas
        
        # Substituir valores nulos ou inválidos com string vazia
        df.fillna("", inplace=True)  

        # Conectar ao banco usando o adaptador do ibm_db_dbi para Pandas
        db_conn = ibm_db_dbi.Connection(conn)
        
        # Preparar a query de inserção
        colunas = ", ".join(df.columns)
        placeholders = ", ".join(["?"] * len(df.columns))
        query = f"INSERT INTO {table_name} ({colunas}) VALUES ({placeholders})"
        
        # Dividir em lotes para melhor performance
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i+batch_size].values.tolist()
            try:
                with db_conn.cursor() as cursor:
                    cursor.executemany(query, batch)
                print(f"Lote {i // batch_size + 1} inserido com sucesso.")
            except Exception as e:
                print(f"Erro ao inserir lote {i // batch_size + 1}: {e}")
                traceback.print_exc()
                db_conn.rollback()
                raise
        
        # Commit final
        db_conn.commit()
        print(f"Dados importados com sucesso para {table_name}.")
    
    except Exception as e:
        print(f"Erro ao importar CSV: {e}")
        traceback.print_exc()
        ibm_db.rollback(conn)
        raise


#chamadas 
if conn:
        try:
            print("Iniciando o processo de importação...")
            start_time = datetime.now()
            print(f"Início: {start_time}")

            create_table(conn, table_name)
            importar_csv_para_tabela_pandas(caminho_arquivo_csv, conn, table_name)

            end_time = datetime.now()
            print(f"Término: {end_time}")
            print(f"Duração total: {end_time - start_time}")    
        except Exception as e:
            print(f"Erro no processo de importação: {e}")
        finally:
            # Fecha a conexão
            ibm_db.close(conn)
            print("Conexão encerrada.")   
