def contar_positivos(l_numeros):

    cont_positivos = 0

    for numero in l_numeros:
        if numero > 0:
            cont_positivo += 1

    print(f'na lista existem {cont_positivos} numeros positivos' )


def main():
    lista_numeros = [1, 3, 5, 6, -9, -7, -2]
    contar_positivos(lista_numeros)

main()    