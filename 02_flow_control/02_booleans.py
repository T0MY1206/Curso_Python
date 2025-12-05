import os

print("Valores booleanos basicos:")
print(True)
print(False)

print("Operadores de comparacion:")
print("5 > 3:", 5 > 3)
print("5 < 3:", 5 < 3)
print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)
print("5 >= 5:", 5 >= 5)
print("5 <= 3:", 5 <= 3)


print("Comparacion de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera")
print("'Hola' == 'hola'", "Hola" == "hola")

print("\nOperadores lógicos:")
print("True and True:", True and True)
print("True and False:", True and False)
print("True or False:", True or False)
print("False or False:", False or False)
print("not True:", not True)
print("not False:", not False)

os.system("cls")
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)