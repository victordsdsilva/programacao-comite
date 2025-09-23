maior = 0

for numero in range(0, 5):
    valor = int (input(f'informe o {numero + 1}° numero --> '))


    if valor > maior:
       maior = valor


print(f'o maior numero foi {maior}')      