from home.consultas import consulta
from layout import layout

class ESTADO:
    ACESSO = 1
    HOME = 2
    SAIR = 3

def opcoes_home():
    layout.tracos()
    layout.msg_ciano("Home")
    layout.tracos()
    layout.msg_cinza_claro("Qual operação deseja realizar:")
    layout.msg_amarela("Cadastrar transação (1)")
    layout.msg_amarela("Cadastrar categoria (2)")
    layout.msg_amarela("Listar transações   (3)")
    layout.msg_amarela("Deletar categoria   (4)")
    layout.msg_amarela("Sair                (5)")
    layout.tracos()

def opcoes_categoria(id_usuario, tipo):
    layout.tracos()
    layout.msg_cinza_claro("Selecione uma categoria:")
    if tipo == 1:
        categorias = consulta.listar_categorias(id_usuario)
    elif tipo == 2:
        categorias = consulta.listar_categorias_deletaveis(id_usuario)
    for categoria, cat_id in categorias:
        indice = [x[0] for x in categorias].index(categoria)
        layout.msg_amarela("{} ({})".format(indice, categoria))    
    layout.tracos()
    cat_indice = int(input("| Resposta: "))
    return categorias[cat_indice][1]

def interface_home(id_usuario):
    opcoes_home()
    layout.tracos()
    opcao_escolhida = int(input("| Resposta: "))
    if opcao_escolhida == 1:
        return cadastrar_transacao(id_usuario)
    elif opcao_escolhida == 2:
        return cadastrar_categoria(id_usuario)
    elif opcao_escolhida == 3:
        return listar_transacoes(id_usuario)
    elif opcao_escolhida == 4:
        deletar_categoria(id_usuario)
        layout.tracos()
        layout.msg_verde("Categoria deletada com sucesso.")
        layout.tracos()
        return (ESTADO.HOME, id_usuario)
    elif opcao_escolhida == 5:
        return (ESTADO.SAIR, None)
    else:
        layout.limpar
        layout.tracos()
        layout.msg_vermelha("Opção inválida. Tente novamente.")
        layout.tracos()
        return (ESTADO.HOME, None)

def cadastrar_transacao(id_usuario):
    while True:
        layout.tracos()
        layout.msg_ciano("Cadastro de Transação")
        layout.tracos()
        value = float(input("| Digite o valor: "))
        type_id = int(input("| Digite 1 para Receita | Digite 2 para Despesa: "))
        cat_id = opcoes_categoria(id_usuario, 1)
        description = input("| Descrição: ")
        if not value:
            print(value)
        elif not type_id:
            print(type_id)
        elif not cat_id:
            print(cat_id)
        elif not description:
            print(description)
        else:
            consulta.criar_transacao(value, type_id, id_usuario, cat_id, description)
            layout.tracos()
            layout.msg_verde("Transacao cadastrada com sucesso.")
            layout.tracos()
            return (ESTADO.HOME, id_usuario)
        return False

def cadastrar_categoria(id_usuario):
    while True:
        layout.tracos()
        layout.msg_ciano("Cadastro de Categoria")
        layout.tracos()
        cat_name = input("| Digite o nome da categoria: ")
        if not cat_name:
            print(cat_name)
        else:
            consulta.criar_categoria(cat_name, id_usuario)
            layout.tracos()
            layout.msg_verde("Categoria " + cat_name + " cadastrada com sucesso.")
            layout.tracos()
            return (ESTADO.HOME, id_usuario)

def listar_transacoes(id_usuario):
    while True:
        layout.tracos()
        layout.msg_ciano("Lista de transações")
        layout.tracos()
        transacoes = consulta.listar_transacoes(id_usuario)
        for transacao in transacoes:
            texto = ["Descrição: " + transacao[0],"Valor: " + str(transacao[1])]            
            layout.msg_roxo_claro(', '.join(texto))
        layout.tracos()
        layout.msg_amarela("Digite qualquer tecla para voltar")
        sair = int(input("|  Resposta: "))
        if sair != None:            
            return (ESTADO.HOME, id_usuario)

def deletar_categoria(id_usuario):
    return consulta.deletar_categoria(id_usuario, opcoes_categoria(id_usuario, 2))
    