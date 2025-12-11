 # =======================
 # SISTEMA DE BIBLIOTECA
 # =======================

 # Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __repr__(self):
        status = "disponivel"
          