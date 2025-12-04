class Retangulo:
    #Atributos
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    #metodos
    def calular_area(self):
        return self.altura * self.largura


def main():
    retangulo = Retangulo(int(input('informe a altura -> ')),
                          int(input('informe a largura -> ')))

    print(f'A area do retangulo é {retangulo.calular_area()}')


main()            
        