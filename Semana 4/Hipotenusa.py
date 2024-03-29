import math
import os

os.system("cls")
print("Calculo de la hipotenusa:")
cateto1 = int(input("- Ingrese el cateto 1: "))
cateto2 = int(input("- Ingrese el cateto 2: "))

hipotenusa = math.sqrt(
    math.pow(cateto1, 2) + math.pow(cateto2, 2)
)

print(f"La hipotenusa es: {hipotenusa}.\n")