from acesso.interface import interface_acesso
from banco_dados import banco_dados
from layout import layout

class ESTADO:
    ACESSO = 1
    HOME = 2
    SAIR = 3

def boas_vindas():
    layout.limpar()
    layout.tracos()
    layout.msgVerde("Seja bem-vindo(a)!!!")
    layout.msgVerde("Controle Financeiro")
    layout.tracos()

def iniciar():

    estado_atual = ESTADO.ACESSO
    id_usuario = None

    while True:
        if estado_atual == ESTADO.ACESSO:
            (estado_atual, id_usuario) = interface_acesso()
        elif estado_atual == ESTADO.HOME:
            print(id_usuario)
            break
        elif estado_atual == ESTADO.SAIR:
            break

banco_dados()
boas_vindas()
iniciar()

'''
Layout----
Saldo do usuário
Cadastrar transação
Cadastrar categoria
Listar transações
Transações por data--
Transações por categoria--
Sair

Consultas----
Lista de categorias
Lista de tipos
Criar transação
'''