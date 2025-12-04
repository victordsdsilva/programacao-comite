class Aluno:
    #Atributos
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    #Metodo
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2


    def cadastrar_aluno():
        aluno = Aluno(input('nume do aluno -> '),
                      float(input('nota 1 do aluno -> ')),
                      float(input('nota 2 do aluno -> '))) 

        return aluno


    def main():
        aluno1 = cadastrar_aluno()
    
        