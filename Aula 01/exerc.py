# • Construir um algoritmo que contenha 3 listas, cada lista contendo:
#   • Nomes de produtos
#   • Preços de cada produto
#   • Quantidades de cada produto
# • Construir uma função para imprimir um dos produtos da lista e uma
# função para retirar um dos produtos das listas. As funções devem receber
# um parâmetro que será usado para acessar a posição dos itens das listas
# que serão impressos ou retirados.

import pandas as pd

loja = {
    'nome_produto': ['Arroz', 'Azeite', 'Leite', 'Pão', 'Café', 'Feijão', 'Óleo', 'Açúcar', 'Sal', 'Macarrão'],
    'preço': [7.50, 30.00, 4.50, 8.50, 18.00, 6.00, 7.00, 4.00, 2.50, 5.00],
    'quantidade': [5, 3, 12, 8, 6, 7, 9, 8, 10, 15]
}
produtos = pd.DataFrame(loja)

def menu():
    while True:
        opcao = input(" 1 - Pesquisar Produto\n 2 Retirar Produto\n 3 - Consultar Produtos\nDigite um número: ")
        if opcao == 1:
            pesquisar_produto()
        elif opcao == 2:
            retirar_produto()
        elif opcao == 3:
            consultar_produtos()
        else:
            print("Digite um número de 1 a 3.")

def pesquisar_produto():
    while True:
        opcao = input("\nEscreva o nome do produto ('0' para retornar): ")
        if opcao == 0:
            menu()
        elif opcao == 
        
        municipios_encontrados = [bairro for bairro in lista_bairros if nome_municipio == bairro.municipio.title()]
        if nome_municipio == '0':
            sub_menu_consulta()
        elif municipios_encontrados:
            print(f"\nBairros de {nome_municipio}:")
            for bairro in municipios_encontrados:
                print(f"\n- {bairro.bairro.upper()}\n Situação: {bairro.situacao}\n Nível Água: {bairro.nivel}m\n Alerta Evacuação: {bairro.alerta}\n Energia: {bairro.energia}\n Abastecimento de Água: {bairro.agua}")
            while True:
                    opcao = input("\nGostaria de saber informações de outro município? (s/n): ").lower()
                    if opcao == "s":
                        break
                    elif opcao == "n":
                        menu()
                    else:
                        print("\nOPÇÃO INVÁLIDA! Por favor, digite 's' para pesquisa ou 'n' para voltar ao menu inicial.")
        else:
            print("Nenhum município encontrado.")

def retirar_produto():
    pass

def consultar_produtos():
    pass