from acesso.interface import interface_acesso
from banco_dados import iniciar_bd
from layout import boas_vindas

ACESSO = 1
HOME = 2
SAIR = 3

iniciar_bd()
boas_vindas()

def iniciar():
    estado_atual = ACESSO
    id_usuario = None

    while True:
        if estado_atual == ACESSO:
            (estado_atual, id_usuario) = interface_acesso()
        elif estado_atual == HOME:
            print(id_usuario)
            break
        elif estado_atual == SAIR:
            break

iniciar()
