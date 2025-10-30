def verificar_par(num):
    if num % 2 == 0:
        return 'par'
    else:
        return 'impar'

def main():
    resultado = verificar_par(int(input('informe um numero --> ')))
    print(resultado)


main()         