from time import sleep

from dados import carregarDados, gerarId, salvarDados
from interface import cabecalho, exibirExtrato, leiaFloat, menu

cabecalho("Gerenciador de Finanças")
arquivo = "financas.json"
transacoes = carregarDados(arquivo)

while True:
    novo_dict = {}
    opcao = menu(
        "Cadastrar Receita", "Cadastrar Despesa", "Exibir Extrato", "Sair do Sistema"
    )
    match opcao:
        case 1 | 2:
            tipo_transacao = "receita" if opcao == 1 else "despesa"
            novo_dict["id"] = gerarId(transacoes)
            novo_dict["tipo"] = tipo_transacao
            novo_dict["descricao"] = str(input("Descrição: ")).strip().lower()
            novo_dict["valor"] = leiaFloat("Valor da transação: ")
            novo_dict["categoria"] = str(input("Categoria: ")).strip().lower()
            transacoes.append(novo_dict)
            salvarDados(arquivo, transacoes)
        case 3:
            exibirExtrato(transacoes)
        case 4 | 0:
            print("SAINDO DO SISTEMA...")
            sleep(1)
            break
        case _:
            print("Opção digitada não existe!!")
    sleep(1)
print("ATÉ LOGO!!!")
