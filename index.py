import sqlite3

conexao = sqlite3.connect("controle-financeiro.db")

comando = conexao.cursor()

#Cria uma tabela
comando.execute("CREATE TABLE pessoas ( nome TEXT, idade INT, peso REAl)")

#Insere uma linha
comando.execute("INSERT INTO pessoas VALUES ('Sávio', 19, 60)")

#Salva as alterações
conexao.commit()

#Fecha a conexão
conexao.close()

