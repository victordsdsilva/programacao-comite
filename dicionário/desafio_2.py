alunos = {}
opçao = -1

while (opçao != 0):
    opçao = int(input('o que deseja fazer ??? \n' \
    'opçao 1: cadastrar aluno \n'
    'opçao 2: exibir média \n' 
    'opçao 3: exibir aluno com maior nota \n' 
    'opçao 0: sair \n\n' 
    'opcao ---> '))


    if opçao == 1:
        key_aluno = len(alunos) +1
        values_alunos = {}

        nome_aluno = input('informe o nome do aluno --> ')
        idade_aluno = int(input('informe a idade do aluno --> '))
        nota_aluno = float(input('informe a nota do aluno --> '))
        alunos.update({key_aluno: values_alunos})
        print()

    elif opçao == 2:
        soma_notas = 0

        for aluno in alunos.values():
            soma_notas += alunos['nota']

        print(f'a média das notas é {soma_notas / len(alunos)}')

    elif opçao == 3:
        maior = 0
        id = 0

    for id, aluno in alunos.items():
        if aluno['nota'] > maior:
            maior = aluno['nota']
            id_alunos = id

    print(f'o aluno com a maior nota é,{alunos[id_alunos]['nome']} | nota {maior}')  

else:
    print('\n opçao invalida \n')      