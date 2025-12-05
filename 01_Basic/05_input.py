#nombre = input("Ingrese su nombre:\n")
#print(f"Hola, {nombre}")

age = input("Ingrese su edad:\n")
print(f"Dentro de 20 años tendras {int(age) + 20}")

age = int(input("Ingrese su edad:\n"))
print(f"Dentro de 20 años tendras {age + 20}")

print("Obtener multiples valores a la vez")
pais, ciudad = input("Ingrese su pais y ciudad separados por coma:\n").split()
print(f"Usted vive en {pais}, {ciudad}")