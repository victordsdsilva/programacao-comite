opçao = -1
senha_encerrar = 1903
encerrar_votaçao = 1900
candidatos = []
contagem_votos = {'nulos': 0}

while opçao != senha_encerrar:
    opçao = input('oque deseja fazer? \n' \
    'opçao 1: cadastrar candidato \n' \
    'opçao 2: iniciar votaçao \n'
    'opçao 3: mostrar votos e vencedor \n'
    'opçao 0: sair \n\n' \
    'opçao --> ')


    if opçao.isdigit():
        opçao = int(opçao)


        if opçao == 1:
            qtd_candidatos = int(input('quantos candidatos deseja cadastrar '))


            #laço para cadastrar candidatos
            for c in range(1, qtd_candidatos+1):
                candidato = []
                nome_candidato = input(f'nome do candidato {c+1}')
                num_candidato = int(input(f'numero do candidato {c+1}'))
                #salva candidato
                candidato.append(nome_candidato)
                candidato.append(num_candidato)
                #adiciona candidato na lista principal
                candidatos.append(tuple(candidatos))
            
            print('\n\n')

        elif opçao == 2: 
            voto = -1
            #mostrar lista de candidatos
            while voto != encerrar_votaçao:
                for candidato in candidatos:
                    print(f'candidato {candidato[0]}  | numero {candidato[1]}')

                voto = int(input('vote no numero de um candidato --> '))
                #contabilisar votacao
                cont += 1
                for candidato in candidatos:
                    if voto == candidato[1]:
                        if candidato[0] not in contagem_votos:
                            contagem_votos.update({candidato[0:] }) 
                    
                    else:
                        contagem_votos[candidato[0]] += 1
                        break      
                    
            else:
                if cont == len(candidato):
                        contagem_votos['nulos'] += 1

        elif opçao == 3:
            #remove nulo incorreto da saida da votaçao '1900'
            contagem_votos['nulos'] -= 1

            #mostrar resultados e vencedor
            maior = 0
            vencedor = ''
            for key, value in contagem_votos.items():
                if value > maior:
                    maior = value
                    vencedor = key
                print(f'{key} | votos {value}')

            print(f'o vencedor é {vencedor} com {maior} votos')

            #se a opçao digitada nao for um numero cai aqui
    else:
        print('\n\nOpçao invalida\n\n')            