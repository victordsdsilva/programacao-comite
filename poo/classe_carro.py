class carro:
    #Atributos
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
    
    #Metodos
    def ligar(self):
        print(f'ligando o {self.modelo} - {self.ano}')


def main():
    carro1 = carro(input('modelo do carro -> '), 
                   input('ano do carro -> '))
    
    carro1.ligar()

main()    
        
        