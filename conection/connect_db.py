import os
os.add_dll_directory(r"C:\\Program Files\\IBM\\SQLLIB\\BIN")  # Ajuste o caminho para o local correto
os.environ["DB2CODEPAGE"] = "1252"
import ibm_db
import traceback

def conexao_db():
    # Informações de conexão
    dsn = (
        "DATABASE=CISSERP;"
        "HOSTNAME=172.29.232.220;"
        "PORT=50123;"
        "PROTOCOL=TCPIP;"
        "UID=dba;"
        "PWD=a9d9p8.E10;" 
    )
    try:
        conn = ibm_db.connect(dsn, "", "")
        print("Conexao estabelecida com sucesso.")
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        traceback.print_exc() # detalhes do erro
        return None
    