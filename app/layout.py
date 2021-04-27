import os
import time

class layout:
    def msgVermelha(msg): 
        print("| " + "\033[91m {}\033[00m" .format(msg))

    def msgVerde(msg): 
        print("| " + "\033[92m {}\033[00m" .format(msg))

    def msgAmarela(msg): 
        print("| " + "\033[93m {}\033[00m" .format(msg))

    def msgRoxoClaro(msg): 
        print("| " + "\033[94m {}\033[00m" .format(msg))

    def msgRoxo(msg): 
        print("| " + "\033[95m {}\033[00m" .format(msg))

    def msgCiano(msg): 
        print("| " + "\033[96m {}\033[00m" .format(msg))

    def msgCinzaClaro(msg): 
        print("| " + "\033[97m {}\033[00m" .format(msg))

    def msgPreta(msg): 
        print("| " + "\033[98m {}\033[00m" .format(msg))

    def tracos(quant=50):
        print("| " + "-" * quant)

    def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')
