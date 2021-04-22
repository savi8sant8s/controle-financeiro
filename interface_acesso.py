from consultas_acesso import criar_usuario
from consultas_acesso import pegar_id_usuario

def opcoes_acesso():
    print("------------")
    print("|  ACESSO   |")
    print("------------")
    print("Qual operação deseja realizar:")
    print("Cadastrar (1)")
    print("Entrar    (2)")
    print("Sair      (3)")

def cadastrar():
    print("CADASTRO")
    nome = input("Digite seu nome:")
    email = input("Digite seu email:")
    senha = input("Digite sua senha:")
    criar_usuario(nome, email, senha)
    print("USUÁRIO CADASTRADO COM SUCESSO")

def login():
    print("LOGIN")
    email = input("Digite seu email:")
    senha = input("Digite sua senha:")
    resposta = pegar_id_usuario(email, senha)
    if resposta == None:
        print("Credenciais inválidas.")
        return 1
    else:
        return 2

def interface_acesso():
    opcoes_acesso()
    opcao_escolhida = int(input())
    if opcao_escolhida == 1:
        cadastrar()
        return 1
    elif opcao_escolhida == 2:
        estado = login()
        return estado
    elif opcao_escolhida == 3:
        return 3
    else:
        print("Opção inválida. Tente novamente...")
        return 1