import os

def main():
    os.system("cls")
    numero = int(input("Por favor ingrese un numero: "))
    if (es_par(numero)):
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

def es_par(numero):
    if(numero % 2 == 0):
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()