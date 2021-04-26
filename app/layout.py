import os
import time

def delay(tempo):
    time.sleep(tempo)

def boas_vindas():
    limpar()
    tracos()
    mensagemCentro("Seja Bem-vindo(a)!!!")
    delay(0.5)
    mensagemCentro("💸CONTROLE  FINANCEIRO💸",44)
    tracos()

def mensagemCentro(texto, tamanhoMaximo=46):
    tamanhoTexto = len(texto)
    espacosVazios = " " * int((tamanhoMaximo - tamanhoTexto)/2)
    print("| " + espacosVazios + texto + espacosVazios + " |")

def mensagem(texto, tamanhoMaximo=46):
    tamanhoTexto = len(texto)
    espacosVazios = " " * (tamanhoMaximo - tamanhoTexto)
    print("| " + texto + espacosVazios + " |")

def tracos(quant=50):
    print("-" * quant)

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')