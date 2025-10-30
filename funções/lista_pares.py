def pares(lista_numeros):
    
    lista_pares = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)

    return lista_pares

def main():
    lista_numeros = [1,2,3,4,5,6,7,8,9,10]
    lista_final = pares(lista_numeros)

    for n in lista_final:
        print(n, end=' ')
    print()

main()    