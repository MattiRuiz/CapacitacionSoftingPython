import pickle
'''
lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]
fichero_binario = open("listaNombres", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario)
'''

fichero = open("listaNombres", "rb")
lista = pickle.load(fichero)
print(lista)