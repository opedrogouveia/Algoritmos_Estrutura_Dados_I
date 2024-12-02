# Construa um algoritmo que peça ao usuário para informar o nome, a
# nota01 e a nota02 de um aluno. Guarde estas informações em um
# dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02) /2]
# e adicione ao dicionário. Ao final, imprima todos os dados do
# dicionário.

while True:
    nome = input("Qual o nome do aluno? ")
    nota01 = int(input("Qual a nota 01 do aluno? "))
    nota02 = int(input("Qual a nota 02 do aluno? "))

    aluno = {
        "nome": nome,
        "nota01": nota01,
        "nota02": nota02
    }

    notaFinal = (aluno["nota01"] + aluno["nota02"]) / 2

    aluno["notaFinal"] = notaFinal

    print(aluno)