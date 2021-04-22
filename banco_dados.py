import sqlite3

nome_bd = "controle-financeiro.db"

def iniciar_bd():
    conexao = sqlite3.connect(nome_bd)
    comando = conexao.cursor()                 

    criar_tabelas(comando)
    criar_categorias_padrao(comando)
    criar_tipos_padrao(comando)

    conexao.commit()
    conexao.close()

def criar_tabelas(comando):
    comando.execute('''CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        user_name TEXT NOT NULL,
                        user_email TEXT UNIQUE NOT NULL,
                        user_password TEXT NOT NULL,
                        user_timestamp BLOB NOT NULL
                    )''')

    comando.execute('''CREATE TABLE IF NOT EXISTS types (
                        type_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        type_name TEXT NOT NULL
                    )''')
                    
    comando.execute('''CREATE TABLE IF NOT EXISTS categories (
                        cat_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                        cat_name TEXT NOT NULL,
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

def criar_categorias_padrao(comando):
    pass

def criar_tipos_padrao(comando):
    pass
