def contar_linhas():
    try:
        with open('log_txt') as arquivo:
            return len(arquivo.readlines())
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO!!!')

   

def main():
    qtd_linhas = contar_linhas()
    print(f'o arquivo lido {qtd_linhas} linhas!')


main()       
