class senhaIncorretaError(Exception):
    pass


class SenhaFracaError(Exception):
    pass


def fazer_login(senha_usuario):
    logar = input('\n\nInforme sua senha -> ')

    if logar == senha_usuario:
        print('\nLogin efetuado com sucesso!\n')
    else:
        print('\nTente novamente!')
        raise senhaIncorretaError('senha incorreta!\n')
    
def cadastrar_senha():
    print('\nADASTRO DE SENHA --> ')
    senha_usuario = input('informe a senha --> ')

    if len(senha_usuario) < 10:
        print('\ntente novamente:')
        raise SenhaFracaError('Senha deve conter 10 caracteres!\n')
    else:
        print('\nSenha cadastrada com sucesso!\n')
        return senha_usuario


def menu():
    senha_usuario = '0'
    while True:
        try:
            opcao = int(input('1 - criar senha\n'
                              '2 - fazer login \n'
                              '3 - sair\n'
                              '--> '))
            if opcao == 1:
                senha_usuario = cadastrar_senha()
            elif opcao == 2:
                fazer_login(senha_usuario)
            elif opcao == 3:
                break
            else:
                print('opção invalida!\n')
                continue
        except SenhaFracaError as erro:
            print(erro)
        except senhaIncorretaError as erro:
            print(erro)


def main():
    menu()



main()