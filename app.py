import sqlite3

def inicio():
    conexao = sqlite3.connect("controle-financeiro.db")

    comando = conexao.cursor()

    #Cria uma tabela
    comando.execute("CREATE TABLE IF NOT EXISTS pessoas ( nome TEXT, idade INT, peso REAl)")

    #Insere uma linha
    nome = input ("Qual o seu nome?")
    idade = int(input ("Qual o seu idade?"))
    peso = float(input ("Qual o seu peso?"))

    conexao.execute ('''INSERT INTO pessoas VALUES (?,?,?) ''', (nome,idade,peso))
    #comando.execute('SELECT * FROM pessoas WHERE coluna =(?,?,?)', (valueA,ValueB,ValueC))

    #Pega uma linha
    pessoas = comando.execute('SELECT * FROM pessoas')
    for row in pessoas:
            print(row)

    #Salva as alterações
    conexao.commit()

    #Fecha a conexão
    conexao.close()

inicio()
