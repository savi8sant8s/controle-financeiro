import sqlite3
from datetime import datetime

nome_bd = "controle-financeiro.db"

class consulta:
    def criar_transacao(value, type_id, user_id, cat_id, description):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()                 

        timestamp = datetime.now()
        comando.execute('''INSERT OR IGNORE INTO transactions (trans_timestamp, trans_value, type_id, user_id, cat_id, trans_description) VALUES (?,?,?,?,?,?)''', (timestamp, value, type_id, user_id, cat_id, description))
        conexao.commit()

    def criar_categoria(cat_name, user_id):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()                 

        timestamp = datetime.now()
        comando.execute('''INSERT OR IGNORE INTO categories (cat_timestamp, cat_name, user_id) VALUES (?,?,?)''', (timestamp, cat_name, user_id))
        conexao.commit()

    def listar_categorias(user_id):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()

        resposta = comando.execute('''SELECT cat_name, cat_id FROM categories WHERE user_id IS NULL OR user_id = ?''', (user_id,))

        conexao.commit()
        return resposta.fetchall()

    def listar_categorias_deletaveis(user_id):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()

        resposta = comando.execute('''SELECT cat_name, cat_id FROM categories WHERE user_id = ?''', (user_id,))

        conexao.commit()
        return resposta.fetchall()

    def listar_transacoes(user_id):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()

        resposta = comando.execute('''SELECT c.cat_name, tr.trans_description, t.type_name, tr.trans_value FROM transactions AS tr INNER JOIN users AS u ON (u.user_id = tr.user_id) INNER JOIN types AS t ON (t.type_id = tr.type_id) INNER JOIN categories AS c ON (c.cat_id = tr.cat_id) WHERE u.user_id = ?''', (user_id,)) 
        
        conexao.commit()
        return resposta.fetchall()

    def listar_tipos():
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()

        resposta = comando.execute('''SELECT * FROM types''')
        
        conexao.commit()
        return resposta.fetchall()

    def saldo(user_id):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()
        
        resposta = comando.execute('''SELECT (SELECT SUM(trans_value) FROM transactions WHERE user_id = ? AND type_id = ?) - (SELECT SUM(trans_value) FROM transactions WHERE user_id = ? AND type_id = ?) AS saldo;''', (user_id, 1, user_id, 2,))

        conexao.commit()   
        return resposta.fetchone()[0]        


    def deletar_categoria(user_id, cat_id):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()

        comando.execute('''DELETE FROM categories WHERE user_id = ? AND cat_id = ?''', (user_id, cat_id))
        conexao.commit()