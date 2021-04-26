from acesso.consultas import criar_usuario, pegar_id_usuario
from validar import validarNome, validarEmail, validarSenha
from layout import limpar, mensagem, mensagemCentro, tracos, delay

ACESSO = 1
HOME = 2
SAIR = 3

def tentar_novamente():
    mensagem("Deseja tentar novamente?")
    mensagem("Sim (1)")
    mensagem("Não (2)")
    resposta = int(input("| Resposta: "))
    return (resposta == 1)


def opcoes_acesso():
    delay(1)
    tracos()
    mensagemCentro("Acesso")
    tracos()
    mensagem("Qual operação deseja realizar:")
    mensagem("Cadastrar (1)")
    mensagem("Entrar    (2)")
    mensagem("Sair      (3)")
    tracos()

def cadastrar():
    while True:
        tracos()
        mensagemCentro("Cadastro")
        tracos()
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        delay(1)
        if not validarNome(nome):
            tracos()
            mensagem("O nome deve conter de 5 a 30")
            mensagem("caracteres sem acento ou números.")
            tracos()
        elif not validarEmail(email):
            tracos()
            mensagem("Ex. de email válido: fulano@email.com.")
            tracos()
        elif not validarSenha(senha):
            tracos()
            mensagem("A senha deve conter de 4 a 32 caracteres.")
            tracos()
        else:
            criar_usuario(nome, email, senha)
            tracos()
            mensagem("Usuario cadastrado com sucesso")
            tracos()
            return (ACESSO, None)
        resposta = tentar_novamente()
        if resposta == False:
            return (ACESSO, None)

def login():
    while True:
        tracos()
        mensagemCentro("Login")
        tracos()
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        delay(1)
        if not validarEmail(email):
            tracos()
            mensagem("Ex. de email válido: fulano@email.com.")
            tracos()
        elif not validarSenha(senha):
            tracos()
            mensagem("A senha deve conter de 4 a 32 caracteres.")
            tracos()
        else:
            id_usuario = pegar_id_usuario(email, senha)
            if id_usuario == None:
                tracos()
                mensagem("Credenciais inválidas.")
                tracos()
            else:
                return (HOME, id_usuario)
        resposta = tentar_novamente()
        if resposta == False:
            return (ACESSO, None)

def interface_acesso():
    opcoes_acesso()
    tracos()
    opcao_escolhida = int(input("| Resposta: "))
    if opcao_escolhida == 1:
        return cadastrar()
    elif opcao_escolhida == 2:
        return login()
    elif opcao_escolhida == 3:
        return (SAIR, None)
    else:
        tracos()
        mensagem("Opção inválida. Tente novamente...")
        tracos()
        delay(1)
        limpar()
        return (ACESSO, None)