def obtem_valor():
    try:
        valor = float(input('informe um numero --> '))
    except ValueError:
        print('valor invalio!', end=' ')
        print('necessario ser um numero inteiro!')
    else:
        print(f'valor informado é {valor}')
        return int(input('informe um valor -> '))
    

def main():
    obtem_valor()    


main()    