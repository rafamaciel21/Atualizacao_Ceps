 O Presente script tem como objetivo atualizar os CEPs da base de dados com base 
    em arquivos disponibilizados da base de dados dos Correios 

  ------------------------------------
  |Etapas criadas no notebook jupyter|
  ------------------------------------
    1 - Criar a conexão com o banco de dados IBM DB2 
    2 - Realizar a verificação do arquivo comos CEPs
    3 - Realizar a comparação do que já existe no banco de dados com o que existe no arquivo
    4 - Atualizar dados existentes 
    5 - Inserir registros novos 