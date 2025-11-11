try:
    with open('meu_nome.txt', 'r') as arquivo:
        for linha in arquivo:
            print(linha)
except FileNotFoundError:
    print('arquivo não encontrado')            