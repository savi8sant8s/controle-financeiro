from acesso.interface import interface_acesso
from home.interface import interface_home
from banco_dados import banco_dados
from layout import layout

class ESTADO:
    ACESSO = 1
    HOME = 2
    SAIR = 3

def boas_vindas():
    layout.limpar()
    layout.tracos()
    layout.msg_verde("Seja bem-vindo(a)!!!")
    layout.msg_verde("Controle Financeiro")
    layout.tracos()

def iniciar():

    estado_atual = ESTADO.ACESSO
    id_usuario = None

    while True:
        if estado_atual == ESTADO.ACESSO:
            (estado_atual, id_usuario) = interface_acesso()
        elif estado_atual == ESTADO.HOME:
            (estado_atual, id_usuario) = interface_home(id_usuario)
        elif estado_atual == ESTADO.SAIR:
            break

banco_dados()
boas_vindas()
iniciar()