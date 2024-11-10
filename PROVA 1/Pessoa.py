from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf):
        self.id = None
        self.nome = nome
        self._cpf = cpf
    
    def __str__(self):
        txt = " Nome: " + self.nome
        txt += "\n CPF: " + self._cpf
        return txt

    @abstractmethod
    def marcarPresenca(self):
        pass