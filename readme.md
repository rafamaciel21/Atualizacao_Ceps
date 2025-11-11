# Em construção!! 
# Passos de execução 

### O Presente script tem como objetivo atualizar os CEPs da base de dados com base em arquivos disponibilizados da base de dados dos Correios 

------------------------------------
Etapas criadas no notebook jupyter
------------------------------------
  - Criar a conexão com o banco de dados IBM DB2 
  - Realizar a verificação do arquivo comos CEPs
  - Realizar a comparação do que já existe no banco de dados com o que existe no arquivo
  - Atualizar dados existentes 
  - Inserir registros novos 

# 🐍 Projeto de Conexão e Manipulação de Dados IBM Db2 com Python

Este projeto foi desenvolvido em **Python** com o objetivo de realizar **conexão, leitura e manipulação de dados em um banco IBM Db2**, utilizando as bibliotecas **pandas** e **ibm_db** dentro do ambiente **Jupyter Notebook**.  

---

## 📚 Tecnologias Utilizadas

- **Python 3.x**
- **Jupyter Notebook**
- **IBM Db2**
- **Pandas**
- **ibm_db**
- **ibm_db_dbi**

---

## 🧩 Bibliotecas Importadas

```python
import ibm_db
import ibm_db_dbi
import pandas as pd
import csv
import traceback
import os
from datetime import datetime
```
--- 

## ⚙️ Instalação do Ambiente

```bash
git clone https://github.com/rafamaciel21/Atualizacao_Ceps.git
cd seu-repositorio

pip install pandas ibm_db ibm_db_dbi
```


## Garantir a conexão do banco de dados

```python
from conection.connect_db import conexao_db
import ibm_db_dbi as dbi

conn = conexao_db()
if conn:
    pconn = dbi.Connection(conn)
    print("Conexão DBI estabelecida com sucesso.")
else:
    print("Falha ao conectar ao banco.")
```
