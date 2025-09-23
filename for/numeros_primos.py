qnt_primos = 0

for n in range(1, 1000):
    n_vezes_div = 0


    for n2 in range(1, n+1):
        if n % n2 == 0:
            n_vezes_div += 1

    if n_vezes_div == 2:
        print(f'numero primo {n}')  
        qnt_primos += 1

    if qnt_primos == 20:
        break 