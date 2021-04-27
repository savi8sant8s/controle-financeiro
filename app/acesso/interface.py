from acesso.consultas import consulta
from validar import validador
from layout import layout

class ESTADO:
    ACESSO = 1
    HOME = 2
    SAIR = 3

def tentar_novamente():
    layout.msgCinzaClaro("Deseja tentar novamente?")
    layout.msgAmarela("Sim (1)")
    layout.msgAmarela("Não (2)")
    layout.tracos()
    opcao_escolhida = int(input("| Resposta: "))
    return (opcao_escolhida == 1)

def opcoes_acesso():
    layout.tracos()
    layout.msgCiano("Acesso")
    layout.tracos()
    layout.msgCinzaClaro("Qual operação deseja realizar:")
    layout.msgAmarela("Cadastrar (1)")
    layout.msgAmarela("Entrar    (2)")
    layout.msgAmarela("Sair      (3)")
    layout.tracos()

def cadastrar():
    while True:
        layout.tracos()
        layout.msgCiano("Cadastro")
        layout.tracos()
        nome = input("| Digite seu nome: ")
        email = input("| Digite seu email: ")
        senha = input("| Digite sua senha: ")
        if not validador.validarNome(nome):
            layout.tracos()
            layout.msgVermelha("O nome deve conter de 5 a 30")
            layout.msgVermelha("caracteres sem acento ou números.")
            layout.tracos()
        elif not validador.validarEmail(email):
            layout.tracos()
            layout.msgVermelha("Ex. de email válido: fulano@email.com.")
            layout.tracos()
        elif not validador.validarSenha(senha):
            layout.tracos()
            layout.msgVermelha("A senha deve conter de 4 a 32 caracteres.")
            layout.tracos()
        else:
            consulta.criar_usuario(nome, email, senha)
            layout.tracos()
            layout.msgVerde("Usuário cadastrado com sucesso.")
            layout.tracos()
            return (ESTADO.ACESSO, None)
        resposta = tentar_novamente()
        if resposta == False:
            return (ESTADO.ACESSO, None)

def login():
    while True:
        layout.tracos()
        layout.msgCiano("Login ")
        layout.tracos()
        email = input("| Digite seu email: ")
        senha = input("| Digite sua senha: ")
        if not validador.validarEmail(email):
            layout.tracos()
            layout.msgVermelha("Ex. de email válido: fulano@email.com.")
            layout.tracos()
        elif not validador.validarSenha(senha):
            layout.tracos()
            layout.msgVermelha("A senha deve conter de 4 a 32 caracteres.")
            layout.tracos()
        else:
            id_usuario = consulta.pegar_id_usuario(email, senha)
            if id_usuario == None:
                layout.tracos()
                layout.msgVermelha("Credenciais inválidas.")
                layout.tracos()
            else:
                return (ESTADO.HOME, id_usuario)
        resposta = tentar_novamente()
        if resposta == False:
            return (ESTADO.ACESSO, None)

def interface_acesso():
    opcoes_acesso()
    layout.tracos()
    opcao_escolhida = int(input("| Resposta: "))
    if opcao_escolhida == 1:
        return cadastrar()
    elif opcao_escolhida == 2:
        return login()
    elif opcao_escolhida == 3:
        return (ESTADO.SAIR, None)
    else:
        layout.limpar
        layout.tracos()
        layout.msgVermelha("Opção inválida. Tente novamente.")
        layout.tracos()
        return (ESTADO.ACESSO, None)