numero = []
for i in range(5):
    numero.append(int(input(f'informe o {i+1}° numero -->')))

print(f'os numeros digitados foram', end=' ')
for i in numero:
    print(i, end=' ')
print(f'\nO maior numero digitado foi {max(numero)}')
print(f'\nO menor numero digitado foi {min(numero)}')
print(f'\nA media dos numero é {sum(numero)/len(numero)}')