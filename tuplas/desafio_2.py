coordenadas = []
cont = 0

#criar coordenadas
for linha in range(3):
    temp = []
    for coluna in range(2):
        temp.append(cont + 1 )
        cont += 1

    coordenadas.append(tuple(temp))

coordenadas = tuple(coordenadas)
print(coordenadas, '\n')

for i in coordenadas:
    cont = 0
    x = 0
    y = 0

    for c in i:
        if cont == 0:
            x = c
        else:
            y = c
        cont += 1

    print(f'ponto: X={x}, y={y}')                