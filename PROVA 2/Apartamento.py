from Torre import Torre

class Apartamento:
    def __init__(self, numero, torre, vaga = None):
        self.id = None
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.prox = None

    def cadastrar(self):
        pass