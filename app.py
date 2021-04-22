from interface_acesso import interface_acesso
from banco_dados import iniciar_bd

ACESSO = 1
HOME = 2
SAIR = 3

def boas_vindas():
    print("SEJA VINDO(A)")
    print("CONTROLE FINANCEIRO")


def iniciar():
    iniciar_bd()
    boas_vindas()
    ESTADO_ATUAL = ACESSO

    while True:
        if ESTADO_ATUAL == ACESSO:
            ESTADO_ATUAL = interface_acesso()
        elif ESTADO_ATUAL == HOME:
            print("Você está em HOME")
            break;
        elif ESTADO_ATUAL == SAIR:
            break

iniciar()
