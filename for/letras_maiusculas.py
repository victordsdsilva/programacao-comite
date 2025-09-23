frase = "Boa Noite Turma do Comite"
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

qtd_maiuscula = 0

for letra in frase:
    for letra_alfabeto in alfabeto:
        if letra == letra_alfabeto:
            qtd_maiouscula += 1

print(f"existem {qtd_maiuscula}letras maiusculas")            


