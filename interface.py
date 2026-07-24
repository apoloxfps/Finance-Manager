# MODULO INTERFACE

# FUNÇÃO QUE IMPRIMI TITULOS PERSONALIZADOS
def cabecalho(titulo):
    print("=" * 46)
    print(titulo.center(46))
    print("=" * 46)


# FUNÇÃO INT INPUT COM TRATAMENTO DE DADOS
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("ERRO digite um numero valido!")
        except KeyboardInterrupt:
            print("\nUsuario preferiu não digita nada, FINALIZANDO...")
            return 0
        else:
            return n


# FUNÇÃO FLOAT INPUT COM TRATAMENTO DE DADOS
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg).replace(",", "."))
        except ValueError:
            print("\033[31mERRO digite um valor valido!\033[m")
        except KeyboardInterrupt:
            print("\nUsuario preferiu não digitar o valor")
            return 0.0
        else:
            return n


# FUNÇÃO MENU QUE IMPRIMI TABELA DE E RETORNA OPCAO DIGITADA
def menu(*opcoes):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for opcao in opcoes:
        print(f"{c} - {opcao}")
        c += 1
    return leiaInt("Qual opção seria: ")


def exibirExtrato(lista):
    if not lista:
        print("Nenhuma trasanção registrada")
    else:
        cabecalho("EXTRATO FINANCEIRO")
        tot_receitas = 0
        tot_despesas = 0
        print(f"{'ID':<4} | {'DESCRIÇÃO':<15} | {'TIPO':<8} | {'VALOR':>8}")
        print("-" * 46)
        for trans in lista:
            print(
                f"{trans['id']:<4} | {trans['descricao']:<15} | {trans['tipo']:<8} | {trans['valor']:>8.2f}"
            )
            if trans["tipo"] == "receita":
                tot_receitas += trans["valor"]
            elif trans["tipo"] == "despesa":
                tot_despesas += trans["valor"]
        print("=" * 46)
        print(f"Total de receita: R$ {tot_receitas:.2f}")
        print(f"Total de despesa: R$ {tot_despesas:.2f}")
        print(f"Saldo: R$ {tot_receitas - tot_despesas:.2f}")
        print("=" * 46)
