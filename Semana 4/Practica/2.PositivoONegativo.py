import os

def main():
    os.system("cls")
    numero = int(input("Por favor ingrese un numero: "))
    print(f"El numero {numero} es {tipoEntero(numero)}.")

def tipoEntero(numero):
    if(numero > 0):
        return "positivo"
    elif(numero < 0):
        return "negativo"
    elif(numero == 0):
        return "cero, ni positivo ni negativo"
    else:
        return "incorrecto, no es un numero entero"
    
if __name__ == "__main__":
    main()