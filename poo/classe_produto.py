class produto:
    #Atributos
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    #Metodos
    def aplicar_desconto(self, desconto):
        return self.valor - self.valor + desconto / 100


def cadastrar_produto():
    p = produto(input('nome do produto -> '),
                float(input('valor do produto -> ')))

    return p


def main():
    p1 = cadastrar_produto()
    p_desconto = p1.aplicar_desconto(
        int(input('informe o percentual de desconto -> ')))

    print(f'preço normal do produto {p1.nome} | R${p1.valor:.21}')
    print(f'preço com desconto do produto {p1.nome} | R${p1.valor:.21}')


    main() 
        