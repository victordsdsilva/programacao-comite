usuario = 'victor'
senha ='12345'
tentativas = 3

while tentativas <= 3:
    if input("informe o usuario --> ") == usuario:
        if input("informe a senha --> ") == senha:
            print(f'bem vindo {usuario}')
            break
        else:
            print("senha incorreta, tente novamente")

            tentativas -= 1

            print(f'tentativas restantes {tentativas}') 
    else:
        print("usuario incorreto, tente novamente")

        tentativas -= 1

        print(f'tentativas restantes {tentativas}')       
