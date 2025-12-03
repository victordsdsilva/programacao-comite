def obtem_operaçao():
    n1,op,n2 = input('incira a conta --> ')
    return n1,op,n2


def calcular():
    n1,op,n2 = obtem_operaçao()
    try:
        if op == '+':
            print(n1, op, n2, '=', int(n1)+int(n2), '\n')
        elif op == '-':
            print(n1, op, n2, '=', int(n1)-int(n2), '\n')    
        if  op == '*':
            print(n1, op, n2, '=', int(n1)*int(n2), '\n')
        if op == '/':
            try:
               print(n1, op, n2, '=', int(n1)/int(n2), '\n') 
            except ZeroDivisionError:
                print('impossivel dividir por zero!\n')
    except ValueError:
        print('valor incerido é inválido')
                                  