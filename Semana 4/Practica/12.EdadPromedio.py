import os

def main():
    os.system("cls")
    
    print("- Calcular la edad promedio -")
    
    edad1 = int(input("Ingrese la edad 1: "))
    edad2 = int(input("Ingrese la edad 2: "))
    edad3 = int(input("Ingrese la edad 3: "))

    promedio = (edad1 + edad2 + edad3) // 3

    print(f"El promerio de las edades: {edad1}, {edad2} y {edad3}, es de {promedio}.")

if __name__ == "__main__":
    main()