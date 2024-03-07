import os
os.system("cls")

edad = int(input("Por favor ingrese su edad: "))

if edad >= 18:
    print("-Usted es mayor de edad.")
elif edad < 18 and edad > 0:
    print("-Usted es menor de edad.")
elif edad <= 0:
    print("-La edad debe ser mayor a 0.")