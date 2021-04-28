import sqlite3
from datetime import datetime

nome_bd = "controle-financeiro.db"

class banco_dados:
    def __init__(self):
        conexao = sqlite3.connect(nome_bd)
        comando = conexao.cursor()                 

        self.criar_tabelas(comando)
        self.criar_categorias_padrao(comando)
        self.criar_tipos_padrao(comando)

        conexao.commit()
        conexao.close()

    def criar_tabelas(self, comando):
        comando.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            user_name TEXT NOT NULL,
                            user_email TEXT UNIQUE NOT NULL,
                            user_password TEXT NOT NULL,
                            user_timestamp BLOB NOT NULL
                        )''')

        comando.execute('''CREATE TABLE IF NOT EXISTS types (
                            type_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            type_name TEXT UNIQUE NOT NULL
                        )''')
                        
        comando.execute('''CREATE TABLE IF NOT EXISTS categories (
                            cat_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                            cat_name TEXT UNIQUE NOT NULL,
                            cat_timestamp BLOB NOT NULL,
                            cat_deletable INTEGER NOT NULL
                        )''')

        comando.execute('''CREATE TABLE IF NOT EXISTS transactions (
                            trans_id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            trans_value	REAL NOT NULL,
                            type_id	INTEGER NOT NULL,
                            user_id	INTEGER NOT NULL,
                            cat_id	INTEGER NOT NULL,
                            trans_description	TEXT NOT NULL,
                            trans_timestamp	BLOB NOT NULL,
                            FOREIGN KEY(type_id) REFERENCES types(type_id),
                            FOREIGN KEY(cat_id) REFERENCES categories(cat_id),
                            FOREIGN KEY(user_id) REFERENCES users(user_id)
                        )''')

    def criar_categorias_padrao(self, comando):
        timestamp = datetime.now()
        values = ["Alimento", "Vestimenta", "Medicação", "Passagem", "Outros"]
        for value in values:
            comando.execute('''INSERT OR IGNORE INTO categories (cat_name, cat_timestamp, cat_deletable) VALUES (?,?,?)''', (value , timestamp, 0))


    def criar_tipos_padrao(self, comando):
        values = ["Receita", "Despesa"]
        for value in values:
            comando.execute('''INSERT OR IGNORE INTO types (type_name) VALUES (?)''', (value,))
        