# • Construa um algoritmo de busca contendo um vetor de números
# inteiros de 20 posições.
# • O algoritmo deve ter duas funções, uma para busca sequencial e
# outra para busca binária.
# • Coloque um contador em cada função para contar as iterações de
# cada função.
# • Peça ao usuário que informe o valor que deseja procurar.
# • Então informe ao usuário se este valor existe no vetor e quantas
# iterações foram necessárias em cada função.

vetor = [5, 8, 12, 3, 20, 15, 7, 9, 1, 18, 4, 6, 10, 2, 11, 17, 14, 13, 19, 16]

def buscaSeq (vetor, valor):
    contadorSeq = 0
    for i in range(len(vetor)):
        contadorSeq += 1
        if vetor[i] == valor:
            print("Operações:", contadorSeq)
            return print("Valor:", valor, "\nPosição:", i)
    print("Operações:", contadorSeq)
    print("Valor:", valor, "não encontrado.")

def buscaBin (vetor, valor):
    contadorBin = 0
    inicio = 0
    fim = len(vetor) - 1
    while inicio <= fim:
        contadorBin += 1
        centro = inicio + (fim - inicio) / 2
        centro = int(centro)
        if valor == vetor[centro]:
            print("Operações:", contadorBin)
            return print("Valor:", valor, "\nPosição:", centro)
        elif valor > vetor[centro]:
            inicio = centro + 1
        else:
            fim = centro - 1
    print("Operações:", contadorBin)
    print("Valor:", valor, "não encontrado.")

valor = int(input("Digite um valor: "))
buscaSeq(vetor, valor)
print("-------------------------")
vetor.sort()
print(vetor)
buscaBin(vetor, valor)