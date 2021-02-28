import time

def esperar(segundos):
    time.sleep(segundos)

def imprimirCaractere(caractere):
    print("| " + (caractere * 46) + " |")

def imprimirLinha():
    print("-" * 50)

def imprimirEspaco():
    print("|" + (" " * 48) + "|")

def imprimirTexto(texto):
    espacos = " " * (46 - len(texto))
    print("| " + texto + espacos + " |")

imprimirLinha()
imprimirCaractere("#")
imprimirEspaco()
esperar(1)
imprimirTexto("CONTROLE-FINANCEIRO")
esperar(1)
imprimirEspaco()
imprimirCaractere("#")
imprimirLinha()