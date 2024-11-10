# Construa o algoritmo em Python de uma lista
# duplamente encadeada que possui uma função para
# inserir elementos em ordem alfabética, uma função para
# imprimir os elementos da lista e uma função para
# imprimir os elementos na ordem inversa.

from Train import Train
train = Train()
elements = ["Charlie", "Alice", "Eve", "Bob", "Dave"]

for element in elements:
    train.add(element)

train.showForward()
train.showBackward()