palavra_secreta = input("informe a palavra secreta --> ")
palavra_encontrada = ["-"] * len(palavra_secreta)
chute_letra = ''
tentativas = 10

for tentativas in range(tentativas+1):
    chute_letra = input(f'chute uma letra {palavra_encontrada} -->')

    for t in range(len(palavra_secreta)):
        if palavra_secreta[t] == chute_letra:
            palavra_encontrada[t] == chute_letra

    if "-" not in palavra_encontrada:
        print('voce venceu !!!')
        break

    print(f'faltam apenas {tentativas - tentativas} tentativas')

else:
    print(f'voce perdeu, a palavra era {palavra_secreta}')        