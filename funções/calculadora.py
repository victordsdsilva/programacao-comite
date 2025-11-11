def calculadora(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        if n2  / 0:
            print('divisao por 0!')
        else:
            return n1 / n2    

def main():
    continuar = True
    while continuar:
        numero1 = float(input('informe o primeiro valor --> '))
        numero2 = float(input('informe o segundo valor --> '))    
        operacao = float(input('informe a operacao --> '))
  
        resultado = calculadora(numero1, numero2,operacao)
        if resultado != None:
            print(f'{numero1} {operacao} {numero2} = {resultado}')

        continuar = input('deseja continuar? "S" ou "N" -->  ')
        if continuar == 'S':
            continuar = True
        elif continuar == 'N':
            continuar = False
        else:
            print('opção inválida')
            continue            

main()