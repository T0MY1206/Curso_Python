import os

edad = 18
if edad >= 18:
    print("Eres mayor de edad")

edad = 16
if edad >= 18:
    print("Eres mayor de edad")

edad = 15 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

nota = 7
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Reprobado")

os.system("cls")
print("Condiciones multiples:")
edad = 18
tiene_carnet = True
if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

edad = 18
tiene_carnet = False
if edad >= 18 or tiene_carnet:
    print("Puedes conducir")
else:
    print("Paga coima")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("Puedes ir a la playa")
else:
    print("Trabajas")

print("Condiciones anidadas:")
edad = 18
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("Puedes ir a la joda")
    else:
        print("No tenes plata para la joda")
else:
    print("No eres mayor de edad, no podes ir a la joda")

if edad < 18:
    print("No podes ir a la joda")
elif tiene_dinero:
    print("Puedes ir a la joda")
else:
    print("Quedate en casas")

os.system("cls")

numero = 5
if numero:
    print("El numero no es cero")

numero = 0
if numero:
    print("El numero no es cero")

nombre = "Juan"
if nombre:
    print("El nombre no es vacio")

numero = 3
es_el_tres = numero == 3
if es_el_tres:
    print("El numero es 3")

os.system("cls")
print("Operador ternario:")
edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)