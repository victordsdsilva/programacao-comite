frase = "Boa Noite Turma do Comite"
espaço = " "

qtd_espaço = 0

for letra in frase:
    if letra == ' ':
        qtd_espaço += 1

print(f"existem {qtd_espaço} espaços ") 
