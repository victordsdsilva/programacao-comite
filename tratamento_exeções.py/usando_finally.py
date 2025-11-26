def obtem_valor():
    try:
        valor = int(input('informe um valor inteiro --> '))
    except ValueError:
        print('valor invalido!', end=' ')
        print('necessario ser um numero inteiro')
    else:
        print(f'valor informado é {valor}')
    finally:
        print('PROGRAMA ENCERRADO!')


def main():
    obtem_valor()


main()                       