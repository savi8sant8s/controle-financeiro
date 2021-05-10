from home.consultas import consulta
from validar import validador
from layout import layout
import time

class ESTADO:
    ACESSO = 1
    HOME = 2
    SAIR = 3

def tentar_novamente():
    layout.msg_cinza_claro("Deseja tentar novamente?")
    layout.msg_amarela("Sim (1)")
    layout.msg_amarela("Não (2)")
    layout.tracos()
    opcao_escolhida = int(input("| Resposta: "))
    return (opcao_escolhida == 1)

def opcoes_home(id_usuario):
    saldo = consulta.saldo(id_usuario)
    layout.tracos()
    layout.msg_ciano("Home")   
    layout.tracos()
    layout.msg_cinza_claro("Seu saldo:")
    layout.formatar_saldo(saldo)
    layout.tracos()
    layout.msg_cinza_claro("Qual operação deseja realizar:")
    layout.msg_amarela("Cadastrar transação (1)")
    layout.msg_amarela("Cadastrar categoria (2)")
    layout.msg_amarela("Listar transações   (3)")
    layout.msg_amarela("Deletar categoria   (4)")
    layout.msg_amarela("Sair                (5)")
    layout.tracos()

def opcoes_categoria(id_usuario, tipo):
    if tipo == 1:
        categorias = consulta.listar_categorias(id_usuario)
        msg = "Digite a respectiva numeração da categoria."
    elif tipo == 2:
        categorias = consulta.listar_categorias_deletaveis(id_usuario)
        msg = "Digite a respectiva numeração da categoria ou 'S' para sair."
    for categoria, cat_id in categorias:
        indice = [x[0] for x in categorias].index(categoria)
        layout.msg_amarela("({}) {}".format(indice, categoria))    
    layout.tracos()

    if categorias == []:
        layout.msg_vermelha("| Não há Categorias personalizadas. Tente novamente...")
        time.sleep(1)   
        return "sair"
    else:
        layout.tracos()
        layout.msg_cinza_claro("Selecione uma categoria:")

    layout.msg_cinza_claro(msg)
    cat_indice = input("|  Resposta: ")
    if (cat_indice in 'Ss'):
        return cat_indice
    elif int(cat_indice) > (len(categorias)-1) or int(cat_indice) < 0: 
        layout.msg_vermelha("| Categoria não existe. Tente novamente...")
        time.sleep(1)
        opcoes_categoria(id_usuario, tipo)     
    else:
        return categorias[int(cat_indice)][1]        

def interface_home(id_usuario):    
    opcoes_home(id_usuario)
    layout.tracos()
    opcao_escolhida = input("| Resposta: ")
    if not validador.validarCat(opcao_escolhida):
        layout.tracos()
        layout.msg_vermelha("Digite apenas números.")
        layout.tracos()
        time.sleep(1)
        return (ESTADO.HOME, id_usuario)
    else:
        opcao_escolhida = int(opcao_escolhida)
    if opcao_escolhida == 1:
        return cadastrar_transacao(id_usuario)
    elif opcao_escolhida == 2:
        return cadastrar_categoria(id_usuario)
    elif opcao_escolhida == 3:
        return listar_transacoes(id_usuario)
    elif opcao_escolhida == 4:
        deletar_categoria(id_usuario)
        return (ESTADO.HOME, id_usuario)
    elif opcao_escolhida == 5:
        return (ESTADO.SAIR, None)
    else:
        layout.tracos()
        layout.msg_vermelha("Opção inválida. Tente novamente")
        layout.tracos()
        time.sleep(1)
        return (ESTADO.HOME, id_usuario)

def cadastrar_transacao(id_usuario):
    while True:
        layout.tracos()
        layout.msg_ciano("Cadastro de Transação")
        layout.tracos()
        value = input("| Digite o valor (Ex.: 20.000,00): R$")
        type_id = input("| Digite 1 para Receita | Digite 2 para Despesa: ")
        cat_id = opcoes_categoria(id_usuario, 1)
        description = input("| Descrição: ")
        if not validador.validarDinheiro(value):
            layout.tracos()
            layout.msg_vermelha("Digite um valor válido. Ex.: 1.100,10")
            layout.tracos()
        elif not validador.validarTipo(type_id):
            layout.tracos()
            layout.msg_vermelha("| Tipo inválido. ")
            layout.msg_vermelha("| Digite 1 para Receita | Digite 2 para Despesa: ")
            layout.tracos()
        elif not validador.validarCat(str(cat_id)):
            layout.tracos()
            layout.msg_vermelha("| Categoria inválida.")
            layout.tracos()
        elif not validador.validarSenha(description):
            layout.tracos()
            layout.msg_vermelha("| Descrição inválida.")
            layout.tracos()
        else:
            consulta.criar_transacao(validador.filtrarDinheiro(value), type_id, id_usuario, cat_id, description)
            layout.tracos()
            layout.msg_verde("Transacao cadastrada com sucesso.")
            layout.tracos()
            return (ESTADO.HOME, id_usuario)
        resposta = tentar_novamente()
        if resposta == False:
            return (ESTADO.HOME, id_usuario)

def cadastrar_categoria(id_usuario):
    while True:
        layout.tracos()
        layout.msg_ciano("Cadastro de Categoria")
        layout.tracos()
        cat_name = input("| Digite o nome da categoria: ")
        if not validador.validarNome(cat_name):
            layout.tracos()
            layout.msg_vermelha("O nome deve conter de 5 a 30")
            layout.msg_vermelha("caracteres sem acento ou números.")
            layout.tracos()
        else:
            consulta.criar_categoria(cat_name, id_usuario)
            layout.tracos()
            layout.msg_verde("Categoria " + cat_name + " cadastrada com sucesso.")
            layout.tracos()
            return (ESTADO.HOME, id_usuario)

def listar_transacoes(id_usuario):
    layout.tracos()
    layout.msg_ciano("Lista de transações")
    layout.tracos()
    transacoes = consulta.listar_transacoes(id_usuario)
    if transacoes == []:
        layout.msg_vermelha("| Não há transações personalizadas. Tente novamente...")
        time.sleep(1)   
        return (ESTADO.HOME, id_usuario)
    for transacao in transacoes:
        texto = ["Categoria: " + str(transacao[0]),"\n|  Descricao: " + str(transacao[1]), "\n|  Tipo: " + str(transacao[2]), "\n|  Valor: R$" + str(transacao[3])]           
        layout.msg_roxo_claro(' '.join(texto))
        layout.tracos()
    return (ESTADO.HOME, id_usuario)

def deletar_categoria(id_usuario):
    resposta = opcoes_categoria(id_usuario, 2)
    if type(resposta) == str:
        return (ESTADO.HOME, id_usuario)
    else:
        layout.tracos()
        layout.msg_verde("Categoria deletada com sucesso.")
        layout.tracos()
        return consulta.deletar_categoria(id_usuario, resposta)
    