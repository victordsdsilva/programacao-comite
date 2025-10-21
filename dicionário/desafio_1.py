palavras = {"ola","mundo","python","programa","comite","bola" }
qtd_letras = {}

for palavra in palavras:

    if f'qtd_letras - {len(palavra)}'not in qtd_letras.keys():
        chave = f'qtd_palavras - {len(palavra)}'
        valor = 1

        qtd_letras.update({chave: valor})

    else:
        qtd_letras [f'qtd_palavra - {len(palavra)}'] += 1


for chave, valor in qtd_letras.items():
    print(f'{chave} | {valor} ')         


