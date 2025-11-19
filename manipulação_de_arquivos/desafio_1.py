def ler_logs(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:

        logs = arquivo.readlines()

        resultados = {'INFO': 0, 'ERROR': 0, 'WARNING': 0}

        for linha in logs:
            if 'INFO' in linha:
                resultados['INFO'] += 1
            elif 'ERROR' in linha:
                resultados['ERROR'] += 1
            elif 'WARNING' in linha:
                resultados['WARNING'] += 1


    return resultados


def gerar_relatorio(resultados):
    with open('relatorio.txt', 'w') as arquivo:
        arquivo.write('RELATORIO DE LOGS\n')
        for chave, valor in resultados.items():
            arquivo.write(f'existem {valor} ocorrencias do log {chave}')


def main():
    nome_arquivo = 'desafio_logs.txt'
    resultados = ler_logs(nome_arquivo)
    gerar_relatorio(resultados)


main()                