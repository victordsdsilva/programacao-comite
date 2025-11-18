import json

def criar_dicio(dados):
    dados = {"nome": "victor", "idade": "16", "nasci": "2008"}
    with open("dados.json.pessoal", "w" ) as d: 
      json.dump(dados, d, indent=4)

def main():
   criar_dicio("dados")

main()