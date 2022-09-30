from lista import Lista

lista = Lista()

lista.adicionar(1)
lista.adicionar(2)
lista.adicionar(3, inicio = True)
lista.adicionar(4)
lista.adicionar(5, inicio = True)

lista.show()

lista.remover(2)

lista.show()