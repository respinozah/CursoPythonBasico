import os

def main():
    os.system("cls")

    print("- ¿Es un numero multiplo de 5 o de 7? -")
    numero = int(input("Por favor ingrese un numero: "))

    if (numero % 5 == 0):
        print(f"El numero {numero} es multiplo de 5.")
    
    if (numero % 7 == 0):
        print(f"El numero {numero} es multiplo de 7.")

if __name__ == "__main__":
    main()