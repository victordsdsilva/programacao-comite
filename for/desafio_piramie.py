saida = ''
tamanho_piramide = int(input("informe o tamanho da piramide --> "))

for n in range(1, tamanho_piramide+1):
    for n2 in range(1, n+1):
        print(n2, end='')
    print('\n')    