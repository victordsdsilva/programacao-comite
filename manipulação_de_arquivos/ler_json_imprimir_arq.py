def arq_json(arquivo):
  try:
    with open('dados.json', 'r') as arquivo:
        print(arquivo.read())
  except FileNotFoundError:
    print('arquivo nao encontrado')        

def main():
   arq_json("arq")


main()

   
