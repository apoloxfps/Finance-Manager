# MODULO INTERFACE

# FUNÇÃO QUE IMPRIMI TITULOS PERSONALIZADOS
def cabecalho(titulo):
    print("=" * 42)
    print(titulo.center(42))
    print("=" * 42)


# FUNÇÃO INT INPUT COM TRATAMENTO DE DADOS
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError:
            print("ERRO digite um numero valido!")
        except KeyboardInterrupt:
            print("\nsuario preferiu não digita nada, FINALIZANDO...")
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
            print("\nUsuario preferiu não digita o valor, FINALZANDO...")
            return 0
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
