nota = 0
soma_notas = 0
qnt_notas = 0
while nota >= 0:
    nota = int(input("informe a nota --> "))
    soma_notas += nota
    qnt_notas += 1

print(f'a media das notas é {soma_notas / qnt_notas}')    