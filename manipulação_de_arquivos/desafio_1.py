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


