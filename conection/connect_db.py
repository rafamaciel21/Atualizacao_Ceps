import ibm_db
import ibm_db_dbi
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_db2_connection():
    try:
        # Obtém as credenciais do ambiente
        DB_HOST = os.getenv('DB_HOST')
        DB_PORT = os.getenv('DB_PORT')
        DB_NAME = os.getenv('DB_NAME')
        DB_USER = os.getenv('DB_USER')
        DB_PASSWORD = os.getenv('DB_PASSWORD')

        # String de conexão
        conn_string = (
            f"DATABASE={DB_NAME};"
            f"HOSTNAME={DB_HOST};"
            f"PORT={DB_PORT};"
            f"PROTOCOL=TCPIP;"
            f"UID={DB_USER};"
            f"PWD={DB_PASSWORD};"
        )

        # Estabelece a conexão
        ibm_conn = ibm_db.connect(conn_string, "", "")
        conn = ibm_db_dbi.Connection(ibm_conn)
        
        return conn

    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {str(e)}")
        return None
