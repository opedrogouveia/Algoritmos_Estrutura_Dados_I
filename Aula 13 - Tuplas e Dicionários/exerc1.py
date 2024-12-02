# Construa um algoritmo que possua uma tupla com os números escritos
# por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
# de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
# condicionais (if e switch).

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")

while True:
    escolha = int(input("Digite um número: "))

    print(numeros[escolha])


