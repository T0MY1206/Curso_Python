###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("Ejercicio 1: Determinar el mayor de dos números")
numero_1, numero_2 = input("Ingrese 2 numeros enteros separados por un espacion").split()
if numero_1 > numero_2:
    print(f"El numero {numero_1} es mayor que {numero_2}")
elif numero_1 < numero_2:
    print(f"El numero {numero_2} es mayor que {numero_1}")
else:
    print("Los numeros son iguales")

print("Ejercicio 2: Calculadora simple")
num1, num2, op = input("Ingrese 2 numeros enteros separados por coma y una operacion (+, -, *, /) tambien separada por coma:").split(',')
if op == "+":
    print(f"El resultado de la suma es {int(num1) + int(num2)}")
elif op == "-":
    print(f"El resultado de la resta es {int(num1) - int(num2)}")
elif op == "*":
    print(f"El resultado de la multiplicacion es {int(num1) * int(num2)}")
elif op == "/":
    print(f"El resultado de la division es {int(num1) / int(num2)}")
else:
    print("Operacion no valida")

print("Ejercicio 3: Año bisiesto")
year = int(input("Ingrese un año:"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")

print("Ejercicio 4: Categorizar edades")
age = int(input("Ingrese una edad:"))
if age >= 0 and age <= 2:
    print("Bebé")
elif age >= 3 and age <= 12:
    print("Niño")
elif age >= 13 and age <= 17:
    print("Adolescente")
elif age >= 18 and age <= 64:
    print("Adulto")
else:
    print("Adulto mayor")