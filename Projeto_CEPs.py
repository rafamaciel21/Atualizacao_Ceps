
''' 
    O Presente script tem como objetivo atualizar os CEPs da base de dados com base 
    em arquivos disponibilizados da base de dados dos Correios 

  ------------------------------
  |Etapas                      |
  ------------------------------
    1 - Criar a conexão com o banco de dados IBM DB2 
    2 - Realizar a verificação do arquivo comos CEPs
    3 - Realizar a comparação do que já existe no banco de dados com o que existe no arquivo
    4 - Atualizar dados existentes 
    5 - Inserir registros novos 
'''


import pandas as pd
import os 
import conection.connect_db as conn_db  
import ibm_db_dbi as dbi
import numpy as np
import traceback 

#conn = conn_db.conexao_db()
'''if conn:
    pconn = dbi.Connection(conn)
    print("Conexão DBI estabelecida com sucesso.")
else:
    print("Falha ao estabelecer conexão DBI.")  
cursor = pconn.cursor()   
'''
file_path = r"Dados\eDNE_Basico20101\Delimitado\LOG_LOCALIDADE.TXT"

df = pd.read_csv(file_path, sep="@", dtype=str, encoding='latin1', header=None, names=['LOC_NU', 'UF', 'CIDADE','CEP', 'SITUACAO', 'LOC_IN_TIPO_LOC','LOC_NU_SUB','LOC_NO_ABREV','COD_IBGE']) 

print(df['COD_IBGE'].head(10))

traceback.print_exc()





'''for index, row in df.iterrows():
    cep = row['CEP']
    logradouro = row['Logradouro']
    bairro = row['Bairro']
    cidade = row['Cidade']
    estado = row['Estado']
    
    cursor.execute("SELECT COUNT(*) FROM CEPS WHERE CEP = ?", (cep,))
    result = cursor.fetchone()
    
    if result[0] > 0:
        cursor.execute("""
            UPDATE CEPS 
            SET Logradouro = ?, Bairro = ?, Cidade = ?, Estado = ? 
            WHERE CEP = ?
        """, (logradouro, bairro, cidade, estado, cep))
        print(f"Registro atualizado para CEP: {cep}")
    else:
        cursor.execute("""
            INSERT INTO CEPS (CEP, Logradouro, Bairro, Cidade, Estado) 
            VALUES (?, ?, ?, ?, ?)
        """, (cep, logradouro, bairro, cidade, estado))
        print(f"Novo registro inserido para CEP: {cep}")'''










