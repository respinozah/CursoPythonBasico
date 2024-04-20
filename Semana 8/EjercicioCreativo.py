
try:
    valorNumero1 = int(input("Ingrese un valor numerico (1): "))
except ValueError as e:
    print("Error ingresando valor numero 1. El valor no es numero entero.")

try:
    valorNumero2 = int(input("Ingrese un valor numerico (2): "))
except ValueError as e:
    print("Error ingresando valor numero 2. El valor no es numero entero.")

try:
    valorTexto1 = str(input("Ingrese un valor de text (1): "))
except ValueError as e:
    print("Error ingresando valor de texto 1. El valor no es texto.")

try:
    valorTexto2 = str(input("Ingrese un valor de text (2): "))
except ValueError as e:
    print("Error ingresando valor de texto 2. El valor no es texto.")

print("Usar un texto como numero:")
try:
    int(valorTexto1)
    print(f"{valorTexto1} es un numero")
except ValueError as e:
    print("No se puede convertir texto a entero.")

print("Sumar texto y numero:")
try:
    resultado = valorNumero1 + valorTexto1
    print(f"El resultado es {resultado}")
except TypeError as e:
    print("No se puede sumar texto y entero.")

print("Dividir dos numeros:")
try:
    resultado = valorNumero1 / valorNumero2
    print(f"El resultado es {resultado}")
except ZeroDivisionError as e:
    print("No se puede dividir entre cero.")