def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print('o divisor não pode ser zero')
    else:
        print(f'valor da divisão: {resultado}')


def obtem_valores():
    a = int(input('informe o primeiro valor --> '))                
    b = int(input('informe o segundo valor --> '))

    dividir(a, b)


def main():
    obtem_valores()

main()        