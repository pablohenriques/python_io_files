try:
    with open("dados/contatos.csv", encoding="latin_1") as arquivo_contatos:
        for linha in arquivo_contatos:
            print(linha, end='')
except FileNotFoundError:
    print("Arquivo não encontrado")
except PermissionError:
    print("Sem permissao de escrita")
finally:
    arquivo_contatos.close()
