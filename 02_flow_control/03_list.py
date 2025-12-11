import os
os.system("cls")


print("Crear listas")
lista1 = [1, 2, 3, 4, 5]
lista2 = ["mazanas", "peras", "platanos"]
lista3 = [1, "hola", 3.14, True]
lista_vacia = []
lista_de_listas = [[1, 2, 3], ["media", 5, 6]]
print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)

print("Acceder a los elementos de la lista")
print(lista2[0])
print(lista2[1])
print(lista2[-1])
print(lista2[-2])
print(lista_de_listas[1][0])

print(lista1[1:4])
print(lista1[:3])
print(lista1[3:])
print(lista1[:])

lista1 = [1, 2, 3, 4, 5 , 6 , 7 , 8 , 9 , 10]
print(lista1[::3])
print(lista1[::-1])

lista1[0] = 20
print(lista1)

lista = [1, 2, 3]

lista = lista + [4, 5, 6]
print(lista)

lista += [4, 5, 6]
print(lista)