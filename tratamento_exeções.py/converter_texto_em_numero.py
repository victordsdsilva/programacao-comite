def converter(texto):
    try:
        num = float(texto)
        print(f'{type(num)} | {num}')
        return True
    except ValueError:
        print('informação digitada não é um numero')
        print('tente novamente')
        return False
    

def obter_informaçao():
    while True:
        info = input('informe um numero --> ')

        if converter(info):
            break


def main():
    obter_informaçao()


main()                