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

        resposta = comando.execute('''SELECT trans_description, trans_value FROM transactions WHERE user_id = ?''', (user_id,))

        conexao.commit()
        return resposta.fetchall()

    def listar_tipos():
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()

        resposta = comando.execute('''SELECT * FROM types''')
        
        conexao.commit()
        return resposta.fetchall()

    def deletar_categoria(user_id, cat_id):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()

        comando.execute('''DELETE FROM categories WHERE user_id = ? AND cat_id = ?''', (user_id, cat_id))
        conexao.commit()