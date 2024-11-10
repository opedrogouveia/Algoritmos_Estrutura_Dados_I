from LinkedList import LinkedList

list = LinkedList()

list.show()

list.addStart("Guilherme")
list.addStart("Daniel")
list.addLast("João")
list.addStart("Camila")
list.addLast("Leonardo")

list.removeStart()
list.removeLast()

list.remove("Guilherme")
list.remove("Pedro")