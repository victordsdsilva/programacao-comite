def inverter_string(palavra='python'):
    palavra_invertida = palavra[:: -1]
    print(f'A palavra invrtida é {palavra_invertida}')


def main():
    palavra = input('informe uma palavra --> ')
    inverter_string(palavra)

main()    