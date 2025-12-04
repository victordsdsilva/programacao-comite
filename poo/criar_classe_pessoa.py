class pessoa:
    # atributos
    def  __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #métodos
    def apresentar(self):
        print(f'ola, seja bem vindo {self.nome}')
        print(f'voce esta com {self.idade} anos')

def main():
    nome = input('informe o nome da pessoa -> ')
    idade = int(input('informe a idade da pessoa -> '))
    pessoa1 = pessoa(nome, idade)
    pessoa1.apresentar()

main()    