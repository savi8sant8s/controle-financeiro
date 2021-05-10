import os
import time

class layout:
    def msg_vermelha(msg): 
        print("| " + "\033[91m {}\033[00m" .format(msg))

    def msg_verde(msg): 
        print("| " + "\033[92m {}\033[00m" .format(msg))

    def msg_amarela(msg): 
        print("| " + "\033[93m {}\033[00m" .format(msg))

    def msg_roxo_claro(msg): 
        print("| " + "\033[94m {}\033[00m" .format(msg))

    def msg_roxo(msg): 
        print("| " + "\033[95m {}\033[00m" .format(msg))

    def msg_ciano(msg): 
        print("| " + "\033[96m {}\033[00m" .format(msg))

    def msg_cinza_claro(msg): 
        print("| " + "\033[97m {}\033[00m" .format(msg))

    def msg_preta(msg): 
        print("| " + "\033[98m {}\033[00m" .format(msg))

    def tracos(quant=50):
        print("| " + "-" * quant)

    def formatar_saldo(msg):
        if msg == None:
            layout.msg_verde("R$ 0,00")
        elif msg >= 0:
            layout.msg_verde("R$ {0:.2f}".format(msg))
        else:
            layout.msg_vermelha("R$ {0:.2f}".format(msg))

    def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')
