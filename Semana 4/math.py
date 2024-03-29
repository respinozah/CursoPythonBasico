import os
import math

os.system("cls")

numero = int(input("Ingrese el numero: "))

print("\n--------- Funciones trigonometricas ---------")
seno = math.sin(math.radians(numero))
print(f"El seno de {numero} es {seno}.")
log_10 = math.log(10)
print(f"El logaritmo natural del {numero} es: {log_10}.")

print("\n--------- Funciones potencias ---------")
print(f"El exponencial de {numero} es {math.exp(numero)}.")
potencia = int(input(f"Indique la potencia a la que quiere elevar {numero}: "))
print(f"{numero} a la {potencia} es {math.pow(numero, potencia)}.")

print("\n--------- Funcion raiz ---------")
print(f"La raiz cuadrada de {numero} es {math.sqrt(numero)}")

print("\n--------- Funcion valor absoluto ---------")
print(f"El valor absoluto de {numero} es {math.fabs(numero)}")

print("\n--------- Constantes ---------")
print(f"Pi: {math.pi}")
