from Apartamento import Apartamento
from Torre import Torre
from Fila import Fila

fila = Fila()

def menu():
    while True:
        escolha = int(input(" 1 - Nova Torre\n 2 - Novo Apartamento\n 3 - Alocar Vaga\n 4 - Liberar Vaga\nDigite um número: "))
        if escolha == 1:
            pass
        elif escolha == 2:
            pass
        elif escolha == 3:
            alocarVaga()
        elif escolha == 4:
            liberarVaga()

def alocarVaga():
    print("Informe os dados do Apartamento:")
    numeroApartamento = input(" Número: ")
    nomeTorre = input(" Nome da Torre: ")
    enderecoTorre = input(" Endereço da Torre: ")
    torre = Torre(nomeTorre, enderecoTorre)
    fila.adicionar(numeroApartamento, torre)

def liberarVaga():
    fila.remover()

menu()