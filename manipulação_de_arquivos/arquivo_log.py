from datetime import datetime

def gerar_logs():
    with open('log_txt', 'w') as arquivo:
        for i in range(100):
            agora = datetime.now()
            arquivo.write(f'{agora} LOG {i+1} \n')

    print('log gerado com sucesso !!!')


def main(): 
    gerar_logs()

main()                