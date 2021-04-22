from consultas_acesso import criar_usuario
from consultas_acesso import pegar_id_usuario
from validar import validarNome, validarEmail, validarSenha

ACESSO = 1
HOME = 2
SAIR = 3

def tentar_novamente():
    print("Deseja tentar novamente?")
    print("Sim (1)")
    print("Não (2)")
    resposta = int(input())
    return resposta == 1


def opcoes_acesso():
    print("------------")
    print("|  ACESSO   |")
    print("------------")
    print("Qual operação deseja realizar:")
    print("Cadastrar (1)")
    print("Entrar    (2)")
    print("Sair      (3)")

def cadastrar():
    while True:
        print("------------")
        print("| CADASTRO |")
        print("------------")
        nome = input("Digite seu nome:")
        email = input("Digite seu email:")
        senha = input("Digite sua senha:")
        if not validarNome(nome):
            print("O nome deve conter de 5 a 30 caracteres sem acento ou números.")
        elif not validarEmail(email):
            print("Ex. de email válido: fulano@email.com.")
        elif not validarSenha(senha):
            print("A senha deve conter de 4 a 32 caracteres.")
        else:
            criar_usuario(nome, email, senha)
            print("Usuario cadastrado com sucesso")
            login()
        resposta = tentar_novamente()
        if resposta == False:
            return ACESSO

def login():
    while True:
        print("------------")
        print("|   LOGIN   |")
        print("------------")
        email = input("Digite seu email:")
        senha = input("Digite sua senha:")
        if not validarEmail(email):
            print("Ex. de email válido: fulano@email.com.")
        elif not validarSenha(senha):
            print("A senha deve conter de 4 a 32 caracteres.")
        else:
            resposta = pegar_id_usuario(email, senha)
            if resposta == None:
                print("Credenciais inválidas.")
            else:
                return HOME
        resposta = tentar_novamente()
        if resposta == False:
            return ACESSO

def interface_acesso():
    opcoes_acesso()
    opcao_escolhida = int(input())
    if opcao_escolhida == 1:
        cadastrar()
        return ACESSO
    elif opcao_escolhida == 2:
        estado = login()
        return estado
    elif opcao_escolhida == 3:
        return SAIR
    else:
        print("Opção inválida. Tente novamente...")
        return ACESSO