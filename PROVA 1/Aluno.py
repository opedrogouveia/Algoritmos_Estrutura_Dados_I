from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, presenca = "Ausente"):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.presenca = presenca
    
    def __str__(self):
        txt = super().__str__()
        txt += "\n Matrícula: " + self.__matricula
        txt += "\n\n PRENSENÇA: " + self.presenca
        return txt

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, value):
        if value == "":
            print("A matrícula não pode ser vazia.")
        else:
            self.__matricula = value

    def marcarPresenca(self):
        if self.presenca == "Ausente":
            self.presenca = "Presente"

    def matricular(self):
        txt = "\n* ALUNO MATRICULADO COM SUCESSO! *\n"
        print(txt + str(self))