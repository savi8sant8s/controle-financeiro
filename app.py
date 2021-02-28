import sqlite3

def inicio():
    conexao = sqlite3.connect("controle-financeiro.db")

    comando = conexao.cursor()

    #Cria uma tabela
    comando.execute("CREATE TABLE IF NOT EXISTS pessoas ( nome TEXT, idade INT, peso REAl)")

    #Insere uma linha
    comando.execute("INSERT INTO pessoas VALUES ('Sávio', 19, 60)")

    #Pega uma linha
    pessoas = comando.execute('SELECT * FROM pessoas')
    for row in pessoas:
            print(row[0])

    #Salva as alterações
    conexao.commit()

    #Fecha a conexão
    conexao.close()

inicio()
