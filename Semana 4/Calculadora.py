import os

ciclo = "si"

def main():
    while ciclo == "si":
        print("Calculadora Team\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division")
        seleccion = int(input("Seleccione una opcion: "))

        if seleccion == 1:
            numero1 = int(input("Digite el primer valor de la suma: "))
            numero2 = int(input("Digite el segundo valor de la suma: "))
            suma = numero1 + numero2
            print(f"El resultado de la suma es: {suma}.")
            continuar()

        elif seleccion == 2:
            numero1 = int(input("Digite el primer valor de la resta: "))
            numero2 = int(input("Digite el segundo valor de la resta: "))
            resta = numero1 - numero2
            print(f"El resultado de la suma es: {resta}.")
            continuar()

        elif seleccion == 3:
            numero1 = int(input("Digite el primer valor de la multiplicacion: "))
            numero2 = int(input("Digite el segundo valor de la multiplicacion: "))
            multiplicacion = numero1 * numero2
            print(f"El resultado de la suma es: {multiplicacion}.")
            continuar()

        elif seleccion == 4:
            numero1 = int(input("Digite el primer valor de la division: "))
            numero2 = int(input("Digite el segundo valor de la division: "))
            division = numero1 / numero2
            print(f"El resultado de la suma es: {division}.")
            continuar()

        else:
            print("Opcion invalida")
            continuar()
        os.system("cls")

def continuar():
    global ciclo
    ciclo = str(input("Desea realizar otra operacion (si / no): "))

if __name__ == "__main__":
    main()