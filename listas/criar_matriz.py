matriz = []

for i in range(10):
    lista = []
    for i in range(10):
        lista.append(i)
    
    matriz.append(lista)

for linha in matriz:
    for coluna in linha:
        print(coluna)

              