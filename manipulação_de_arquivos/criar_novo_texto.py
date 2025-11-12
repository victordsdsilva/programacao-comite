def obter_texto():
    texto = input('digite o novo texto -> ')
    print('novo texto obtido!!!')
    return texto


def escrever():
    with open('novo_texto.txt', 'w') as arquivo:
        arquivo.write(obter_texto())
    print('novo texto gravado!!!')

def main():
    escrever()

main()  