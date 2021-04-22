import sqlite3
import os
from datetime import datetime

nome_bd = os.environ.get("nome_bd")

def criar_usuario(nome, email, senha):
    conexao = sqlite3.connect(nome_bd)
    comando = conexao.cursor()                 

    timestamp = datetime.now()
    comando.execute('''INSERT OR IGNORE INTO users (user_timestamp, user_name, user_email, user_password) VALUES (?,?,?,?)''', (timestamp, nome, email, senha))
    conexao.commit()

def pegar_id_usuario(email, senha):
    conexao = sqlite3.connect(nome_bd)
    comando = conexao.cursor()                 

    resposta = comando.execute('''SELECT user_id FROM users WHERE user_email = ? AND user_password = ?''', (email, senha))

    conexao.commit()
    return resposta.fetchone()
