def contagem_caracteres(palavra):
    return len(palavra)


def main():
    tamanho = contagem_caracteres(input('digite uma palavra --> '))
    print(f'A palavra tem {tamanho} caracteres')


main()    

   