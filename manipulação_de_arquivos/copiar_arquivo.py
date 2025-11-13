from shutil import copy


def copiar_arquivo():
    copy('log_txt', 'bkp_log.txt')


def main():
    copiar_arquivo()


main()        