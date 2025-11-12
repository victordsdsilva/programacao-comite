def encontrar_palavra(nome_arquivo, palavra):
    try:
        with open(nome_arquivo) as arquivo:
            texto = arquivo.readlines()
            cont = 0
            for linha in texto:
                if palavra.lower() in linha.lower():
                    cont += 1
                    print(f'palavra "{palavra.lower()}" encontrada! | qtd palavras encontradas {cont}')
    except FileNotFoundError:
        print('arquivo nao encontrado!!!')


def main():
    nome_arquivo = 'novo_texto.txt'
    palavra = input('qual a palavraesta procurando? --> ')
    encontrar_palavra(nome_arquivo, palavra)

main()                             
