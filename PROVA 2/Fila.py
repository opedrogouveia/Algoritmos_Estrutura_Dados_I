from Apartamento import Apartamento
from Torre import Torre

garagem = {
    "vaga_A": None,
    "vaga_B": None,
    "vaga_C": None,
    "vaga_D": None,
    "vaga_E": None
}

class Fila():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def adicionar(self, numero, torre):
        vaga_disponivel = None
        for vaga, situacao in garagem.items():
            if situacao is None:
                vaga_disponivel = vaga
                garagem[vaga] = numero
                break
        novo_apartamento = Apartamento(numero, torre, vaga_disponivel)
        if self.primeiro is None:
            self.primeiro = novo_apartamento
            self.ultimo = novo_apartamento
        else:
            self.ultimo.prox = novo_apartamento
            self.ultimo = novo_apartamento
        self.imprimir()

    def remover(self):
        if self.primeiro is None:
            print("Nenhum apartamento para remover!")
        else:
            vaga_liberada = self.primeiro.vaga
            garagem[vaga_liberada] = None
            print(f"Apartamento {self.primeiro.numero} removido da vaga {vaga_liberada}")
            self.primeiro = self.primeiro.prox
            if self.primeiro is None:
                self.ultimo = None
        self.imprimir()

    def imprimir(self):
        print("------------------------")
        if self.primeiro is None:
            print("Fila está vazia!")
        else:
            aux = self.primeiro
            text = ""
            while aux:
                text += "Número do apartamento: " + aux.numero
                text += "\nTorre: " + str(aux.torre)
                text += "\nVaga: " + str(aux.vaga) + "\n"
                aux = aux.prox
            print(text)
        print("------------------------")