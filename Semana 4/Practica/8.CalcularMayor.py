import os

def main():
    os.system("cls")

    print("-Calcular el numero mayor-")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
    numero3 = int(input("Ingrese el tercer numero: "))

    numeroMayor = 0

    if numero1 > numero2:
        if numero1 > numero3:
            numeroMayor = numero1
        else:
            numeroMayor = numero3
    elif numero2 > numero3:
        numeroMayor = numero2
    else:
        numeroMayor = numero3

    print(f"-Entre los numeros {numero1}, {numero2} y {numero3}, el numero mayor es {numeroMayor}.")

if __name__ == "__main__":
    main()