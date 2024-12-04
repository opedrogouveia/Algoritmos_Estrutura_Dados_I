class Torre:
    def __init__(self, nome, endereco):
        self.id = None
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        txt = "Nome: " + self.nome
        txt += "\nEndereço: " + self.endereco
        return txt