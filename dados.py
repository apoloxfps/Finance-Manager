import json


def carregarDados(caminho):
    try:
        # abri o caminho e apelida de arquivo
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)  # vai carregar o arquivo que foi aberto
    except (FileNotFoundError, json.JSONDecodeError):  # possiveis erros
        return []  # retorna lista vazia
    else:
        return dados  # retorna a lista carregada


def salvarDados(caminho, lista):
    try:
        # vai tentar abrir o caminho e apelidar de arquivo
        with open(caminho, "w", encoding="utf-8") as arquivo:
            # vai escrever a lista no arquivo(caminnho)
            json.dump(lista, arquivo, indent=4, ensure_ascii=False)
    except (OSError, PermissionError, TypeError) as erro:  # mostra o erro caso não funcione
        print(f"Houve um erro de {erro}")
    else:
        print("Transação salva com SUCESSO!")


def gerarId(lista):
    if not lista:  # se lista estiver vazia
        return 1
    else:
        ultimo_id = lista[-1]["id"]  # o valor do id do ultimo dict
        return ultimo_id + 1  # o valor do id + 1
