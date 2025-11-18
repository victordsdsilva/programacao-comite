import json

def criar_dicio(dados):
    dados = {"nome": "victor", "idade": "16"}
    with open("dados.json", "w" ) as d: 
      json.dump(dados, d, indent=4)

def main():
   criar_dicio("dados")

main()  