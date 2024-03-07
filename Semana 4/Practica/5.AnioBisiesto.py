import os
os.system("cls")

anio = int(input("Ingrese un año para determinar si bisiesto: "))

if (not anio % 4 and (anio % 100 or not anio % 400)):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")