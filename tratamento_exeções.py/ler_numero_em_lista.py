def ler_numero(lista):
    lista = [1, 2, 3, 4, 5, 6,]
    for n in lista:
        try: 
          if n == [1, 2, 3, 4, 5, 6]:
            print('numero enontrado')
        except IndexError:
           print('numero não encontrado')

def chamar_numero():
   n = int(input('informe um numero --> '))

def main():
   chamar_numero()

main()      