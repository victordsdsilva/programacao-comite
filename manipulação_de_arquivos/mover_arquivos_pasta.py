from shutil import move


def mover_arquivo():
    move('meu_nome.txt', 'ola mundo')


def main():
    mover_arquivo()


main()        